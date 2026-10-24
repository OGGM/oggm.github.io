"""Find candidate publications that use OGGM.

1. Collect papers citing the OGGM reference paper (OpenAlex + Semantic Scholar).
2. Drop those already in _data/publications.yml or in _tools/publications_reviewed.yml.
3. For each remaining candidate, fetch open-access full text (HTML, else PDF) and
   extract the snippets mentioning OGGM, so a human (or Claude) can decide quickly
   whether the paper *uses* OGGM or only cites it.

Usage:
    python _tools/find_publications.py --cache /some/tmp/dir --out candidates.json

pypdf is optional (needed to read PDFs).
"""
import argparse
import concurrent.futures as cf
import difflib
import hashlib
import html
import io
import json
import os
import re
import time
import unicodedata

import requests
import yaml

try:
    import pypdf
except ImportError:
    pypdf = None

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
PUBS = os.path.join(REPO, '_data', 'publications.yml')
REVIEWED = os.path.join(HERE, 'publications_reviewed.yml')

# Maussion et al. 2019, GMD: The Open Global Glacier Model (OGGM) v1.1
SEED_DOI = '10.5194/gmd-12-909-2019'

UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/126.0 Safari/537.36')

# Mentions that indicate OGGM itself (not just the reference list entry)
PATTERN = re.compile(r'OGGM|Open Global Glacier Model|PyGEM|oggm\.org|'
                     r'cluster\.klima\.uni-bremen\.de|zenodo\.597193', re.I)
REF_TITLE = re.compile(r'The Open Global Glacier Model \(OGGM\) v1\.1', re.I)
# Copernicus interactive discussion comments (referee, author, editor, community)
COMMENT_DOI = re.compile(r'^10\.5194/.*-((rc|ac|cc|ec|ed|co)\d+|supplement)$')
COMMENT_TITLE = re.compile(r'^(reply on|interactive comment|point by point response|comment on)', re.I)
PDF_META = re.compile(r'<meta[^>]+name=["\']citation_pdf_url["\'][^>]+content=["\']([^"\']+)', re.I)
PDF_META2 = re.compile(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+name=["\']citation_pdf_url', re.I)


def norm_doi(d):
    if not d:
        return None
    d = d.lower().strip()
    return re.sub(r'^https?://(dx\.)?doi\.org/', '', d)


def norm_title(t):
    # NFKC turns PDF ligatures (e.g. 'ﬂ') into plain letters
    t = unicodedata.normalize('NFKC', t or '').lower()
    return re.sub(r'[^a-z0-9]', '', t)


def known_papers():
    dois, titles = set(), set()
    for f in [PUBS, REVIEWED]:
        if not os.path.exists(f):
            continue
        data = yaml.safe_load(open(f)) or []
        if f == PUBS:
            entries = [e for c in data for e in c['entries']]
        else:
            entries = data
        for e in entries:
            if e.get('doi'):
                dois.add(norm_doi(str(e['doi'])))
            if e.get('title'):
                titles.add(norm_title(e['title']))
    return dois, titles


def openalex_citing():
    w = requests.get(f'https://api.openalex.org/works/doi:{SEED_DOI}', timeout=30).json()
    wid = w['id'].split('/')[-1]
    # Page-number paging (cursor paging needs an API key)
    out, page = [], 1
    while True:
        r = requests.get('https://api.openalex.org/works', timeout=60, params={
            'filter': f'cites:{wid}', 'per-page': 200, 'page': page,
            'select': 'id,doi,title,publication_year,type,primary_location,'
                      'best_oa_location,locations,abstract_inverted_index'}).json()
        if not r.get('results'):
            if r.get('error'):
                print('OpenAlex:', r.get('error'), r.get('message'))
            break
        out += r['results']
        page += 1
    res = []
    for x in out:
        abstract = ''
        inv = x.get('abstract_inverted_index')
        if inv:
            pos = sorted((p, w) for w, ps in inv.items() for p in ps)
            abstract = ' '.join(w for _, w in pos)
        src = ((x.get('primary_location') or {}).get('source') or {})
        urls = []
        for loc in [x.get('best_oa_location')] + (x.get('locations') or []):
            if loc:
                for k in ['pdf_url', 'landing_page_url']:
                    if loc.get(k) and loc[k] not in urls:
                        urls.append(loc[k])
        res.append(dict(doi=norm_doi(x.get('doi')), title=x.get('title'),
                        year=x.get('publication_year'), type=x.get('type'),
                        venue=src.get('display_name'), abstract=abstract,
                        urls=urls, source='openalex'))
    return res


def s2_citing():
    res, offset = [], 0
    while offset is not None:
        for attempt in range(5):
            r = requests.get(f'https://api.semanticscholar.org/graph/v1/paper/DOI:{SEED_DOI}/citations',
                             params={'fields': 'title,year,externalIds,venue,openAccessPdf,abstract',
                                     'limit': 500, 'offset': offset}, timeout=60)
            if r.status_code == 200:
                break
            time.sleep(5)
        else:
            print('Semantic Scholar failed, continuing without it')
            return res
        j = r.json()
        for c in j.get('data', []):
            p = c['citingPaper']
            ids = p.get('externalIds') or {}
            doi = norm_doi(ids.get('DOI'))
            if not doi and ids.get('ArXiv'):
                doi = f'10.48550/arxiv.{ids["ArXiv"]}'.lower()
            pdf = (p.get('openAccessPdf') or {}).get('url')
            res.append(dict(doi=doi, title=p.get('title'), year=p.get('year'),
                            venue=p.get('venue'), abstract=p.get('abstract') or '',
                            urls=[pdf] if pdf else [], source='s2'))
        offset = j.get('next')
    return res


def merge(lists):
    by_key = {}
    for lst in lists:
        for p in lst:
            key = p['doi'] or norm_title(p['title'])
            if not key:
                continue
            if key in by_key:
                q = by_key[key]
                q['urls'] += [u for u in p['urls'] if u not in q['urls']]
                q['abstract'] = q['abstract'] or p['abstract']
                q['source'] += '+' + p['source']
                for k in ['venue', 'year', 'title']:
                    q[k] = q.get(k) or p.get(k)
            else:
                by_key[key] = dict(p)
    return list(by_key.values())


def html_to_text(s):
    s = re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>', ' ', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s))


def fetch(url, cache):
    fn = os.path.join(cache, hashlib.md5(url.encode()).hexdigest())
    if os.path.exists(fn):
        return open(fn, 'rb').read()
    try:
        r = requests.get(url, headers={'User-Agent': UA}, timeout=40, allow_redirects=True)
        data = r.content if r.status_code == 200 else b''
    except Exception:
        data = b''
    open(fn, 'wb').write(data)
    return data


def to_text(data):
    if data[:5] == b'%PDF-':
        if pypdf is None:
            return ''
        try:
            rd = pypdf.PdfReader(io.BytesIO(data))
            return re.sub(r'\s+', ' ', ' '.join(p.extract_text() or '' for p in rd.pages))
        except Exception:
            return ''
    return html_to_text(data.decode('utf-8', 'ignore'))


def get_fulltext(p, cache):
    urls = list(p['urls'])
    if p['doi'] and p['doi'].startswith('10.48550/arxiv.'):
        urls.append('https://arxiv.org/pdf/' + p['doi'].split('arxiv.', 1)[1])
    elif p['doi']:
        urls.append('https://doi.org/' + p['doi'])
    best, best_url = '', None
    seen = set()
    while urls:
        u = urls.pop(0)
        if u in seen:
            continue
        seen.add(u)
        data = fetch(u, cache)
        if data[:5] != b'%PDF-':
            # landing pages often only show the abstract but link the PDF
            h = data[:300000].decode('utf-8', 'ignore')
            m = PDF_META.search(h) or PDF_META2.search(h)
            if m:
                urls.insert(0, html.unescape(m.group(1)))
        t = to_text(data)
        # a full paper is long; landing pages with abstract only are short
        if len(t) > len(best):
            best, best_url = t, u
        if len(t) > 30000 and PATTERN.search(t):
            break
    return best, best_url


def snippets(text, width=300, nmax=8):
    spans = []
    for m in PATTERN.finditer(text):
        a, b = max(0, m.start() - width), min(len(text), m.end() + width)
        if spans and a <= spans[-1][1]:
            spans[-1][1] = b
        else:
            spans.append([a, b])
    out = []
    for a, b in spans:
        s = text[a:b]
        if REF_TITLE.search(s) and len(PATTERN.findall(s)) <= 2:
            continue  # just the reference list entry
        out.append(s)
    return out[:nmax], len(out)


def published_version(doi):
    """For a preprint DOI, return the DOI of the published paper (Crossref relation)."""
    m = None
    for attempt in range(5):
        try:
            r = requests.get('https://api.crossref.org/works/' + doi, timeout=30)
        except Exception:
            r = None
        if r is not None and r.status_code == 200:
            m = r.json()['message']
            break
        if r is not None and r.status_code == 404:
            return None
        time.sleep(2 + 3 * attempt)  # rate limited
    if m is None:
        return None
    rel = m.get('relation', {}).get('is-preprint-of', [])
    return norm_doi(rel[0]['id']) if rel else None


def doi_from_title(title):
    """Semantic Scholar sometimes has no DOI: look it up on OpenAlex by exact title."""
    try:
        r = requests.get('https://api.openalex.org/works', timeout=30,
                         params={'search': title, 'per-page': 5, 'select': 'doi,title'}).json()
    except Exception:
        return None
    for x in r.get('results', []):
        if x.get('doi') and similar(x['title'], title):
            return norm_doi(x['doi'])
    return None


def similar(t1, t2, thresh=0.9):
    """Titles from PDFs carry junk (line numbers, trailing words): compare loosely."""
    a, b = norm_title(t1), norm_title(t2)
    if not a or not b:
        return False
    return a == b or difflib.SequenceMatcher(None, a, b).ratio() >= thresh


def process(p, cache):
    if not p['doi'] and p.get('title'):
        p['doi'] = doi_from_title(p['title'])
    if p['doi']:
        p['published_doi'] = published_version(p['doi'])
    text, url = get_fulltext(p, cache)
    p['fulltext_chars'] = len(text)
    p['fulltext_url'] = url
    p['n_mentions'] = len([m for m in PATTERN.finditer(text)])
    p['snippets'], p['n_snippets'] = snippets(text)
    if not p['snippets'] and p['abstract'] and PATTERN.search(p['abstract']):
        p['snippets'] = ['[abstract] ' + p['abstract']]
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cache', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--workers', type=int, default=4)
    args = ap.parse_args()
    os.makedirs(args.cache, exist_ok=True)

    oa, s2 = openalex_citing(), s2_citing()
    print(f'OpenAlex: {len(oa)}, Semantic Scholar: {len(s2)}')
    allp = merge([oa, s2])
    dois, titles = known_papers()
    allp = [p for p in allp if not (p['doi'] and COMMENT_DOI.match(p['doi']))
            and not COMMENT_TITLE.match(p['title'] or '')]
    cand = [p for p in allp
            if not (p['doi'] in dois or norm_title(p['title']) in titles)]
    print(f'Unique citing: {len(allp)}, already listed/reviewed: {len(allp) - len(cand)}, '
          f'to check: {len(cand)}')

    with cf.ThreadPoolExecutor(args.workers) as ex:
        cand = list(ex.map(lambda p: process(p, args.cache), cand))
    # DOIs found by title may point to known papers or comments
    cand = [p for p in cand if not (p['doi'] and (p['doi'] in dois or COMMENT_DOI.match(p['doi'])))]
    print(f'After DOI lookup: {len(cand)} candidates')
    # preprints whose published version is listed, reviewed, or also a candidate
    cand = [p for p in cand if p.get('published_doi') not in dois or not p.get('published_doi')]
    cand_dois = {p['doi'] for p in cand}
    for p in cand:
        pub = p.get('published_doi')
        p['duplicate_of'] = pub if pub in cand_dois else None
    print(f'After removing preprints of listed papers: {len(cand)} candidates')
    json.dump(cand, open(args.out, 'w'), indent=1, ensure_ascii=False)
    print(f'Wrote {args.out}')


if __name__ == '__main__':
    main()

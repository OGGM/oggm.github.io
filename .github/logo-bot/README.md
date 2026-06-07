# Logo Rotation PR Bot

This bot opens pull requests to rotate the logo by date across three OGGM sites.

## How it works

- Workflow: `.github/workflows/logo-rotation-pr.yml`
- Script: `.github/logo-bot/update_logo.py`
- Config: `.github/logo-bot/events.json`

The workflow runs daily and opens three parallel jobs, one per target repo:

| Job | Repo | Branch | Config file |
|-----|------|--------|-------------|
| `rotate-website` | `OGGM/oggm.github.io` | `master` | `_config.yml` |
| `rotate-docs` | `OGGM/oggm` | `stable` | `docs/conf.py` |
| `rotate-tutorials` | `OGGM/tutorials` | `stable` | `_config.yml` |

Each job:
1. Computes the active event window (fixed-date or lunar holiday window).
2. Updates the logo field in the target config file.
3. Opens or updates a PR only when the logo value changes.

## Required secret

Cross-repo jobs (`rotate-docs`, `rotate-tutorials`) need a secret named
`CROSS_REPO_PAT` in `OGGM/oggm.github.io` → Settings → Secrets → Actions.

The token must be a fine-grained PAT with **Contents: read/write** and
**Pull requests: read/write** on both `OGGM/oggm` and `OGGM/tutorials`.

## Event configuration

Edit `.github/logo-bot/events.json` to change windows or add new events.

### `targets` array

Each target has:

- `id`: identifier used with `--target` flag.
- `repo`: GitHub repo (omit for the current repo).
- `branch`: branch to open the PR against.
- `config_file`: path within the repo to the file being modified.
- `format`: `yaml_logo` (Jekyll/Jupyter Book `logo:` field) or `sphinx` (`html_logo = ...`).
- `default_logo`: logo value used outside event windows.
- `celebration_logo_prefix`: prepended to `logo_filename` during an event.
- `logo_event_url_field` (optional): YAML key for a clickable logo URL (website only).

### `events` array

Each event has:

- `name`: identifier used in branch/PR naming.
- `logo_filename`: filename of the celebration logo (same across all repos).
- `source_url`: event information URL. When set, the website logo becomes clickable.
- `priority`: higher value wins if windows overlap.
- `rules`: one or more date rules.

Supported rule types:

- `fixed_range`
  - `start`: `MM-DD`
  - `end`: `MM-DD`
  - Supports year wrap (for example `12-15` to `01-05`).
- `holiday_window`
  - `country`: ISO country code used by `python-holidays`.
  - `contains`: substring used to match holiday names.
  - `start_offset`: days before holiday date.
  - `end_offset`: days after holiday date.

## Testing

Run workflow manually (`workflow_dispatch`) and set `date` to test any day.

You can also run locally (targets the website by default):

```bash
python -m pip install -r .github/logo-bot/requirements.txt
python .github/logo-bot/update_logo.py --today 2026-12-20
python .github/logo-bot/update_logo.py --today 2026-12-20 --target docs --workdir /path/to/oggm
```

## Notes on lunar events

Lunar event dates are resolved through `python-holidays` at runtime, which currently gives the expected dates for Chinese New Year, Diwali, and Eid al-Fitr for 2026-2030.

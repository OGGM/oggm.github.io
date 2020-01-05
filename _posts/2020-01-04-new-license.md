---
layout: post
title: The OGGM ecosystem uses a new license
subtitle: bye-bye copyleft
author: Fabien Maussion
date: 2020-01-04T00:00:00
tags: other
---

For better or for worse, OGGM just changed the license of all our
software (OGGM, OGGM-Edu, OGGMcontrib, rgitools, etc.) from GPLv3 to the more
permissive [BSD-3-Clause License](https://github.com/OGGM/oggm/blob/master/LICENSE.txt).

It was not easy to make this decision: when we chose GPLv3, it was by
conviction that all software that uses our work should also be free software,
hence the choice of a [copyleft license](https://en.wikipedia.org/wiki/Copyleft).
There are plenty of vivid debates online
about which license is "more free" than others, and we won't start a flame
war here.

After some thought, we (well, mostly me, but I was supported by most of the
OGGM contributors) settled for BSD3.
We had quite some discussion [on github](https://github.com/OGGM/oggm/issues/858)
about this, and I am going to summarize the main points here:



1. The OGGM projects provide a framework from which many models and other software
can benefit from ([OGGM-Edu](http://edu.oggm.org) is one of them, and we hope
to engage more models, such as the MIT licensed [SERMeQ](https://github.com/ehultee/plastic-networks)
and [PyGEM](https://github.com/drounce/PyGEM) projects).
With the GPL license, we would enforce our license to these downstream
projects (or, worse, limit the endorsement of OGGM because of license issues).
With BSD3, including OGGM code is as easy as adding our copyright notice to
your repository.

2. The GPL license is very complex and wordy. BSD3 (or MIT) are simple and clear.

3. Even with GPL, there is no guarantee that modifications to OGGM will be made
freely available. Previously, modifications of OGGM could not be shared openly
thanks to GPLv3, that's true; however, single authors or organisations could take
OGGM, make it better, and
publish/produce data based on their modified version of OGGM without having
to share it to others (as long as their modifications remained private within their
"organisation"). This is not better with BSD, but at least the license is now
simple and easy: people are allowed to do so if they wish.

4. After settling on MIT (which is the license recommended by Github and probably
the "easiest" and most used one), I changed my mind for BSD 3-clause. The
reasons are that (i) BSD3 is the license chosen by many packages in the
scientific python ecosystem, and by many packages we love (numpy, bokeh, scipy,
holoviews...) and (ii) because the "third clause" (non endorsement) seems
[appropriate](https://opensource.stackexchange.com/a/9137)
in the context of academic citations and publications. Indeed,
although we encourage people to use our model, we don't want our names to be
used to promote bad science (e.g. climate change denialists).

That's it! Not a big deal for many, but still important in my opinion. We hope
that you agree with these changes, and we hope that OGGM will continue to grow
in the future, regardless of which (open) license we are using!

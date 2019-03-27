---
layout: post
title: A (not so) realistic wishlist for the RGI
subtitle: Christmas is coming
author: Fabien Maussion
date: 2018-12-09T12:00:00
tags: science RGI programming
---

This is the annual [AGU week](https://fallmeeting.agu.org/2018/) and although
I'm nowhere near Washington I will participate to several meetings, one of
them about the state and future of the
[IACS Working group on the Randolph Glacier Inventory](http://www.cryosphericsciences.org/wg_randGlacierInv.html).

In the OGGM team, we are heavy users of the RGI, and I am very grateful for
these data. Since the first release in 2012, the RGI has been the basis of an
incalculable number of studies, some of them highly relevant for society and
the IPCC. Our friend and mentor [Graham Cogley](https://www.igsoc.org/news/grahamcogley/)
(1948–2018) was a tenant of this success.

## Status

The [RGI](https://www.glims.org/RGI/) is now at version 6 (released one and a
half years ago) and has significantly gained in maturity since the first release
nearly five years earlier. Its coverage is nearly global, the time frame covered
gets closer to its target of the 2000-2010 decade, and its attributes
(such as glacier or terminus type, hypsometry) are getting more accurate and
complete.

So, what now? Is the project "finished", and can the community move on?

I hope it isn't, and although I have only been involved in the recent phase of
the project, I think I am sufficiently familiar with the product to formulate
a non-exhaustive, and only sometimes realistic list of wishes for future
versions of the RGI. I am aware of the challenges behind each of these points,
this is why they are called "wishes" and not  "requests".

### 1. Glacier divides

In theory, glacier outlines in the RGI delineate a single "dynamical entity",
mostly defined by a connected ice flow from bottom to top (very similar to
a hydrological "catchment basin", i.e. all ice in a catchment would end up a
the glacier tongue it it wasn't melting on the way). In practice, the
*majority* of the RGI glaciers are divided this way, i.e. in "pieces of cake"
as I like to call them. See for example this glacier complex (an "ice cap")
in Iceland:

<img src="/img/blog/rgi_wish/iceland.png" alt="" width="70%" align="center"/>

However, there are notable exceptions to this rule.
A prominent example is glacier ``'RGI60-05.10315'`` an ice-cap in north-east
Greenland and also the largest RGI entity (by far) with 7537 km$^2$:

 <img src="https://rgitools.readthedocs.io/en/latest/_images/RGI60-05.10315.png" alt="" width="70%" align="center"/>

Other examples include the Hintereisferner and Vernagtferner in the Austrian
Alps which should actually be divided into several entities but aren't because
they used to be a single glacier some decades ago:

<p>
<img src="https://rgitools.readthedocs.io/en/latest/_images/RGI60-11.00897.png" alt="" width="52%" align="left"/>
<img src="https://rgitools.readthedocs.io/en/latest/_images/RGI60-11.00719.png" alt="" width="46%"/>
</p>

This seems trivial at first, but it is a real problem for (i) volume estimates
based on scaling relationships and (ii) flowline modelling ad done by OGGM.
Together with topography, it is one of the major source of uncertainty coming
from the RGI alone.

Note that [some semi automated](https://www.cambridge.org/core/journals/journal-of-glaciology/article/new-semiautomatic-approach-for-dividing-glacier-complexes-into-individual-glaciers/A8213D5446F9D3EAE9BCC731A53DFA3E) methods exist (and we [have developed our own](https://github.com/OGGM/partitioning)).
Our big efforts so far only had limited success for reasons I won't extend here
(maybe in a later post, however).

Proper glacier divides are on the top on my wishlist since a long time,
and I hope that it will get better soon.


### 2. Derived (vector) products and metadata

Glacier divides are required for some applications, but others would required
the merged geometries. Tools like OGGM also need to know where glaciers have
boundaries with other glaciers, and to which. Therefore, we developed
[rgitools](https://rgitools.readthedocs.io/en/latest/) to do exactly this.

For example, here is what our tool provides once run on a region of Iceland:

<img src="https://rgitools.readthedocs.io/en/latest/_images/plot_intersects.png" alt="" width="100%"/>

We call these "intersects", and I believe they would be useful to others as
well. Based on these, one can merge the glacier features back to the total
ice mass (useful for distributed modelling):

<img src="https://rgitools.readthedocs.io/en/latest/_images/plot_merged.png" alt="" width="100%"/>

Note that we have been able to compute these, but I think that it would be
very valuable (and more consistent) to ship them in parallel to the RGI.

### 3. Topography maps

Since Version 4.0, the RGI comes with hypsometric statistics for nearly all
glaciers. These were computed by Matthias Huss, who did a tremendous job
at gathering and merging various DEM sources. It would be great if the
raw data (i.e. individual topographic maps) would also *officially*
ship with the RGI
for consolidated boundary conditions across modelling experiments.

Here again, the data is there, but not (yet) available. Note that these data
will be available soon as a side product of
[G2TI](http://people.ee.ethz.ch/~danielfa/IACS/G2TI.html), but I
think that this should be part of the RGI production process.

Also, I wish there would be a globally available, consistent DEM of the
surface of the Earth, but I've [learned](https://rgitools.readthedocs.io/en/latest/dems.html)
that this is way harder tan  I thought it would be.


### 4. A more transparent release process

As a user of the RGI more than a contributor, I was informed about each RGI
release when it came out. I believe that a more transparent release process
borrowed from software development practices (i.e. "beta releases") would
help to avoid simple but annoying mistakes like listed
[here](https://rgitools.readthedocs.io/en/latest/known-issues.html).

It would also allow to prepare the attributes listed above in parallel to the
release process.

### 5. More traceable RGI ids

The RGI identifiers (ids) are unique for each version but are not guaranteed
to remain the same across versions (for several reasons not explained here).

For these glaciers which didn't change from one version to another, it would
be great to have a "link table" from one version to another. This would
help a lot with the problem of
[links between other glacier databases](https://oggm.org/2017/02/19/wgms-rgi-links/)
as well.

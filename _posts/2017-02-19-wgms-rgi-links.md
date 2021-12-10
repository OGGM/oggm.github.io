---
layout: post
title: A new WGMS to RGI lookup table
subtitle: The non-trivial problem of finding reference data for global glacier models
author: Fabien Maussion
date: 2017-02-19T09:00:00
tags: RGI science
---

The latest release of the *World Glacier Monitoring Service* (WGMS) *Fluctuations
Of Glaciers* (FoG) database ([WGMS, 2016](http://wgms.ch/data_databaseversions/))
ships with a new lookup table,
linking the glaciers in the WGMS database to those in the
Randolph Glacier Inventory ([RGI](http://www.glims.org/RGI/), Version 5).

## The problem

Let's provide a little bit of context before going on.
The RGI is the first
and, as of today, the only global inventory of glacier outlines
available[^1].
WGMS-FoG is the reference database for surface mass-balance observations[^2].
Each year, various institutes around the globe send their data to the WGMS,
which centralizes and publishes them.


[^1]: The [GLIMS](https://nsidc.org/glims/) database is centralized and
      just reached global completeness. it will provide a good alternative to
      the RGI in the near future.

[^2]: I also mention the [GMBAL](http://people.trentu.ca/~gcogley/glaciology/glglmbal.htm#Top)
      database provided by Graham Cogley, which is - as far as I know - largely
      merged in the WGMS.

So far, so good. Glacier modelers can use the RGI to initialise their
model simulations, and perhaps use the WGMS mass-balance data to calibrate and
validate their mass-balance model. At least this is how our
[homegrown model](http://oggm.org) does it.

**The problem is that both databases
are unaware of each other.**  The
reasons for this discrepancy are sometimes obvious, sometimes not:

- most WGMS identifiers pre-date the RGI (which was first published in 2012).
  Indeed, the RGI identifiers have to be attributed automatically
  to each of the 212,136 inventorized glaciers worldwide
- in several cases, the WGMS entries were outdated (inaccurate lon/lat
  coordinates due to glacier shrinkage, missing decimals,
  or simple reporting problems)
- the researchers working on the field might have a different definition of
  "their" glacier than the one provided by the RGI (i.e. geometry, location
  of the ice divides, etc.)
- sometimes, the apparently simple definition of "glacier entity" is
  problematic. While the
  RGI intends to provide a *snapshot* of glacier outlines at a certain date,
  the WGMS can store glacier data over several decades. During that time,
  a large glacier complex might break up in several tributaries which have
  no dynamical connection any more

With these issues in mind, the "RGI working group on linkage between databases"[^3]
started to work on this problem a couple of years ago, and the list was finalized
by the WGMS in 2016. I summarize here the results of this collaborative effort.

[^3]: Valentina Radić and Rachel Lo (University of British Columbia) provided a
      first list, which was then complemented by Graham Cogley (Trent University),
      who published it on the RGI website. In 2016, Ben Marzeion
      (Universty of Bremen) hired Johannes Landmann (University of Innsbruck)
      to formalise and automatize the process under my supervision.
      The results of his work can be found on this
      [github repository](https://github.com/OGGM/databases-links). Johannes
      then moved to Zürich and finalized this work: the WGMS published the
      first list in August 2016. The original list needed several corrections,
      but the final list was sent to us again in early 2017.

## The links

*Note: the code used to make these analyses is available*
[here](https://github.com/OGGM/oggm/blob/master/docs/notebooks/wgms_refmbdata.ipynb)

The lookup table contains 4,331 links between the various databases (WGMS, WGI,
GLIMS, and RGI), and 2,959 with the RGI alone. Most of them have been created
automatically by intersecting the WGMS lon/lat coordinates
with the RGI V5 polygons. Several mass-balance glaciers have then been checked
manually and led to a correction in the original WGMS entry.

The WGMS database has 427 glaciers with mass-balance data, out of which 283
glaciers have more than 5 years of mass-balance[^4].
However, not all of them are directly usable. There are some duplicates,
such as the Careser glaciers (which
[broke up](https://glacierchange.wordpress.com/2012/04/08/careser-glacier-breaking-up-italy/)
around 2009 and now have distinct WGMS identifiers - but only one RGI polygon).
**Finally, this leaves us with 263 glaciers linked between the WGMS and the
RGI**[^5].

[^4]: Five years of data is an arbitrary threshold we chose to use to determine
      which glaciers should be considered for validation

[^5]: removing the duplicates leaves us with 16 glaciers which have yet to be
      linked. The problem here is that there are strong discrepancies between
      the RGI and the WGMS, and that the RGI outlines are partly missing

These 263 glaciers have very different mass-balance record lengths:

  <figure>
      <a href="/img/blog/wgms-links/nglacier-hist.jpg" >
      <img src="/img/blog/wgms-links/nglacier-hist.jpg" alt="missing" width="80%" />
      </a>
  </figure>

The majority of glaciers (201) have less than 30 years of data. The longest
timeseries are found in Europe, North-America, and the ex-USSR:

  <figure>
      <a href="/img/blog/wgms-links/glacier-map.jpg" >
      <img src="/img/blog/wgms-links/glacier-map.jpg" alt="missing" width="100%" />
      </a>
  </figure>

According to the RGI classification, most of these data are obtained on
land-terminating ("valley") glaciers. 28 records are from ice-caps,
and 8 of the records are from marine-terminating glaciers.

## Observational bias

These numbers have to be compared to the 212,136 glaciers worldwide.
While the map above seems to show that there are observations almost everywhere
where glaciers are found on the globe, there is in fact a significant regional
bias:

  <figure>
      <a href="/img/blog/wgms-links/barplot-ng.jpg" >
      <img src="/img/blog/wgms-links/barplot-ng.jpg" alt="missing" width="100%" />
      </a>
  </figure>

With almost 60 glaciers, the European Alps are overrepresented in comparison
to Asia or Antarctica. This bias becomes *much* stronger if you take into
account the different glaciated areas between the RGI regions:

  <figure>
      <a href="/img/blog/wgms-links/barplot-perice.jpg" >
      <img src="/img/blog/wgms-links/barplot-perice.jpg" alt="missing" width="100%" />
      </a>
  </figure>

The last graph shows that many regions (especially at high latitudes) have
comparatively far less observations than European locations.

## Data availability

The data is available from the [WGMS](http://wgms.ch/data_databaseversions/)
and the [RGI](http://www.glims.org/RGI/) websites. The filtered lookup table used
by OGGM and the corresponding mass-balance time series can be found on our
dedicated [repository](https://github.com/OGGM/oggm-sample-data/tree/master/wgms)
(if you use the later link, please refer to the WGMS and RGI as official providers
of the data).

#### Notes

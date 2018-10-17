---
layout: page
title: "Topics for the Innsbruck & Bremen Oct 2018 code sprint"
description: "For inspiration only!"
header-img: "img/backgrounds/blue_ice.jpg"
---

The theme of the day is: "do what you want!"

But just in case you need some inspiration, here is a list of topics that
could definitely need some attention from one or two sprinters ;-)

I strongly recommend to spend your time on something you would *not* do on a
regular work day! "Business as usual" would be kind of missing the point of
a sprint: the idea is to learn something new and make a (big) step forward
in a direction interesting to you.

## Topics related to OGGM

Even if you are not an OGGM user or a glaciologist, OGGM can need your help!

### OGGM interactive graphics

Currently we use matplotlib to plot the model output and some intermediate
processing steps. More modern tools like [HoloViews](http://holoviews.org/)
allow a much more interactive and dynamic plotting, which would allow to
access and understand data faster and better.

This topic can be addressed by many sprinters at once, since there is a lot to
do!

Related Github issue: [https://github.com/OGGM/oggm/issues/547](https://github.com/OGGM/oggm/issues/547)

### Bringing HCL colors to OGGM

With the release of [python-colorspace](https://python-colorspace.readthedocs.io),
we now have a way to use expertly created colormaps in OGGM.
We should replace the existing colors (which are meh) with nice ones!

Related Github issue: [https://github.com/OGGM/oggm/issues/548](https://github.com/OGGM/oggm/issues/548)

### Make flowline glaciers less ugly

Related Github issue: [https://github.com/OGGM/oggm/issues/553](https://github.com/OGGM/oggm/issues/553)

### OGGM Edu - educational

[OGGM-Edu](https://github.com/OGGM/oggm-edu) is a repository of jupyter
notebooks (and soon: also a website) targeting students at all levels (from
school to university). Currently it is only for advanced users, but the idea
is to develop the platform further in order to reach this goal!

The vision is to build an educational platform around three main pillars:
- a website, where we can explain the concepts and link readers to the right
  tutorial for them
- dashboards, i.e. interactive websites where users can click, see and learn.
  This is useful for non-programmers. For example: [https://dash.klima.uni-bremen.de/](https://dash.klima.uni-bremen.de/)
- jupyter notebooks, that you can run on your laptop OR directly online, thus
  avoiding a painful installation (on mybinder, see the proof of concept:
  [https://mybinder.org/v2/gh/OGGM/oggm-edu/master](https://mybinder.org/v2/gh/OGGM/oggm-edu/master))

There is a lot of work to here for sprinters as well. See the github issues:
[https://github.com/OGGM/oggm-edu/issues](https://github.com/OGGM/oggm-edu/issues)


### OGGM Documentation

We are in the last weeks before submitting a revised version of the
[OGGM paper](https://www.geosci-model-dev-discuss.net/gmd-2018-9/) and an associated OGGM version 1.1. Before this major release
I would like to polish the docs to make them easier to follow and more attractive
for new users.

See the [DOC github issues](https://github.com/OGGM/oggm/issues?q=is%3Aissue+is%3Aopen+label%3Adocs)
for some ideas about how to improve the docs.

### OGGM 3000

OGGM is a project in constant development. Along more involved developments,
some issues might be addressed (or at least started) in one day.

**Play with the SIA2D (distributed) model** (this is more "for fun" since the model is not
used operationally yet): [Github issues](https://github.com/OGGM/oggm/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+SIA2D)

**Read GCM data**: add [more datasets](https://github.com/OGGM/oggm/issues/469) to the OGGM workflow (e.g. CMIP5)

**add support for the new DLR Global DEM**: [GitHub issue](https://github.com/OGGM/oggm/issues/556)

**Your idea?**

## Topics NOT related to OGGM


- Convert a [mountain wave app](http://moe.met.fsu.edu/~rhart/mtnwave.html)
  from Matlab to Python and make it pretty!
- **Any issue you would like to contribute to**! What is your favorite package?  

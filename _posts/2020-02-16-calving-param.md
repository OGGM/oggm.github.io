---
layout: post
title: A "new" calving parameterization in OGGM
subtitle: It's only the beginning...
author: Fabien Maussion
date: 2020-02-16T00:00:00
tags: science model
---

I always thought that it would be very hard to get the
[Oerlemans & Nick (2005)](https://www.cambridge.org/core/journals/annals-of-glaciology/article/minimal-model-of-a-tidewater-glacier/C6B72F547D8C44CDAAAD337E1F2FC97F)
parameterization in OGGM's flowline model. As it turns out, getting *something* to work was not so hard after all.
This is very much a work in progress, but it should
get the ball rolling for more advanced treatment of frontal ablation
with OGGM in the future (stay tuned!).

<figure>
    <a href="/img/blog/calving_param/calving_ex.png" >
    <img src="/img/blog/calving_param/calving_ex.png" alt="Image missing" width="100%" />
    </a>
    <figcaption><i>Illustration of the Water-depth – calving-rate feedbacks.
    See the notebook linked below for more details.</i></figcaption>
</figure>

The new feature is documented in a Jupyter Notebook. You can read it rendered
<a href='{{ site.baseurl }}/img/blog/calving_param/kcalving_parameterization.html'>  on this page</a>,
or you can run the notebook yourself on [OGGM-Edu](https://edu.oggm.org/en/latest/oggm_tuto.html).

Many thanks to David Rounce who persevered in convincing me that it shouldn't be
"that hard to implement", and Lizz Ultee for her expertise and advice.

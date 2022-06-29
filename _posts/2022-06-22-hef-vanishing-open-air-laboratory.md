---
layout: post
title: Are we losing our Open Air laboratory?
subtitle: In 11 years, the famous Hintereisferner glacier will lose around 50% of its mass of 2020
author: Lilian Schuster
date: 2022-06-22T00:00:00
tags: edu outreach

---

# Are we losing our Open Air laboratory?

### In just 11 years, the famous Hintereisferner glacier will lose around 50% of its volume of 2020. 

Since many decades, the [Hintereisferner glacier](https://wgms.ch/products_ref_glaciers/hintereisferner-alps/) in the Ötztal Alps, Austria, is the key research site for glaciological studies of the [Department of Atmospheric and Cryospheric Sciences (ACINN) from the University of Innsbruck](https://www.uibk.ac.at/acinn/research/ice-and-climate/projects/hintereisferner). There exist [length measurements](https://www.wgms.ch/data/min-data-graphs/491_FV_cum.png) for around 150 years and [mass-balance measurements](https://www.wgms.ch/data/min-data-graphs/491_MB_ann.png) ([amount of mass a glacier gains and loses over a year](https://www.antarcticglaciers.org/glacier-processes/mass-balance/introduction-glacier-mass-balance/)) since 1953. There have been as well many local-scale projects on that glacier. For example, recently, a permanent terrestrial laser scanner was installed to identify snow (re)distribution [(Voordendag et al, 2021)](https://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/V-2-2021/153/2021/). 


**Below you can see a webcam image of the Hintereisferner on June 21, 2022:** 
<figure>
    <a href="https://www.foto-webcam.eu/webcam/hintereisferner1/2022/06/21/1330" >
    <img src="/img/blog/hef-vanishing-open-air-laboratory/hintereisferner1-220621-1330-hu.jpg" alt="Image missing" width="70%" />
    </a>
    <figcaption align = "center"><br><em>So far, this melt season 2022 started exceptionally: Hintereisferner has lost already in June most of its protecting snow cover. In the 4 preceeding years from where we have webcam images available, Hintereisferner always had much more snow left in June. Check it out yourself by clicking on the image and changing the years on the webcam webpage!</em></figcaption>
</figure>


 <br/> Although, the OGGM community here in Innsbruck works on large-scale glacier modelling, we still have a special relation to the Hintereisferner: Hintereisferner is often used as a [test glacier to check regularly our existing code](https://github.com/OGGM/oggm/blob/157c44b5b63c2a848ffb318afe77da4a18223a0d/oggm/tests/conftest.py#L266) and also when starting a new workflow, we use Hintereisferner as first test before repeating it on many other glaciers. In addition, many of us have contributed to mass-balance measurements on that glacier. [Here is a german article with some nice pictures from one of these measurement campaigns](http://bergspektiven.at/eisige-welten-gletscher-im-wandel/#jp-carousel-4449).
 
Over the last months, I recognized, that for Hintereisferner and many other reference glaciers with additional observational data, the model projects very fast melting rates in the near future. That means reference glaciers are almost or even completely lost in the year 2100. I am interested in comparing the influence of different mass-balance model choices on the projections, if the glaciers are gone, the differences are of course zero. After some discussions with [Dave](https://www.cmu.edu/cee/people/faculty/rounce.html), we thought about another measure, i.e. the year where half of a glaciers' volume is lost. When I computed that year, it was a bit shocking: 

> According to the model, in 2031, Hintereisferner loses 50% of its volume from 2020. In that 11 year time-period, the glacier is projected to lose every year around 5% of its glacier volume. 

On the next meeting with my supervisors, Fabien and Dave, I showed them the numbers and a similar plot as the one below:

<figure>
    <a href="/img/blog/hef-vanishing-open-air-laboratory/volume_projections_HEF_glacier_most_complex_easy.jpg" >
    <img src="/img/blog/hef-vanishing-open-air-laboratory/volume_projections_HEF_glacier_most_complex_easy.jpg" alt="Image missing" width="75%" />
    </a>
    <figcaption align = "center"><br><em>Relative volume change projections compared to 2020 for the Hintereisferner glacier, Ötztal Alps, Austria</em></figcaption>
</figure>


 <br/>Fabien was a bit sceptical: Are you sure that this is Hintereisferner?

Of course, the numbers had made me suspicious as well. And, yes, it is the Hintereisferner. To have more robust estimates, I repeated then my computations for 5 different climate projection models (i.e. [GCMs](https://en.wikipedia.org/wiki/General_circulation_model)) and for two [emission scenarios](https://www.dkrz.de/en/communication/climate-simulations/cmip6-en/the-ssp-scenarios) using the newest available data and model options (see the plot above). The low emission scenario (ssp126) corresponds to a global warming of around 1.8°C in 2100 and the high emission scenario (ssp585) to a global warming of around 4.8°C compared to preindustrial times ([click here](https://www.ipcc.ch/report/ar6/wg1/static/ad35aedbeee1cba2bfb73b440f1c295d/d3324/IPCC_AR6_WGI_SPM_Figure_8.png)). Volume changes similarly for the two emission scenarios, because Hintereisferner is reacting to past and near-future climate change which is independent of the emission scenario. For 4 out of the 5 GCMs, in 2031 or earlier, 50% of the volume is projected to be lost, while only for [1 GCM](https://www.isimip.org/gettingstarted/input-data-bias-adjustment/details/86/), half of the volume is just lost in year 2037. Because of this one outlier GCM, I preferred to show you the [median](https://en.wikipedia.org/wiki/Median) volume estimates. It shows more robustly the central tendency compared to using an average value. So, overall, the scenarios and GCMs agree very well on the near-term projections. And, unfortunately, I have not (yet) found any coding error! At least, if we reduce our emissions fast enough, some ice patches of Hintereisferner might be left until 2100. 

***What do you think: How much time is left until Hintereisferner gets too small to be used as Open Air Laboratory?*** 



--- 

##### For those interested in more methodological details:

For these estimates, I just used simple methods that could be applied to any glacier on the world. To model the mass-balance over the glacier, I use a variant from the default mass-balance model option that is currently under development in the [OGGM massbalance-sandbox](https://github.com/OGGM/massbalance-sandbox). That means, surface type distinction is included to distinguish between melt factors of ice and snow and I use variable temperature lapse rates  instead of a constant value. I use W5E5 [(Lange et al., 2019)](https://dataservices.gfz-potsdam.de/pik/showshort.php?id=escidoc:4855898) as past climate dataset and the 5 GCMS from the ISIMIP3b [(Lange & Büchner, 2021)](https://data.isimip.org/10.48364/ISIMIP.842396.1) projections for the future climate, both on a daily resolution. For the projections that I have shown you, I calibrated the glacier to match the geodetic observations of [Hugonnet et al. 2021](https://www.nature.com/articles/s41586-021-03436-z). The precipitation has been corrected by a precipitation factor that depends on the winter precipitation amount of that glacier. 

---

*This was just a side-story of my actual research: the influence of different mass-balance model and calibration options on glacier change projections for reference glaciers (Schuster et al., in preparation).* 

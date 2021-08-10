---
layout: post
title: Equilibrium runs with OGGM
subtitle: Comparison of methods
author: Fabien Maussion
date: 2021-08-10T00:00:00
tags: science model
---

Following ongoing discussions about the [GlacierMIP3](https://github.com/GlacierMIP/GlacierMIP3) experiment, I thought that it would be good to pursue the discussion started in a [previous blog post]({{ site.url }}/2021/08/05/mean-forcing/) with concrete examples with OGGM.

The objective of these simulations is to simulate glacier evolution under a "stable climate", say for example the climate of 2000-2021 (21 years). The assumption is that climate doesn't change anymore and keeps its properties (central value, variability). This is a purely theoretical scenario, since in reality climate always changes. It is highly improbable that statistical values such as the average and standard deviation of temperature do not change with time. However, these simulations have a high scientific and societal value, as explained in the GlacierMIP3 protocol.

The objective of this blog post is to explain how OGGM computes and uses the modelled glacier mass-balance, and why the design of these theoretical experiments matters. Although these examples are OGGM specific, I believe that some of these results are applicable to other models as well. 

## A few definitions

In OGGM, we have a separation between the **glacier geometry evolution model** and the **glacier mass-balance model**. 

The geometry evolution model needs to know the mass-balance profile of the glacier at regular time intervals and varying elevations along the glacier. **The default is to do a yearly update**: in practice, this means that the geometry evolution model knows the altitude area distribution of the glacier at year y0, asks the mass-balance model to compute the annual mass-balance for the upcoming year, and then computes the geometry evolution accordingly. At y1, with the new geometry, the mass-balance model is asked again to provide the new mass-balance, etc.

The fact that the geometry evolution model needs climate at annual time steps has no influence whatsoever on the time resolution of the mass-balance model. The mass-balance model can compute the mass-balance at hourly or annual time steps, as long as it provides the annual mass-balance to the geometry evolution model. In OGGM, **the current default is to compute mass-balance at monthly time steps**: for any given year, the monthly data is used to compute the 12 months of mass-balance, summed and provided to the geometry evolution model. The model used here is a monthly temperature index model as described in Marzeion et al., (2012) and Maussion et al., (2019).

## Forcing methods

I am going to illustrate three different forcing methods, meant to represent the theoretical equilibrium experiment that we wish to conduct. We keep the period 2000-2020 as an example.

**Method 1 (AvgClim)** uses averaging of the climate data first. In practice, we compute a monthly climatology of the temperature and precipitation time series. We then use the OGGM monthly mass-balance model to compute the mass-balance based on this monthly climatology. The mass-balance provided to the geometry evolution model is the same each year (it is only a function of elevation, not of time).

**Method 2 (AvgMB)** also uses averaging, but *after* the computation of the mass-balance. In practice, we compute the monthly mass-balance for the entire time period (2000-2020). We then average it to compute the monthly climatology of the mass-balance (not the climate), before summing it to annual and passing it to the geometry evolution model. Like for Method 1, the mass-balance provided to the geometry evolution model is the same each year (it is only a function of elevation, not of time).

**Method 3 (RdnMB)** uses a random number generator to create a synthetic time series of climate. Each given year is picked randomly from the (2000-2021) period. In this process, we are careful not to pick the same year twice within a 21 year period. Unlike method 1 and 2, the mass-balance provided to the geometry evolution model at a given height changes each year. 

## Example 1: Hintereisferner, reference period 2000-2020

Here is a plot showing the monthly specific mass-balance computed by the mass-balance model over a fixed glacier geometry using the three methods above:

<img src="/img/blog/equilibrium/monthly_mb_2020.png" alt="" width="100%"/>

The random climate randomly shifts between the grey lines, while the two other methods compute a time invariant mass-balance. The differences between Method 1 and Method 2 are small, but most visible in the transition periods, in the months where the temperature varies above and below the melt threshold.

The annual specific mass-balance averages are -1684, -1739, and -1739 mm w.e. yr$^{-1}$ for the three methods, respectively. Method 2 and 3 have the same average, per construction. The reason why Method 1 has not the same average is explained in the [previous blog post]({{ site.url }}/2021/08/05/mean-forcing/) and is due to the presence of non-linear equations in the mass-balance model.

Now, let's see what happens if we run the full model (glacier mass-balance + glacier evolution) for a period of 300 years using this three forcing scenarios:

<img src="/img/blog/equilibrium/volume_2020.png" alt="" width="100%"/>

So far so good! In the strongly retreating case, all forcing methods lead to very similar results. Now let's see what happens in a colder scenario.

## Example 2: Hintereisferner, reference period 1960-1980

In the 60s and 70s, Hintereisferner was close to balance and even had several positive years, leading to a positive average mass-balance over that period under the present day geometry.

Now let's have a look at the plots again:

<img src="/img/blog/equilibrium/monthly_mb_1980.png" alt="" width="100%"/>

The annual specific mass-balance averages are 303, 241, and 241 mm w.e. yr$^{-1}$ for the three methods, respectively. For the volume evolution, this implies:

<img src="/img/blog/equilibrium/volume_1980.png" alt="" width="100%"/>

That's quite a difference now. **Why does this matter?** In OGGM at least, the melting temperature threshold (the monthly temperature at which melt occurs) is a global parameter (set at -1°C per default). The more months we have where the temperature is oscillating around this threshold, the more likely it is that the average climate is actually below this threshold. This leads to non-linear effects, which are small in the grand scheme of things but become increasingly relevant in the equilibrium scenarios, where glaciers are slowly adapting to a theoretical, stable climate. In these theoretical scenarios, even a few mm w.e. matter a lot.

## Conclusions

In OGGM at least, only Methods 2 and 3 are viable options to represent the climate of a given period (although we agree that this is a theoretical experiment). This is even more relevant when considering the calibration to geodetic estimates, where only Methods 2 and 3 will guarantee consistency.

It must be noted that more advanced models using internal representations of daily variability *might* be less sensitive than OGGM to such choices. This is standard practice in GloGEM and PyGEM, but not yet in OGGM. The new generation of mass-balance models ([massbalance-sandbox](https://github.com/OGGM/massbalance-sandbox) developed by Lilian Schuster) now offer such models to our users. We will run these simulations in due time and update this blog post when available.

## Code & Data

The code used to create these plots is available [here](https://gist.github.com/fmaussion/3acc65ea9119dcf90fcb957c05f2977d).

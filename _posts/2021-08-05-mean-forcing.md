---
layout: post
title: Impact models and averages of forcing data
subtitle: A recommendation
author: Anouk Vlug, Lilian Schuster, Fabien Maussion
date: 2021-08-05T00:00:00
tags: science model
---

A very typical situation in geosciences is that a numerical model (here called "impact model") is driven by forcing data (often: reanalysis data or climate model output). There are many impact models around: hydrological models and glacier models are obvious ones.

## Take home message

This blog post has one simple message to convey:

####  **Do not average the forcing data before giving it to the impact model.** 

*(unless you know what you are doing and your model is calibrated that way)*

## A simple demonstration

Let $M$ be the non-linear impact model, and $X$ the forcing data variables (temperature, precipitation, etc.). Therefore, $M(X)$ is the output of the impact model.

Now let $\overline{X}$ be the average of the variable $X$ (either a temporal average, a climatology over 30 years, or the average of several ensemble members). Accordingly, $\overline{M(X)}$ is the average of the model output after being forced by the non-averaged $X$ (this is the *true* average value of the quantity we are interested in).

Then, it is easy to show that if $M$ is a non-linear impact model (like most models), the following model results are NOT equivalent:

$\overline{M(X)} \neq M(\overline{X})$


## A simple example (degree day model)

In the very famous degree day melt model, the daily melt $m$ is computed as:

$ M = \mu T \text{ if } T\geq 0 \text{, and }  M = 0 \text{ otherwise}$

with $\mu$ a calibrated melt factor (let's assume it is $\mu = 1$ here). 

Then, lets say we want to compute the melt on Oct. 1 of five consecutive years. For four years, the temperature was -2°C, then on the fifth it was 5°C. Then, $\overline{M(X)} = 5 / 5 = 1$. However, $M(\overline{X}) = M(-3 / 5) = 0$, i.e.: not the same.

*Note: from the example above, it may seem that monthly degree days models are not possible. While monthly degree days models need tweaks, they are possible: either by changing the temperature thresholds, or by using the standard deviation of temperature as proxy for variability. The problem in our example above is that $M$ has been calibrated with a certain data: after calibration, this data should NOT be averaged further.*

## A concrete example: ensemble average

If you want more information about why we write this down today, here is what Anouk Vlug found out the hard way during her PhD thesis:

I have been amazed by the impact that climate variability had in my glacier simulations, to the extent that I wondered “what can go so wrong?”
Here is an illustration:

<img src="/img/blog/forcing/anouk.png" alt="" width="100%"/>

The experiment includes most of the land-terminating glaciers in the Canadian Arctic. For the glacier simulations, OGGM was forced with the 13 fully forced ensemble members from the Community Earth System Model Last Millennium Ensemble (CESM-LME) individually at first, and then with the ensemble mean. In the figure you can see that this leads to a very different evolution of the glacier volume in the region. The simulation that was forced with the ensemble mean is very different from the mean of the ensemble, and lies far outside the spread of the simulations that were forced with the individual ensemble members.

So, why does this happen? It is because of the effect of the averaging illustrated above. When the ensemble members are averaged, this strongly reduces the temperature variability. So much, in fact, that much fewer years in the averaged timeseries lead to glacier melt, and therefore the glaciers are now growing instead of shrinking!

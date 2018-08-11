---
layout: post
title: Mass-balance model calibration for the Alps
subtitle: Regional parameters derived with HISTALP climate
author: Matthias Dusch
date: 2018-08-10T00:00:00
tags: alps histalp calibration
---

In this post we will update the OGGM mass balance (MB) parameter values to be used for
Alpine model runs with HISTALP[^1] baseline climate data.

## Background

To calculate the monthly MB along the elevation range of an
individual glacier we need several parameters in OGGM:
A precipitation scaling factor ($$p_f$$),
a melt temperature ($$T_{Melt}$$),
a liquid precipitation temperature ($$T_{Liquid}$$)
and the temperature laps rate ($$\Gamma$$).
A more detailed description of these parameters and how
they are used can be found in Chapter 3.3 of
[Maussion et al. (2018)](https://www.geosci-model-dev-discuss.net/gmd-2018-9/)
and also in the
[OGGM documentation](https://oggm.readthedocs.io/en/latest/mass-balance.html).  

For these parameters we provide default values which were determined with
a cross-validation for our 254 global reference glaciers.
This cross-validation is done with CRU[^2] data and the default values we
obtain are:
$$p_f = $$ 2.5,
$$T_{Melt} = $$ -1.0$$^{°}$$C,
$$T_{Liquid} = $$ 2.0$$^{°}$$C and
$$\Gamma = $$ -6.5 K km$$^{-1}$$.

For regional runs it might be better to use regional parameters, and
this is especially true if other baseline climate data is used.

For runs in the European Alps, the HISTALP dataset can be used to replace
CRU: it has a higher resolution (although unpublished experiments show that
this doesn't necessarily improve the modelled MB much), and more importantly
goes further back in time (up to 1801 for precipitation).


## Cross-validation of Alpine reference glaciers

The leave-one-out cross-validation can be performed for 41 glaciers in the
Alps. For these glaciers we have at least 5 years of MB measurements
within the timespan of the HISTALP data.
To test different parameters we systematically change one parameter at a time
over a subjectively chosen range. This results in 1215 different parameter
combinations.

The following 4 figures show different quality measures (RMSE[^3], bias[^4],
quotient of the standard deviations[^5] and correlation coefficient[^6]).
Each figure is arranged with respect to one of the 4 MB parameters.
In these figures each data point represents the mean quality measure
for the 41 glaciers of one of the 1215 parameter combinations.
For more visual clarity data points with the same MB parameter in the
individual figures are unified in a standard box-whisker plot.  
The parameter combination where all but the one parameter in question are set to
the global default values are indicated with a red dot.
The parameter combination which we propose to be used with the HISTALP climate
data is indicated with a blue dot and also a grey vertical line.
Grey horizontal lines show the optimal quality measures.


<a href="/img/blog/histalp-parameters/prcpsf_crossval_box_neu.png"><img src="/img/blog/histalp-parameters/prcpsf_crossval_box_neu.png" alt="Image missing" width="100%" /></a>
<a href="/img/blog/histalp-parameters/tmelt_crossval_box_neu.png"><img src="/img/blog/histalp-parameters/tmelt_crossval_box_neu.png" alt="Image missing" width="100%" /></a>
<a href="/img/blog/histalp-parameters/tliq_crossval_box_neu.png"><img src="/img/blog/histalp-parameters/tliq_crossval_box_neu.png" alt="Image missing" width="100%" /></a>
<a href="/img/blog/histalp-parameters/tgrad_crossval_box_neu.png"><img src="/img/blog/histalp-parameters/tgrad_crossval_box_neu.png" alt="Image missing" width="100%" /></a>


## Proposed parameters to be used with HISTALP data

The proposed default parameters to be used with HISTALP climate data for Alpine
wide runs are:

$$p_f = $$ 1.75  
$$T_{Melt} = $$ -1.75$$^{°}$$C  
$$T_{Liquid} = $$ 2.0$$^{°}$$C  
$$\Gamma = $$ -6.5 K km$$^{-1}$$


## Mass balance cross-validation tool

The code used to perform the cross-validations can be found
[here.](https://github.com/OGGM/mb_crossval)

### Footnotes
[^1]: [ZAMG Histalp](http://www.zamg.ac.at/histalp/)
[^2]: [Climatic Research Unit](http://www.cru.uea.ac.uk/)
[^3]: root mean square error between measured annual mass balance and modeled mass balance.
[^4]: mean difference between measured and modeled mass balance.
[^5]: mean of the modeled mass balance standard deviation divided by the measured mass balance standard deviation.
[^6]: correlation coefficient between measured and modeled mass balance.

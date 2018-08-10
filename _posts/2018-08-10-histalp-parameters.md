---
layout: post
title: OGGM parameters for the Alps
subtitle: Regional mass balance parameters derived with HISTALP climate
author: Matthias Dusch
date: 2018-08-10T00:00:00
tags: model alps histalp parameters
---

In this post we will propose OGGM mass balance parameter values to be used for
Alpine model runs with HISTALP[^1] climate data.

## Global mass balance parameters

To calculate the monthly mass balance along the elevation range of an
individual glacier we need several parameters in OGGM:
A precipitation scaling factor ($$p_f$$),
a melt temperature ($$T_{Melt}$$),
a liquid precipitation temperature ($$T_{Liquid}$$)
and the temperature laps rate ($$\Gamma$$).
A more detailed description of these parameters and how
they are used can be found in Chapter 3.3 of
[Maussion et al. (2018)](https://www.geosci-model-dev-discuss.net/gmd-2018-9/)
and also within the
[OGGM documentation](https://oggm.readthedocs.io/en/latest/mass-balance.html).  
For these parameters we provide and mostly use default values which were found
through mass balance cross-validation for our 254 global reference glaciers.
This cross-validations is done with CRU[^2] data and the default values we
obtain are:
$$p_f = $$ 2.5,
$$T_{Melt} = $$ -1.0$$^{°}$$C,
$$T_{Liquid} = $$ 2.0$$^{°}$$C and
$$\Gamma = $$ -6.5 K km$$^{-1}$$.

For regional runs it might be better to use regional parameters and
this is especially true if other climate data is used.
For runs in the Alps the HISTALP dataset can be used.


## Cross-validation of Alpine reference glaciers

The leave-one-out cross-validation can be performed for 41 glaciers in the
Alps. For these glaciers we have at least 5 years of mass balance measurements
within the timespan of the HISTALP data.
To test different parameters we systematically change one parameter at a time
over a subjectively chosen range. This results in 1215 different parameter
combinations.

The following 4 figures show different quality measures (RMSE[^3], bias[^4],
quotient of the standard deviations[^5] and correlation coefficient[^6]).
Each figure is arranged with respect to one of the 4 mass balance parameters.
In these figures each data point represents the mean quality measure
for the 41 glaciers of one of the 1215 parameter combinations.
For more visual clarity data points with the same mass balance parameter in the
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

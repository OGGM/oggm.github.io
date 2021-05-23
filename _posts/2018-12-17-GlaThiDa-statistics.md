---
layout: post
title: An overview of the Glacier Thickness Database
subtitle: Some statistics and interactive plots
author: Matteo Castellani
date: 2019-03-21T00:00:00
tags: science glacier thickness RGI
---

# GlaThiDa analysis

The <a href="https://www.gtn-g.ch/data_catalogue_glathida/">GlaThiDa 2.0</a> (GLAcier THIckness DAtabase) is a collection of thickness measurements from glaciers all over the world. Different research groups used different techniques in collecting these measurements over several years.
This database is potentially an amazing tool for glacier research and it could be particularly useful for the validation of models like OGGM.<br>
This analysis breaks down the structure of this database and the statistics about the surveyed glaciers, to give its users a fast overview over the entire data-set.

### Database Structure
There are 820370 entries (thickness measurements) in the GlaThiDa all associated to GPS coordinates. Some of them have a glacier name associated with but many don't. It is therefore important to point each observation to its respective glacier. To do so we used the [Randolph Glacier Inventory 6.0](https://www.glims.org/RGI/) (RGI) associating each measurement from the GlaThiDa to a glacier in the RGI if its GPS coordinates were lying inside a glacier outlines. The result is that **771** glaciers have thickness measurements in the GlaThiDa. Out of the 820370 initial entries 27882, 3.4% resulted outside of any glacier outlines defined in the RGI. Some reason for this could be: a slightly wrong GPS coordinate collected in the GlaThiDa measurement; observations taken outside of the glacier by mistake or intentionally, to make sure that all the glacier was covered; a different shape of the glacier at the moment when the observation was taken, compared to the moment when the RGI was compiled; a wrong assessment of the glacier shape in the RGI.
### GlaThiDa glaciers distribution and types
The map below shows the spacial distribution of the glaciers with at least one GlaThiDa entry.
<iframe src="/img/blog/glathida_analysis/glathida_map.html" sandbox="allow-same-origin allow-scripts" width="100%" height="500" scrolling="no" seamless="seamless" frameborder="0"> </iframe>

Code and Data: [GitHub](https://github.com/MatCast/GlaThiDa-RGI)

Most of the glaciers with thickness observation are in the Greenland Periphery region and in the Artic Canada North region. If we compare the glaciers with measurements with the number of glaciers present in each specific region though, we see that Arctic Canada North is the best represented region with around 5% of the glaciers having at least one thickness measurement point. The region with most glaciers, Central Asia, has a very low number of glaciers represented in the GlaThiDa database. This is probably due to the difficulty in getting measurements for glaciers as such high altitudes at those present in the Himalaya.
<iframe src="/img/blog/glathida_analysis/glathida_reg_hist.html" sandbox="allow-same-origin allow-scripts" width="100%" height="430" scrolling="no" seamless="seamless" frameborder="0"> </iframe>

Code and Data: [GitHub](https://github.com/MatCast/GlaThiDa-RGI)

More than two third of the RGI entities with GlaThiDa measurements are glaciers  while the rest are ice caps. Land terminating glaciers and ice caps are the vast majority.

<iframe src="/img/blog/glathida_analysis/glathida_types.html" sandbox="allow-same-origin allow-scripts" width="100%" height="400" scrolling="no" seamless="seamless" frameborder="0"> </iframe>

Code and Data: [GitHub](https://github.com/MatCast/GlaThiDa-RGI)

### Measurements Distribution per Glacier
Unfortunately not all the glaciers with measurements are perfectly covered over the whole glacier area. In fact around 42% of the glaciers have less than 100 thickness observations. Given that some glaciers can extend for over 100 km², it's clear that some of them are very poorly covered.

<iframe src="/img/blog/glathida_analysis/glathida_pts_area.html" sandbox="allow-same-origin allow-scripts" width="100%" height="400" scrolling="no" seamless="seamless" frameborder="0"> </iframe>

Code and Data: [GitHub](https://github.com/MatCast/GlaThiDa-RGI)

More than 91% of all the glaciers (represented in the figure above) have less than 100 thickness measurements per squared kilometer.
Almost 44% of all the glaciers with thickness observations have less than 5 observations per squared kilometer.

We can use OGGM to generate a gridded map of each glacier represented in the GlaThiDa. With this map we can divide each glacier in 100m altitude bands to check how many of those bands contain at least one thickness measurement.

<iframe src="/img/blog/glathida_analysis/glathida_bands.html" sandbox="allow-same-origin allow-scripts" width="100%" height="400" scrolling="no" seamless="seamless" frameborder="0"> </iframe>

Code and Data: [GitHub](https://github.com/MatCast/GlaThiDa-RGI)

Almost half of the glaciers have observations in at least half of the 100m altitude bands. Glaciers with few observations but well distributed over their length can be very useful for understanding glacier thickness patterns and for model validation.


### Survey Year
Finally it is important to look at the distribution of the survey year, i.e the year when the thickness measurement campaign was led for each glacier.

<iframe src="/img/blog/glathida_analysis/glathida_years.html" sandbox="allow-same-origin allow-scripts" width="100%" height="400" scrolling="no" seamless="seamless" frameborder="0"> </iframe>

Code and Data: [GitHub](https://github.com/MatCast/GlaThiDa-RGI)

Measurements were taken between 1977 and 2015, but most of them after 2005. The spread in the dates of the campaign could potentially create problems when trying to compare glaciers with each other to find similar patterns, but also when using the data for model validation. <br>
Most glacier models make in fact use of digital elevation models to setup the model run. Any digital elevation model is compiled with data available at the time of its construction. The time difference between the date of data assimilation for the digital elevation model, and the date of the survey for the thickness observation, could be in the order of several years. This would create an error when validating the model.

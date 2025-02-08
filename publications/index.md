---
layout: page
title: "Publications"
description: "Publications related to OGGM"
---

### Publications making use of the OGGM model

{% assign publications = site.data.publications %}

{% assign total_count = 0 %}
{% for category in publications %}
  {% assign count = category.entries | size %}
  {% assign total_count = total_count | plus: count %}
{% endfor %}

Currently, there are {{ total_count }} entries. We are not aware of all of them! [Click here](https://github.com/OGGM/oggm.github.io/issues/248){:target="_blank"} if you’d like to add your own.

{% for category in publications %}
**{{ category.category }}** <small>({{ category.entries | size }} entries)</small>
{% assign sorted_entries = category.entries | sort: "authors" %}
{% for entry in sorted_entries -%}
- <small>{{ entry.authors }}: <strong>{{ entry.title }}</strong>, {{ entry.journal }}, <a href="https://doi.org/{{ entry.doi }}" target="_blank">doi:{{ entry.doi }}</a>, {{ entry.year }}.</small>
{% endfor %}
{% endfor %}

### Related publications (selection)

- <small> Marzeion, B., Kaser, G., Maussion, F., and Champollion, N.: **Limited influence of climate change mitigation on short-term glacier mass loss**, Nature Climate Change, [doi:10.1038/s41558-018-0093-1](https://doi.org/10.1038/s41558-018-0093-1), 2018.</small>
- <small> Marzeion, B., Cogley, J.G., Richter, K., and Parkes, D.: **Attribution of global glacier mass loss to anthropogenic and natural causes**, Science, 345, 919-921, [doi:10.1126/science.1254702](https://doi.org/10.1126/science.1254702), 2014.</small>
- <small> Marzeion, B., Jarosch, A. H., and Hofer, M.: **Past and future sea-level change from the surface mass balance of glaciers**, The Cryosphere, 6, 1295-1322, [doi:10.5194/tc-6-1295-2012](https://doi.org/10.5194/tc-6-1295-2012), 2012.</small>

### Theses making use of OGGM

(that we are aware of)

**PhD**

- <small> Eis, J., **Reconstructing glacier evolution using a flowline model**, [doi:10.26092/elib/432](http://dx.doi.org/10.26092/elib/432), 2020.</small>
- <small> van der Laan, L., **Near-Term Global Glacier Mass Balance Modelling**, [doi:10.15488/14171](https://doi.org/10.15488/14171), 2023.</small>
- <small> Malles, J., **Past to Future and Land to Sea: constraining global glacier models by observations and exploring ice-ocean interactions**, [doi:10.26092/elib/2323](http://dx.doi.org/10.26092/elib/2323), 2023.</small>
- <small> Recinos, B., **Ocean-glacier interaction on the large regional scale**, [doi:10.26092/elib/434](http://dx.doi.org/10.26092/elib/434), 2020.</small>
- <small> Vlug, A., **The influence of climate variability on the mass balance of Canadian Arctic land-terminating glaciers, in simulations of the last millennium**, [doi:10.26092/elib/1501](http://dx.doi.org/10.26092/elib/1501), 2021.</small>
- <small> Pelto, B., **An approach to remotely monitor glacier mass balance at seasonal to annual time scales, Columbia and Rocky Mountains, Canada**, [doi:10.24124/2020/59097](http://doi.org/10.24124/2020/59097), 2020.</small>

**Master**
- <small> Chizzola, R. **Influence of the future changes of the Atlantic Meridional Overturning Circulation on North Atlantic Glaciers**, [link](https://diglib.uibk.ac.at/ulbtirolhs/content/titleinfo/9648318), 2024.</small>
- <small> Holmgren, E. **21<sup>st</sup> century glacier runoff and how it buffers drought in 75 large-scale basins**, [link](https://diglib.uibk.ac.at/ulbtirolhs/content/titleinfo/7754587), 2022.</small>
- <small> Oberrauch, M. **Testing the importance of explicit glacier dynamics for mountain glacier change projections**, [link](https://diglib.uibk.ac.at/ulbtirolhs/content/titleinfo/5878449), 2021.</small>
- <small> Schmitt, P., **Flowline glacier bed estimation with numerical modelling and cost minimization: Extending the open source model COMBINE 1D**, [link](https://diglib.uibk.ac.at/ulbtirolhs/content/titleinfo/6139027), 2021.</small>
- <small> Castellani, M. **Estimating Glacier Ice Thickness with Machine Learning**, [link](https://diglib.uibk.ac.at/urn:nbn:at:at-ubi:1-60115), 2020.</small>
- <small> Schuster, L., **Response time sensitivity of glaciers using the Open Global Glacier Model**, [link](https://diglib.uibk.ac.at/ulbtirolhs/content/titleinfo/4864453), 2020.</small>
- <small> Gregor, P., **Inversion of Glacier Bed from Surface Observations by Cost Minimization: Introducing the Open Source Model COMBINE**, [link](https://diglib.uibk.ac.at/ulbtirolhs/content/titleinfo/3086935), 2019.</small>
- <small> Thorlaksson, D., **Calibrating a glacier ice thickness model from in-situ point measurements**, [link](https://diglib.uibk.ac.at/urn:nbn:at:at-ubi:1-7259), 2017.</small>

**Bachelor / Undergrad**
- <small> Cort, J., **An assessment of Swiss glacier change by 2100 under varying climate projections using the Open Global Glacier Model (OGGM)**, 2024.</small>
- <small> Arndt, M., **On Thin Ice: The future of glacial runoff in La Paz, Bolivia**, [doi:10.5281/zenodo.7946884](https://dx.doi.org/10.5281/zenodo.7946884), 2023.</small>
- <small> Schwienbacher, F., **Model sensitivity of the mass-balance module of the OGGM model**, 2017.</small>

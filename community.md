---
layout: page
title: "Community"
description: "Users and developpers of the OGGM model"
header-img: "img/backgrounds/members.jpg"
---

OGGM has a vibrant community of users. We strive for open communication and active community support. Welcome!

### Github, Open Meetings and Slack

A lot of the project communication regarding code issues or support happens on [GitHub](https://github.com/OGGM/oggm). We also have a very active Slack community for chit-chat ([reach out](mailto:info@oggm.org)
if you want to join in, it is open to anyone!). We organize regular, [open meetings]({{site.baseurl}}/meetings) to discuss progress and ask questions.

### Social media

Find us on [Twitter](https://twitter.com/OGGM_org)!


### Research projects related to OGGM

Here is a non-exhaustive list of past and current research projects related to OGGM. If you are interested in what you read here, feel free to contact the respective groups for more information and potential collaboration!

#### Current

- [Ocean-ice Interaction of peripheral Greenland Glaciers](ttp://marzeion.info/content/ocean-ice-interaction-peripheral-greenland-glaciers) (Universität Bremen)
- [Projections of global glacier melt under low-end warming scenarios](http://marzeion.info/content/projections-global-glacier-melt-under-low-end-warming-scenarios) (Universität Bremen)
- [Certainties and uncertainties in the future surface mass balance of mountain glaciers](https://www.uibk.ac.at/acinn/research/ice-and-climate/projects/uncertainties-glacier-smb.html.en) (Universität Innsbruck)
- [Paris Agreement Overshooting - Reversibility, Climate Impacts and Adaptation Needs (PROVIDE)](https://www.uibk.ac.at/acinn/research/ice-and-climate/projects/provide.html.en) (Universität Innsbruck)

#### Past

- Evaluating simulated centennial climate variability over the past millennium using global glacier modelling - LMGLACE (UC Louvain)
- [Predictability and Attribution of Regional Sea Level Change Caused by Glacier Mass Change](http://marzeion.info/content/predictability-and-attribution-regional-sea-level-change-caused-glacier-mass-change) (Universität Bremen)
- [The Upper Grindelwald Glacier as indicator for Holocene climate variability](http://acinn.uibk.ac.at/research/ice-and-climate/projects/grindelwald) (Universität Innsbruck)
- [Modelling of glacier length changes in the Alps on the base of tree-ring based temperature reconstructions for the last 2500 years](http://acinn.uibk.ac.at/research/ice-and-climate/projects/glacier-length) (Universität Innsbruck)

### Past and present OGGM contributors

{% assign people = site.data.people | sort:"last_name" %}

<ul style="columns: 3; -webkit-columns: 3; -moz-columns: 3; list-style-type: none;">
{% for member in people %}
{% if member.visible %}
  <li style="display: inline-block;">
	<strong>{{ member.first_name }} {{ member.last_name }} </strong>
	<br>
	<small><i>{{ member.institution }}</i></small>
	<br>
	{% if member.github %}
	<small>
	<a href="https://github.com/{{ member.github }}" title="Github" target="_blank"><span class="fa-stack fa-lg"> <i class="fa fa-github fa-stack-1x"></i> </span></a>
  </small>
	{% endif %}
	{% if member.url %}
	<small>
	<a href="{{ member.url }}" title="Google Plus" target="_blank"><span class="fa-stack fa-lg"><i class="fa fa-external-link fa-stack-1x"></i></span></a>
  </small>
	{% endif %}
  <hr>
	</li>
{% endif %}
{% endfor %}
</ul>

### Networks

 <a href="https://cryo-tools.org/">
 <img src="https://cryo-tools.org/wp-content/uploads/2017/10/cryo-tools-logo-200px.png" alt="CryTools logo" height="130px" style="margin-left:10px">
</a>

 <a href="https://cryosphericsciences.org/">
 <img src="http://www.iugg.org/images/logos/IACS_logo_new2.png" alt="IUGG-IACS logo"  height="120px" style="margin-left:10px">
</a>
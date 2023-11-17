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

### Research projects related to OGGM

Here is a non-exhaustive list of past and current research projects related to OGGM. If you are interested in what you read here, feel free to contact the respective groups for more information and potential collaboration!

#### Current

- [Ocean-ice Interaction of peripheral Greenland Glaciers](https://groce.de/en/our-projects/5-peripheral-glaciers/) (Universität Bremen)
- [Assessment of the ocean contribution to mass loss of Greenland’s peripheral glaciers – a scale-transitioning approach](https://gepris.dfg.de/gepris/projekt/443246981) (MARUM, Universität Bremen)
- Projections of global glacier melt under low-end warming scenarios (Universität Bremen)
- [Certainties and uncertainties in the future surface mass balance of mountain glaciers](https://www.uibk.ac.at/acinn/research/ice-and-climate/projects/uncertainties-glacier-smb) (Universität Innsbruck)
- [Paris Agreement Overshooting - Reversibility, Climate Impacts and Adaptation Needs (PROVIDE)](https://www.uibk.ac.at/acinn/research/ice-and-climate/projects/provide) (Universität Innsbruck)

#### Past

- Evaluating simulated centennial climate variability over the past millennium using global glacier modelling - LMGLACE (UC Louvain)
- Predictability and Attribution of Regional Sea Level Change Caused by Glacier Mass Change (Universität Bremen)
- [The Upper Grindelwald Glacier as indicator for Holocene climate variability](https://www.uibk.ac.at/acinn/research/ice-and-climate/projects/holocene-climate-variability) (Universität Innsbruck)
- [Modelling of glacier length changes in the Alps on the base of tree-ring based temperature reconstructions for the last 2500 years](https://www.uibk.ac.at/acinn/research/ice-and-climate/projects/modelling-glacier-length-changes) (Universität Innsbruck)

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

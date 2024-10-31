---
layout: page
title: "Research projects"
description: "Research projects making use of OGGM"
header-img: "img/backgrounds/members.jpg"
---

Below is a non-exhaustive list of past and current research projects where OGGM is used. We are not aware of all of them! [Click here](https://github.com/OGGM/oggm.github.io/issues/248) if you’d like to add your own.

{% assign projects = site.data.projects | sort:"dates" | reverse %}

<ul style="list-style-type: none;">
{% for project in projects %}
{% if project.visible %}
  <li style="display: inline-block;">
	<strong>{{ project.dates }}: {{ project.title }} </strong>
	{% if project.url %}
	<small>
	<a href="{{ project.url }}" title="Project website" target="_blank">
      <i class="fa fa-external-link"></i>
    </a>
    </small>
	{% endif %}
	<br>
	<small><strong>PI:</strong> {{ project.pi }}</small> <br>
	<small><strong>Institution:</strong> {{ project.institution }}</small> <br>
	<small><strong>Funder:</strong> {{ project.funder }}</small>
  <hr>
	</li>
{% endif %}
{% endfor %}
</ul>

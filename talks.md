---
layout: default
title: Talks
permalink: talks/
---

<div class="home">
  {%- if page.title -%}
    <h1 class="page-heading">{{ page.title }}</h1>
  {%- endif -%}


<div id="list-talks">
<h2>Talks and Workshops</h2>

{% for talk in site.categories.talks %}
<p class="talk-item" id="talk-{{forloop.index}}"><a href="{{talk.conference_link}}">{{ talk.conference }}</a> - <em>{{ talk.place }}</em>, {{ talk.date|date:"%D, %d %M %Y" }}.
{% if talk.link %}
<a href="{{talk.link}}"><span class="ui-icon ui-icon-circle-arrow-s"></span>Download</a>
{% endif %}
</p>

{% endfor %}
</div>
</div>


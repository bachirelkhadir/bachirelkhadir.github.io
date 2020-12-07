---
layout: default
---

<div class="home">
  {%- if page.title -%}
    <h1 class="page-heading">{{ page.title }}</h1>
  {%- endif -%}
  <h1>About me</h1>
  <img id="myphoto" alt="Bachir El Khadir" src="{{ "/assets/imgs/me.jpg" | relative_url }}"/>
  <div id="aboutme">
  {% include_relative about.md %}
  </div>

<h2>News</h2>
{{site.news.size}} News.
<ul>
  {% for post in site.news %}
  News:
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>


</div>

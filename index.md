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


<div id="recent-news">
    <h2 id="news-title">Recent News and Highlights</h2>
    <div id="news">
    <section class="year">
    <h3>2020</h3>
    <ul>
    {% for news in site.categories.news %}
    {% capture year %}{{ news.date | date: "%Y"}}{% endcapture %}
    {% if year == "2020" %}
    <li>{{news.content}}</li>
    {% endif %}
    {% endfor %}
    </ul>
    </section>
    </div> 
</div>

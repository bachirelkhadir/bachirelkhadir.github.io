---
layout: default
title: Publications
permalink: publications/
---

<div class="home">
  {%- if page.title -%}
    <h1 class="page-heading">{{ page.title }}</h1>
  {%- endif -%}
  
  
    {% for publication in site.categories.publications %}



<div class="publication" id="publication-{{publication.id}}">
    <p><span class="title">{{ publication.title }}</span>.
        <span class="authors">{{ publication.authors }}</span>,
        <span class="date">{{ publication.date|date:"%Y" }}.</span>
        {% if publication.journal %}
        <span class="journal">{{ publication.journal }}.</span>
        {% endif %}
        {% for links in publication.links %}
        {% for link in links %}
        <a href="{{link[1]}}">[{{link[0]}}]</a>
        {% endfor %}
        {% endfor %}
        <nobr><a id="show-abstract-{{forloop.index}}"><span id="abstract-icon-{{forloop.index}}" class="ui-icon ui-icon-plusthick"></span>Abstract</a></nobr>.
    </p>
    <p hidden class="abstract-info minimize" id="abstract-info-{{forloop.index}}">{{ publication.content | strip_html }}</p>

<div class="img-list">
          {% for pic in publication.images %}
          
            <a href="/assets/imgs/publications/{{ pic.url }}">
              <figure>
                {% if pic.thumbnail %}
                <img alt="{{ pic.description }} (thumbnail)" title="{{ pic.description }} (thumbnail)" src="/assets/imgs/publications/{{ pic.thumbnail }}" loading="lazy">
                {% else %}
                <img alt="{{ pic.description }}" title="{{ pic.description }}" src="/assets/imgs/publications/{{ pic.url }}" loading="lazy">
                {% endif %}
                    <figcaption>{{ pic.description }}</figcaption>
                </figure>
            </a>
    {% endfor %}
    </div>
</div>


{% endfor %}


</div>




<script>
 $(document).ready(function(){
     {% for publication in site.categories.publications %}
     $("#abstract-info-{{forloop.index}}").hide();
     $("#show-abstract-{{forloop.index}}").click(function(){
         var icon = $("#abstract-icon-{{forloop.index}}");
         icon.toggleClass("ui-icon-plusthick");
         icon.toggleClass("ui-icon-minusthick");
         $("#abstract-info-{{forloop.index}}").toggle();
     });
     {% endfor %}
 });
 // http://jsfiddle.net/iambriansreed/bjdSF/
 jQuery(function(){
     var minimized_elements = $('p.minimize');
     var max_length = 300;
     minimized_elements.each(function(){
         var t = $(this).text();
         if(t.length < max_length) return;

         $(this).html(
             t.slice(0, max_length)+'<span>... </span><a href="#" class="more">More</a>'+
             '<span style="display:none;">'+ t.slice(max_length, t.length)+' <a href="#" class="less">Less</a></span>'
         );

     });

     $('a.more', minimized_elements).click(function(event){
         event.preventDefault();
         $(this).hide().prev().hide();
         $(this).next().show();
     });

     $('a.less', minimized_elements).click(function(event){
         event.preventDefault();
         $(this).parent().hide().prev().show().prev().show();
     });
 });
</script>

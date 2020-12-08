---
layout: default
title: Talks
permalink: talks/
---

<div class="home">
<h1 class="page-heading">Talks and Workshops</h1>


<div id="map-talks"></div>

<div id="list-talks">
{% for talk in site.categories.talks %}
<p class="talk-item" id="talk-{{forloop.index}}"><a href="{{talk.conference_link}}">{{ talk.conference }}</a> - <em>{{ talk.place }}</em>, {{ talk.date|date:"%D, %d %M %Y" }}.
</p>
{% endfor %}
</div>




<script>

$(document).ready(function(){
    var mymap = L.map('map-talks').setView([40., -50.], 2);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: '',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        accessToken: 'pk.eyJ1IjoibWFyb3hlIiwiYSI6ImNrMHk5ZXZuZzBjaHUzaXBoejhobm83emQifQ.hvVILgnjUb_jj9eMR127Dg'
    }).addTo(mymap);


    {% for talk in site.categories.talks %}
    {% if talk.longitude %}
    var marker = L.marker([{{talk.longitude}},{{talk.latitude}}]).addTo(mymap);
    marker.bindPopup("{{talk.conference}}, {{talk.date|date:'%M %Y'}}");

    // When the marker is clicked,
    // highlight the corresponding item in the list of talks
    marker.on('click', function(e){
        $(".talk-item").removeClass("talk-selected");
        $("#talk-{{forloop.index}}").addClass( "talk-selected" );
    });

    marker.setIcon(L.icon({iconUrl: '/assets/imgs/red_pin.png', iconSize: [24, 24],}));
    marker{{forloop.index}} = marker;
    $("#talk-{{forloop.index}}").click(function() {
        marker{{forloop.index}}.openPopup();
        $(".talk-item").removeClass("talk-selected");
        $("#talk-{{forloop.index}}").addClass( "talk-selected" );
    })
    {% endif %}
    {% endfor %}

});
</script>
</div>

#!/usr/bin/env python3

#!/usr/bin/env python3
import shutil
import json
import pandas as pd
from slugify import slugify
import datetime


backup_js_fn = "./bachirelkhadir.com.dec06.2020.json"
template_fn = "output/talks/{date_trim}-{slug}.md"
template_content = """\
---
conference : {conference}
place : {place}
link : {link}
conference_link : {conference_link}
date : {date}
longitude : {longitude}
latitude : {latitude}
---

Talk

"""

with open(backup_js_fn) as backup_file:
    backup = json.load(backup_file)

backup = [entry['fields'] for entry in backup if entry['model'] == 'research.talk']

escape = lambda s: '"%s"' % s

for entry in backup:
    date = entry['date']
    date = str(datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z'))
    # date = date.strftime('%Y-%m-%d HH:MM:SS')
    date_trim = date[:10]

    conference = escape(entry['conference'])
    place = escape(entry['place'])
    link = escape(entry['link'])
    conference_link = escape(entry['conference_link'])
    date = escape(entry['date'])
    longitude = escape(entry['longitude'])
    latitude = escape(entry['latitude'])

    print(date, date_trim + "|")

    slug = slugify(conference)[:10]
    fn = template_fn.format(**locals())
    with open(fn, "w") as f:
        f.write(template_content.format(**locals()))

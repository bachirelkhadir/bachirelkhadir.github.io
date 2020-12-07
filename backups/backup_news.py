#!/usr/bin/env python3
import shutil
import json
import pandas as pd
from slugify import slugify
import datetime


backup_js_fn = "./bachirelkhadir.com.dec06.2020.json"
template_fn = "output/news/{date_trim}-{slug}.md"
template_content = """\
---
date:   {date}
---

{content}
"""

with open(backup_js_fn) as backup_file:
    backup = json.load(backup_file)


backup = [entry['fields'] for entry in backup if entry['model'] == 'news.news']

for entry in backup:
    date = entry['date']
    date = str(datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z'))
    # date = date.strftime('%Y-%m-%d HH:MM:SS')
    date_trim = date[:10]
    print(date, date_trim + "|")

    content = entry['body']
    slug = slugify(content)[:10]
    fn = template_fn.format(**locals())
    with open(fn, "w") as f:
        f.write(template_content.format(**locals()))





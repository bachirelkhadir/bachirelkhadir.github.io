#!/usr/bin/env python3

#!/usr/bin/env python3
import shutil
import json
import pandas as pd
from slugify import slugify
import datetime


backup_js_fn = "./bachirelkhadir.com.dec06.2020.json"
template_fn = "output/publications/{date_trim}-{slug}.md"
template_content = """\
---
date:   {date}
title: {title}
status: {status}
authors: {authors}
link: {link}
journal: {journal}
remark: {remark}
---

{abstract}

"""

with open(backup_js_fn) as backup_file:
    backup = json.load(backup_file)

# print(backup)
backup = [entry['fields'] for entry in backup if entry['model'] == 'research.publication']

print(pd.DataFrame(backup).columns)
exit
for entry in backup:
    date = entry['date']
    date = str(datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z'))
    # date = date.strftime('%Y-%m-%d HH:MM:SS')
    date_trim = date[:10]

    title = entry["title"]
    status = entry["status"]
    authors = entry["authors"]
    link = entry["link"]
    journal = entry["journal"]
    remark = entry["remark"]
    abstract = entry["abstract"]

    print(date, date_trim + "|")

    slug = slugify(title)[:10]
    fn = template_fn.format(**locals())
    with open(fn, "w") as f:
        f.write(template_content.format(**locals()))

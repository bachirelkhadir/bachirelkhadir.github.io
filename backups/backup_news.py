#!/usr/bin/env python3

import json
import pandas as pd

backup_js_fn = "./bachirelkhadir.com.dec06.2020.json"
with open(backup_js_fn) as backup_file:
    backup = json.load(backup_file)


backup = [entry['fields'] for entry in backup if entry['model'] == 'news.news']


backup = pd.DataFrame(backup)

print(backup)

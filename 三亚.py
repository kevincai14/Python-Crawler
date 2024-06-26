import requests
import csv
import json
import re
from bs4 import BeautifulSoup
from lxml import etree

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}
res = requests.get("https://www.sanyaairport.com/appsvr/pageHbdt?flightNumber=&planDate=&flightAttr=22&size=20&page=1", headers=headers)

print(res.text)

# pattern = re.compile(r'"(\w+)":\s*(".*?"|null|\d+)')
# matches = pattern.findall(res.text)
#
# data = {key: value.strip('"') if value != 'null' else None for key, value in matches}
#
# fields = list(data.keys())
#
# with open('三亚航班.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.DictWriter(file, fieldnames=fields)
#     writer.writeheader()
#     writer.writerow(data)

record_pattern = re.compile(r'\{.*?\}', re.DOTALL)
records = record_pattern.findall(res.text)

data_list = []
for record in records:
    matches = re.findall(r'"(\w+)":\s*(".*?"|null|\d+)', record)
    data = {key: value.strip('"') if value != 'null' else None for key, value in matches}
    data_list.append(data)

fields = set()
for data in data_list:
    fields.update(data.keys())
fields = list(fields)

with open('三亚航班.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for data in data_list:
        writer.writerow(data)


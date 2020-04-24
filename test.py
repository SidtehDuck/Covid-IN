import requests, json, time, os, random

r = requests.get('https://api.covid19india.org/raw_data.json')

print(r.status_code)

data = r.text

print(data)
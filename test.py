import requests, json, time, os, random
import pandas as pd, numpy as np, matplotlib as plt


f = open('token.json',)
token_data = json.load(f)

print(token_data['token'])



r = requests.get('https://api.covid19india.org/data.json')

data = r.json()

print('Total cases so far in India: ' + data['statewise'][0]['confirmed'] + '\n')


if data['statewise'][1]['statecode'] == 'MH':
    print('YEET MAHARASHTRA IS FUCKED BOIS')
    print('Confirmed cases: ' + data['statewise'][1]['confirmed'])
    print('Active cases: ' + data['statewise'][1]['active'])

if data['statewise'][2]['statecode'] == 'GJ':
    print('GUJARAT IS FUCKING DYING TOO BOIS')
    print('Confirmed cases: ' + data['statewise'][2]['confirmed'])
    print('Active cases: ' + data['statewise'][2]['active'])
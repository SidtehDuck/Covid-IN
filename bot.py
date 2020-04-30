import discord, os, time, random, json
from discord.utils import get
from discord.ext import commands
from discord import Embed, Emoji
from discord.ext.commands import Bot
import requests

#holy fucking shit this code is spaghetti as fuck

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

token_file = open('token.json',)
token_data = json.load(token_file)
TOKEN = token_file['token']

client = commands.Bot(command_prefix = '%')
os.chdir(r'home/ducc/duccz/Covid-IN')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'You are delayed by {round(client.latency * 1000)} ms')


client.run(TOKEN)
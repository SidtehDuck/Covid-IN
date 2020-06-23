import discord, os, time, random, json
from discord.utils import get
from discord.ext import commands
from discord import Embed, Emoji
from discord.ext.commands import Bot
import requests
from datetime import datetime

#holy fucking shit this code is spaghetti as fuck

r = requests.get('https://api.covid19india.org/data.json')
data = r.json()

'''if data['statewise'][1]['statecode'] == 'MH':
    print('YEET MAHARASHTRA IS FUCKED BOIS')
    print('Confirmed cases: ' + data['statewise'][1]['confirmed'])
    print('Active cases: ' + data['statewise'][1]['active'])

if data['statewise'][2]['statecode'] == 'GJ':
    print('GUJARAT IS FUCKING DYING TOO BOIS')
    print('Confirmed cases: ' + data['statewise'][2]['confirmed'])
    print('Active cases: ' + data['statewise'][2]['active'])

token_file = open('token.json',)
token_data = json.load(token_file)
TOKEN = str(token_file['token'])
'''

with open("token.json", "r") as infile:
    try:
        CONFIG = json.load(infile)
        TOKEN = CONFIG["token"]
    except (KeyError, FileNotFoundError):
        raise EnvironmentError(
            "Your token.json file is either missing, or incomplete. Check your config.json and ensure it has the keys 'token' and 'owner_id'"
        )

client = commands.Bot(command_prefix = '%')
#os.chdir(r'home/ducc/duccz/Covid-IN')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'You are delayed by {round(client.latency * 1000)} ms')

@client.command()
async def statMH(ctx):
    await ctx.send('cases in MH rn: ' + data['statewise'][1]['confirmed'])
    await ctx.send('active cases in MH rn: ' + data['statewise'][1]['active'])
    await ctx.send('total deaths in MH rn: ' + data['statewise'][1]['deaths'])
@client.command()
async def statPB(ctx):
    await ctx.send('confirmed cases in punjab rn: ' + data['statewise'][15]['confirmed'])
    await ctx.send('active cases in punjab rn: ' + data['statewise'][15]['active'])
    await ctx.send('total deaths in punjab rn: ' + data['statewise'][15]['deaths'])

@client.command()
async def statCG(ctx):
    await ctx.send('confirmed cases in CG rn: ' + data['statewise'][23]['confirmed'])
    await ctx.send('active cases in CG rn: ' + data['statewise'][23]['active'])
    await ctx.send('total deaths in CG rn: ' + data['statewise'][23]['deaths'])

@client.command()
async def statRJ(ctx):
    await ctx.send('confirmed cases in RJ rn: ' + data['statewise'][5]['confirmed'])
    await ctx.send('active cases in RJ rn: ' + data['statewise'][5]['active'])
    await ctx.send('total deaths in RJ rn: ' + data['statewise'][5]['deaths'])

@client.command()
async def statT(ctx):
    await ctx.send('confirmed cases in India rn: ' + data['statewise'][0]['confirmed'])
    await ctx.send('active cases in India rn: ' + data['statewise'][0]['active'])
    await ctx.send('total deaths in India rn: ' + data['statewise'][0]['deaths'])

@client.command()
async def statlemi(ctx):
    await ctx.send('Random text here')


client.run(TOKEN)
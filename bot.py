import discord, time, random, json
from discord.utils import get
from discord.ext import commands
from discord import Embed, Emoji
from discord.ext.commands import Bot
import requests
from datetime import datetime

TOKEN = 'redacted'
client = commands.Bot(command_prefix = '%')


r = requests.get('https://api.covid19india.org/data.json')
data = r.json()

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    embed = discord.Embed(
        title='Ping',
        description=f'🏓 Pong! \t `{round(client.latency * 1000)}ms`',
        colour=discord.Colour.red(),
        timestamp=datetime.utcnow()
    )
    await ctx.send(embed=embed)

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
    await ctx.send('confirmed cases in' + data['statewise'][21]['state'] + 'rn: ' + data['statewise'][21]['confirmed'])
    await ctx.send('active cases in CG rn: ' + data['statewise'][21]['active'])
    await ctx.send('total deaths in CG rn: ' + data['statewise'][21]['deaths'])

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

client.run(TOKEN)
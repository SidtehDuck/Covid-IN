import discord, os, time, random, json
from discord.utils import get
from discord.ext import commands
from discord import Embed, Emoji
from discord.ext.commands import Bot
import requests

TOKEN = 'redacted'
client = commands.Bot(command_prefix = '.cin ')
#os.chdir(r'directory here')

response = requests.get('')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'You are delayed by {round(client.latency * 1000)} ms')


client.run(TOKEN)
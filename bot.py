import discord
import json
import os
import time
import random
from discord.utils import get
from discord.ext import commands
from discord import Embed, Emoji
from discord.ext.commands import Bot

TOKEN = 'NzAxNTA4NjAxODY0MjU3NjM5.Xpyg8g.00VMNpm9Uen5H73itaNVg7eskZA'
client = commands.Bot(command_prefix = '.cin ')
os.chdir(r'C:\Users\chiku\Downloads\COVID-IN')


@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'your retarded ass is delayed by {round(client.latency * 1000)} ms')

@client.command()
async def harshit(ctx):

    for i in range(1):
        await ctx.send('atti batti shatti harshit khaye batti <@553560674043953163>')


client.run(TOKEN)
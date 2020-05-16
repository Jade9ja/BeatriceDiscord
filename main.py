import discord
from discord.ext import commands
import io
import os
import aiohttp
BOT_TOKEN = '<Your bot token here>'
client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('ready!')

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('BOT_TOKEN')

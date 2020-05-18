import discord
from discord.ext import commands
import io
import os
from utils import default
client = commands.Bot(command_prefix = '/')
config = default.get("config.json")
@client.event
async def on_ready():
    print('We ready fam!')
    
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(config.token)

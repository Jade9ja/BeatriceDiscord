import time
import discord
import psutil
import os
from datetime import datetime
from discord.ext import commands
from utils import default

class inf(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.config = default.get("config.json")
        self.process = psutil.Process(os.getpid())

    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.client.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command()
    async def invite(self, ctx):
        """ Invite me to your server """
        await ctx.send(f"**{ctx.author.name}**, use this URL to invite me\n<{discord.utils.oauth_url(self.client.user.id)}>")

    @commands.command()
    async def saucecode(self, ctx):
        """ Check put discord.py documentation here :)"""
        #Check out https://github.com/Jade9ja/AspiritusDiscord
        await ctx.send(f"**{ctx.client.user}** is powered by discord.py, read the docs here:\nhttps://discordpy.readthedocs.io/en/latest/")

    @commands.command()
    async def about(self, ctx):
        """ About the client """
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = round(len(self.client.users) / len(self.client.guilds))

        embedColour = discord.Embed.Empty
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            embedColour = ctx.me.top_role.colour

        embed = discord.Embed(colour=embedColour)
        embed.set_thumbnail(url=ctx.client.user.avatar_url)
        embed.add_field(name="Uptime", value=self.client.uptime, inline=True)
        embed.add_field(
            name=f"Developer{'' if len(self.config.owners) == 1 else 's'}",
            value=', '.join([str(self.client.get_user(x)) for x in self.config.owners]),
            inline=True)
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(name="Servers", value=f"{len(ctx.client.guilds)} ( avg: {avgmembers} users/server )", inline=True)
        embed.add_field(name="Commands loaded", value=len([x.name for x in self.client.commands]), inline=True)
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"ℹ About **{ctx.client.user}** | **{self.config.version}**", embed=embed)


def setup(client):
    client.add_cog(inf(client))

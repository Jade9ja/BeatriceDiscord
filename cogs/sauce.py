import datetime
import json
import requests
import discord
from discord.ext import commands
from jikanpy import Jikan
from jikanpy.exceptions import APIException
jikan = Jikan() 
api = 'https://trace.moe/api/search?url='
malu = 'https://myanimelist.net/anime/'
class sauce(commands.Cog):
    ''' Image size should be <10 MB'''

    def __init__(self,client):
        self.client = client

    @commands.command()
    async def sauce(self,ctx,*args):
        url = "".join(args)
        res = requests.get(api + url).json()
        entitle = res.get('docs')[0].get("title_english")
        nattitle = res.get('docs')[0].get("title_native")
        episodes = res.get('docs')[0].get("episode")
        season = res.get('docs')[0].get("season")
        malid = res.get('docs')[0].get("mal_id")
        perc = res.get('docs')[0].get("similarity")
        rperc = perc*100
        rperc = round(rperc,2)
        anime = jikan.anime(malid)
        imgurl = anime.get("image_url")
        embed = discord.Embed(
            title = 'getSauce',
            description = 'My top guess:',
            colour = ctx.author.top_role.colour
        )
        embed.add_field(name ='Similarity:', value = f'{rperc}',inline=False)
        embed.add_field(name = entitle + f' ({nattitle})', value = 'Episode: ' + str(episodes) + '\n Season: ' + str(season) + '\n MAL: ' + str(malu) + str(malid),inline= False)
        embed.set_footer(text='Trace.moe API | Beta')
        embed.set_thumbnail(url = imgurl)
        await ctx.send(embed = embed)
def setup(client):
    client.add_cog(sauce(client))



import discord
from discord.ext import commands
from jikanpy import Jikan
from jikanpy.exceptions import APIException
import re
import asyncio
jikan = Jikan() 

class anime(commands.Cog):
    '''The anime module..'''
    def __init__(self,client):
        self.client = client

    async def cog_command_error(self,ctx,error):
        print('Error in {}:{}'.format(ctx,error))

    @commands.command()
    async def anime(self,ctx,*args):
        query = " ".join(args)
        try:
            mid = jikan.search("anime", query).get("results")[0].get("mal_id") # Not always accurate...but me lazy :P
        except APIException:
            print("Error connecting to service!")
        if mid:
            anime = jikan.anime(mid)
            atitle = anime.get("title")
            japanese = anime.get("title_japanese")
            typ = anime.get("type")
            duration = anime.get("duration")
            synopsis = anime.get("synopsis")
            source = anime.get("source")
            status = anime.get("status")
            episodes = anime.get("episodes")
            score = anime.get("score")
            rating = anime.get("rating")
            genre_lst = anime.get("genres")
            genres = ""
            for genre in genre_lst:
                genres += genre.get("name") + ", "
            studios = ""
            studio_lst = anime.get("studios")
            for studio in studio_lst:
                studios += studio.get("name") + ", "
            duration = anime.get("duration")
            premiered = anime.get("premiered")
            image_url = anime.get("image_url")
        else:
            await ctx.send("No results found!")
        embed = discord.Embed(
            title = atitle + f" ({japanese})",
            description = synopsis,
            colour = ctx.author.top_role.colour
        )
        embed.set_footer(text='Jikan API | Data provided by MyAnimeList.net ID: {}'.format(str(mid)))
        embed.set_thumbnail(url= image_url)
        embed.add_field(name='**Type|Rating:**', value = str(typ) + ' | ' + str(rating),inline=False)
        embed.add_field(name='**Source**', value = source,inline=False)
        embed.add_field(name='**Status:**', value = status,inline=False)
        embed.add_field(name='**genres:**', value = genres,inline=False)
        embed.add_field(name='**Episodes/Duration:**', value = str(episodes) + ' @ ' + str(duration),inline=False)
        embed.add_field(name='**Score:**', value = score,inline=False)
        embed.add_field(name='**Studio(s):**', value = studios,inline=False)
        embed.add_field(name='**Premiered:**', value = premiered,inline=False)
        embed.add_field(name='MyAnimeList Link', value='https://myanimelist.net/anime/' + str(mid), inline=False)
        
        await ctx.send(embed = embed)

    @commands.command()
    async def manga(self,ctx,*args):
        query = " ".join(args)
        try:
            mid = jikan.search("manga", query).get("results")[0].get("mal_id") # Not always accurate...but me lazy :P
        except APIException:
            print("Error connecting to service!")
        if mid:
            manga = jikan.manga(mid)
            typ = manga.get("type")
            score = manga.get("score")
            mtitle = manga.get("title")
            chapters = manga.get("chapters")
            status = manga.get("status")
            volumes = manga.get("volumes")
            japanese = manga.get("title_japanese")
            synopsis = manga.get("synopsis")
            image = manga.get("image_url")
            genre_lst = manga.get("genres")
            genres = ""
            for genre in genre_lst:
                genres += genre.get("name") + ", "
        else:
            await ctx.send("No results found!")
        embed = discord.Embed(
            title = mtitle + f" ({japanese})",
            description = synopsis,
            colour = ctx.author.top_role.colour
        )
        embed.set_footer(text='Jikan API | Data provided by MyAnimeList.net ID: {}'.format(str(mid)))
        embed.set_thumbnail(url= image)
        embed.add_field(name='**Type:**', value = typ,inline=False)
        embed.add_field(name='**Status:**', value = status,inline=False)
        embed.add_field(name='**genres:**', value = genres,inline=False)
        embed.add_field(name='**Score:**', value = score,inline=False)
        embed.add_field(name='**Volumes|Chapters:**', value = str(volumes) + ' @ ' + str(chapters),inline=False)
        embed.add_field(name='MyAnimeList Link', value='https://myanimelist.net/manga/' + str(mid), inline=False)
        
        await ctx.send(embed = embed)
    
    @commands.command()
    async def character(self,ctx,*args):
        query = " ".join(args)
        try:
            mid = jikan.search("character", query).get("results")[0].get("mal_id") # Not always accurate...but me lazy :P
        except APIException:
            print("Error connecting to service!")
        if mid:
            char = jikan.character(mid)
            english = char.get("name")
            japanese = char.get("name_kanji")
            about = char.get("about")
            about = about.replace("\n"," ")
            if len(about) > 1200:
                about = about[:1200] + "..."
            img_url = char.get("image_url")
        else:
            await ctx.send("No results found!")
        embed = discord.Embed(
            title = english + f" ({japanese})",
            description = about,
            colour = ctx.author.top_role.colour
        )
        embed.set_footer(text='Jikan API | Data provided by MyAnimeList.net ID: {}'.format(str(mid)))
        embed.set_thumbnail(url= img_url)
        embed.add_field(name='MyAnimeList Link', value='https://myanimelist.net/character/' + str(mid), inline=False)
        
        await ctx.send(embed = embed)

    @commands.command()
    async def upcoming(self,ctx):
        up = jikan.season_later()
        animu = up.get("anime")
        embed = discord.Embed(
            title = 'Upcoming Anime',
            colour = ctx.author.top_role.colour
        )
        ct = 0
        for animes in animu:
            ct += 1
            embed.add_field(name=f'{animes.get("title")}', value = animes.get("url"),inline=False)
            if ct > 20:
                break
        embed.set_footer(text='Jikan API | Data provided by MyAnimeList.net')
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(anime(client))
import datetime
import asyncio
import aiohttp
import discord
from discord.ext import commands
from pytz import timezone



class admin(commands.Cog):
    '''Group management module...'''

    def __init__(self,client):
        self.client = client

    def _currenttime(self):
        return datetime.datetime.now(timezone('Asia/Kolkata')).strftime("%H:%M:%S")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def purge(self, ctx, *amt):
        ''' Delete multiple messages 
        /purge <amount>
        '''
        try:
            amt = int(amt[0])
        except IndexError:
            amt = 1
        delt = 0
        while amt >= 1:
            cap = min(amt, 100)
            delt += len(await ctx.channel.purge(limit=cap, before=ctx.message))
            amt -= cap
        tmp = await ctx.send(f'**:put_litter_in_its_place:** {delt} messages Purged!')
        await asyncio.sleep(15)
        await tmp.delete()
        await ctx.message.delete()

    @commands.command()
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member = None, *reason):
        '''Kicks the user in question:
        /kick <usertag>
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            await ctx.send('Goal!!!')
            await member.kick(reason=reason)
        else:
            await ctx.send('Bruh...specify a user!')

    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member=None, *reason):
        '''Bans the user in question
        /ban <usertag>
        '''
        if member is not None:
            if reason:
                reason = ' '.join(reason)
            else:
                reason = None
            tmp = await ctx.send('Whacking the pest ...')
            await asyncio.sleep(5)
            await tmp.delete()
            await ctx.send(f'Banned {member.mention}!')
            await member.ban(reason=reason)
        else:
            await ctx.send('I am not sure, who should I ban?')

    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def unban(self, ctx,*, member):
        '''Unbans the user in question
        /unban <username#discriminator>
        '''
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) ==(member_name, member_disc):
                await ctx.guild.unban(user)
                await ctx.send(f'Fine {user.mention} can join again...')
                return

    @commands.command()
    async def hierarchy(self, ctx):
        '''Lists the role hierarchy of the current server.
'''
        msg = f'Role hierarchy for **{ctx.guild}**:\n\n'
        roleDict = {}

        for role in ctx.guild.roles:
            if role.is_default():
                roleDict[role.position] = 'everyone'
            else:
                roleDict[role.position] = role.name

        for role in sorted(roleDict.items(), reverse=True):
            msg += role[1] + '\n'
        await ctx.send(msg)

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def setrank(self, ctx, member: discord.Member=None, *rankName: str):
        '''Assigns a rank to a user
        /setrole <usertag> <role>
        '''
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        if member is not None:
            await member.add_roles(rank)
            await ctx.send(f':white_check_mark: Assigned the role **{rank.name}** to **{member.name}**.')
        else:
            await ctx.send(':no_entry: Dont be lazy..specify a user -_- ')

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_roles = True)
    @commands.bot_has_permissions(manage_roles = True)
    async def rmrank(self, ctx, member: discord.Member=None, *rankName: str):
        '''Removes a rank from a user
        /rmrole <usertag> <role>
        '''
        rank = discord.utils.get(ctx.guild.roles, name=' '.join(rankName))
        if member is not None:
            await member.remove_roles(rank)
            await ctx.send(f':white_check_mark: Removed the role **{rank.name}** of **{member.name}**.')
        else:
            await ctx.send(':no_entry: Gimme the name!')


def setup(client):
    client.add_cog(admin(client))
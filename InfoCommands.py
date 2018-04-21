from discord.ext.commands import Bot
from discord.ext import commands
import discord
import asyncio
import random

Admins = ['285521611887607809']
colors = [int(0xe6194b), int(0x3cb44b), int(0xffe119), int(0x0082c8), int(0xf58231), int(0x911eb4), int(0x46f0f0), int(0xf032e6), int(0xd2f53c), int(0xfabebe), int(0x008080), int(0xe6beff), int(0xaa6e28), int(0xfffac8), int(0x000000)]

class InfoCommands():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def info(self, ctx, user: discord.Member):
        if ctx.message.author.id in Admins:
            try:
                embed = discord.Embed(title='{}\'s info'.format(user.name), description=None, color=random.choice(colors))
                embed.add_field(name='Name', value=user.name, inline=True)
                embed.add_field(name='ID', value=user.id, inline=True)
                embed.add_field(name='Status', value=user.status, inline=True)
                embed.add_field(name='Role', value=user.top_role)
                embed.add_field(name='Joined', value=user.joined_at)
                embed.set_thumbnail(url=user.avatar_url)
                await self.client.say(embed=embed)
            except:
                await self.client.say('Error! User Is A Required Argument \nExample: .info @ProfessorPiggy#1198')

    @commands.command(pass_context=True)
    async def botinfo(self, ctx):
        if ctx.message.author.id in Admins:
            embed = discord.Embed(title='{}'.format(self.client.user.name), description='Multipurpose Discord Bot', color=random.choice(colors))
            embed.add_field(name='Client ID: ', value=self.client.user.id, inline=True)
            embed.add_field(name='Prefix: ', value='[\'-\']', inline=True)
            embed.add_field(name='Created At: ', value=self.client.user.created_at, inline=True)
            embed.add_field(name='Discriminator: ', value=self.client.user.discriminator, inline=True)
            embed.add_field(name='Discord Version: ', value='Discord.py Async '+discord.__version__, inline=True)
            embed.add_field(name='Running on Python Version: ', value=(__import__('sys').version), inline=True)
            embed.set_thumbnail(url=self.client.user.avatar_url)
            embed.set_footer(text=('Created By Yakob and TheBubbler27'))
            await self.client.say(embed=embed)
        else:
            await self.client.say('You Do Not Have Permission To Use This Command')

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):
        """Shows Server Info"""
        server = ctx.message.server
        roles = [x.name for x in server.role_hierarchy]
        role_length = len(roles)
        roles = ', '.join(roles);
        channels = len(server.channels);
        time = str(server.created_at); time = time.split(' '); time= time[0];

        embed = discord.Embed(description= "Info on this server",title = ':thinking:', colour = random.choice(colors));
        embed.set_thumbnail(url = server.icon_url);
        embed.add_field(name = '__Server __', value = str(server))
        embed.add_field(name = '__Server ID__', value = str(server.id))
        embed.add_field(name = '__Owner__', value = str(server.owner));
        embed.add_field(name = '__Owner ID__', value = server.owner.id)
        embed.add_field(name = '__Members__', value = str(server.member_count));
        embed.add_field(name = '__Text/Voice Channels__', value = str(channels));
        embed.add_field(name = '__Roles__', value = '%s'%str(role_length));
        embed.add_field(name = '__Server Region__', value = '%s'%str(server.region));
        embed.add_field(name = '__Verification Level__', value = server.verification_level)
        embed.add_field(name = '__Created on__', value = server.created_at.__format__('Date - %d %B %Y at time - %H:%M:%S'));
            
        await self.client.say(embed = embed)

def setup(client):
    client.add_cog(InfoCommands(client))

import discord
from discord.ext import commands
import random

colors = [int(0xe6194b), int(0x3cb44b), int(0xffe119), int(0x0082c8), int(0xf58231), int(0x911eb4), int(0x46f0f0), int(0xf032e6), int(0xd2f53c), int(0xfabebe), int(0x008080), int(0xe6beff), int(0xaa6e28), int(0xfffac8), int(0x000000)]
Admins = ['285521611887607809', '168167351580098561']

class DeveloperCommands():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def Load(self, ctx, extension_name : str):
        author = ctx.message.author.id
        if author in Admins:
            """Loads an extension."""
            try:
                self.client.load_extension(extension_name)
            except (AttributeError, ImportError) as e:
                await self.client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
                return
            await self.client.say("`{}` loaded.".format(extension_name))
        else:
            await self.client.say((':eyes: | {} Tried to use `\'Load\'` | ID: {}'.format(ctx.message.author.mention, ctx.message.author.id)))
            await self.client.say(":no_entry_sign: | Staff Only! | Action has been logged!")
            embed = discord.Embed(title='{} Tried To Use An Admin Command!'.format(ctx.message.author.name), description=None, color=0x00ff00)
            embed.add_field(name='User Name:', value=ctx.message.author.name, inline=True)
            embed.add_field(name='User ID:', value=ctx.message.author.id, inline=True)
            embed.add_field(name='Command Used:', value='`-Load`', inline=True)
            embed.add_field(name='Channel Used in:', value=ctx.message.channel.name)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.client.send_message(discord.Object(id='437387457982627840'), embed=embed)
            
    @commands.command(pass_context=True)
    async def Unload(self, ctx, extension_name : str):
        author = ctx.message.author.id
        if author in Admins:
            """Unloads an extension."""
            self.client.unload_extension(extension_name)
            await self.client.say("`{}` unloaded.".format(extension_name))
        else:
            await self.client.say((':eyes: | {} Tried to use `\'Unload\'` | ID: {}'.format(ctx.message.author.mention, ctx.message.author.id)))
            await self.client.say(":no_entry_sign: | Staff Only! | Action has been logged!")
            embed = discord.Embed(title='{} Tried To Use An Admin Command!'.format(ctx.message.author.name), description=None, color=random.choice(colors))
            embed.add_field(name='User Name:', value=ctx.message.author.name, inline=True)
            embed.add_field(name='User ID:', value=ctx.message.author.id, inline=True)
            embed.add_field(name='Command Used:', value='`-Unload`', inline=True)
            embed.add_field(name='Channel Used in:', value=ctx.message.channel.name +': ' + ctx.message.channel.id)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.client.send_message(discord.Object(id='437387457982627840'), embed=embed)

    @commands.command(pass_context=True)
    async def Reload(self, ctx, extension_name : str):
        author = ctx.message.author.id
        if author in Admins:
            self.client.unload_extension(extension_name)
            self.client.load_extension(extension_name)
            await self.client.say(':white_check_mark: Reloaded `{}`'.format(extension_name))
        else:
            await self.client.say((':eyes: | {} Tried to use `\'Reload\'` | ID: {}'.format(ctx.message.author.mention, ctx.message.author.id)))
            await self.client.say(":no_entry_sign: | Staff Only! | Action has been logged!")
            embed = discord.Embed(title='{} Tried To Use An Admin Command!'.format(ctx.message.author.name), description=None, color=0x00ff00)
            embed.add_field(name='User Name:', value=ctx.message.author.name, inline=True)
            embed.add_field(name='User ID:', value=ctx.message.author.id, inline=True)
            embed.add_field(name='Command Used:', value='`-Reload`', inline=True)
            embed.add_field(name='Channel Used in:', value=ctx.message.channel.name)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.client.send_message(discord.Object(id='437387457982627840'), embed=embed)

    @commands.command(pass_context=True)
    async def CC(self, ctx, *args):
        if ctx.message.author.id in Admins:
            await self.client.create_channel(discord.Object(args[0]), args[1], type=discord.ChannelType.text)
            await self.client.say('Channel `\'{}\'` Created in {}'.format(args[1], args[0]))
        else:
            await self.client.say((':eyes: | {} Tried to use `\'CC\'` | ID: {}'.format(ctx.message.author.mention, ctx.message.author.id)))
            await self.client.say(":no_entry_sign: | Staff Only! | Action has been logged!")
            embed = discord.Embed(title='{} Tried To Use An Admin Command!'.format(ctx.message.author.name), description=None, color=0x00ff00)
            embed.add_field(name='User Name:', value=ctx.message.author.name, inline=True)
            embed.add_field(name='User ID:', value=ctx.message.author.id, inline=True)
            embed.add_field(name='Command Used:', value='`-CC`', inline=True)
            embed.add_field(name='Channel Used in:', value=ctx.message.channel.name)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.client.send_message(discord.Object(id='437387457982627840'), embed=embed)


    @commands.command(pass_context=True)
    async def makeinv(self, ctx, sid:str):
        if ctx.message.author.id in Admins:
            s = await self.client.create_invite(discord.Object(sid))
            await self.client.say(s)
        else:
            await self.client.say((':eyes: | {} Tried to use `\'makeinv\'` | ID: {}'.format(ctx.message.author.mention, ctx.message.author.id)))
            await self.client.say(":no_entry_sign: | Staff Only! | Action has been logged!")
            embed = discord.Embed(title='{} Tried To Use An Admin Command!'.format(ctx.message.author.name), description=None, color=0x00ff00)
            embed.add_field(name='User Name:', value=ctx.message.author.name, inline=True)
            embed.add_field(name='User ID:', value=ctx.message.author.id, inline=True)
            embed.add_field(name='Command Used:', value='`-makeinv`', inline=True)
            embed.add_field(name='Channel Used in:', value=ctx.message.channel.name)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.client.send_message(discord.Object(id='437387457982627840'), embed=embed)

    @commands.command(pass_context=True)
    async def unban(self, ctx, uid:str):
        if ctx.message.author.id in Admins:
            await self.client.unban(uid, ctx.message.server)
            await self.client.say('Unbanned {} From {}'.format(int(uid), ctx.message.server))
        else:
            await self.client.say((':eyes: | {} Tried to use `\'unban\'` | ID: {}'.format(ctx.message.author.mention, ctx.message.author.id)))
            await self.client.say(":no_entry_sign: | Staff Only! | Action has been logged!")
            embed = discord.Embed(title='{} Tried To Use An Admin Command!'.format(ctx.message.author.name), description=None, color=0x00ff00)
            embed.add_field(name='User Name:', value=ctx.message.author.name, inline=True)
            embed.add_field(name='User ID:', value=ctx.message.author.id, inline=True)
            embed.add_field(name='Command Used:', value='`-unban`', inline=True)
            embed.add_field(name='Channel Used in:', value=ctx.message.channel.name)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.client.send_message(discord.Object(id='437387457982627840'), embed=embed)

    @commands.command(pass_context=True)
    async def Set_prefix(self, ctx, *args):
        if ctx.message.author.id in Admins:
            global BOT_PREFIX
            BOT_PREFIX=(args)
            await self.client.say(':white_check_mark: Prefix Has Been Changed To: `{}`'.format(BOT_PREFIX))
        else:
            await self.client.say((':eyes: | {} Tried to use `\'Set_Prefix\'` | ID: {}'.format(ctx.message.author.mention, ctx.message.author.id)))
            await self.client.say(":no_entry_sign: | Staff Only! | Action has been logged!")
            embed = discord.Embed(title='{} Tried To Use An Admin Command!'.format(ctx.message.author.name), description=None, color=0x00ff00)
            embed.add_field(name='User Name:', value=ctx.message.author.name, inline=True)
            embed.add_field(name='User ID:', value=ctx.message.author.id, inline=True)
            embed.add_field(name='Command Used:', value='`-Set_prefix`', inline=True)
            embed.add_field(name='Channel Used in:', value=ctx.message.channel.name)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.client.send_message(discord.Object(id='437387457982627840'), embed=embed)


def setup(client):
    client.add_cog(Developer
                   Commands(client))

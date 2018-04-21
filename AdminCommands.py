import discord
from discord.ext import commands
import time
import random

Admins = ['285521611887607809', '168167351580098561']
colors = [int(0xe6194b), int(0x3cb44b), int(0xffe119), int(0x0082c8), int(0xf58231), int(0x911eb4), int(0x46f0f0), int(0xf032e6), int(0xd2f53c), int(0xfabebe), int(0x008080), int(0xe6beff), int(0xaa6e28), int(0xfffac8), int(0x000000)]

class AdminCommands():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def test(self, ctx):
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.client.send_typing(channel)
        t2 = time.perf_counter()
        embed=discord.Embed(title=None, description='Testing... {}ms'.format(round((t2-t1)*1000)), color=0x2874A6)
        await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def Disconnect(self, ctx):
        if ctx.message.author.id == '285521611887607809':
            await self.client.say('Logging Out.')
            await self.client.close()
        else:
            await self.client.say('That Is An Owner Command.')

    @commands.command(pass_context=True)
    async def restart(self, ctx):
        if ctx.message.author.id in Admins:
            await self.client.say('Client Has Restarted!')
            await self.client.connect()
        else:
            await self.client.say('You Do Not Have Permission To Use This Command')

    @commands.command(pass_context=True)
    async def Prune(self, ctx, args):
        if ctx.message.author.id in Admins:
            mgs = [] 
            number = int(args)
            async for x in self.client.logs_from(ctx.message.channel, limit = number):
                mgs.append(x)
            await self.client.delete_messages(mgs)
            await self.client.say('Deleted `{}` Messages'.format(number))
        else:
            await self.client.say('You Do Not Have Permission To Use This Command')

    @commands.command(name='eval')
    async def _eval(self, ctx, *, code):
        """A bad example of an eval command"""
        await self.client.say(eval(code))

    @commands.command(pass_context=True)
    async def newnick(self, ctx, user: discord.Member, args):
        if ctx.message.author.id in Admins:
            try:
                await self.client.change_nickname(user, args)
                await self.client.say('{}\'s Nickname Successfully Changed To \'`{}`\''.format(user.mention, args))
            except discord.errors.Forbidden as e:
                await self.client.say('Error! {}'.format(e))
        else:
            await self.client.say('You Do Not Have Permission To Use This Command')

    @commands.command(pass_context=True)
    async def leaveserver(self, ctx, args):
        badserver = self.client.get_server(args)
        await self.client.leave_server(badserver)
        embed = discord.Embed(description = 'Successfully Left {}'.format(badserver.name), title = ':runner:', color = random.choice(colors))
        embed.add_field(name = 'Server ID:', value = badserver.id)
        await self.client.say(embed=embed)


def setup(client):
    client.add_cog(AdminCommands(client))
    

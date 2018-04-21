from discord.ext.commands import Bot
from discord.ext import commands
import discord
import asyncio
import time
import requests
import exception
import random
import aiohttp
from datetime import datetime
import sys
import os
import traceback
import sqlite3

global BOT_PREFIX
BOT_PREFIX=('-', '<@426613171088916492> ')
client = Bot(command_prefix=BOT_PREFIX)
startup_extensions = ['DeveloperCommands', 'AdminCommands', 'InfoCommands', 'Moderation', 'GameShuffle', 'WebRequests']
Admins = ['285521611887607809']
colors = [int(0xe6194b), int(0x3cb44b), int(0xffe119), int(0x0082c8), int(0xf58231), int(0x911eb4), int(0x46f0f0), int(0xf032e6), int(0xd2f53c), int(0xfabebe), int(0x008080), int(0xe6beff), int(0xaa6e28), int(0xfffac8), int(0x000000)]
db = sqlite3.connect('Money.db')
c = db.cursor()

@client.event
async def on_ready():
    print('\n\nLogged in as: {} - {}\nDiscord Version: {}\n'.format(client.user.name, client.user.id, discord.__version__))

@client.event
async def on_member_join(member):
    channel='428062396775661578'
    Member_Role = discord.utils.get(member.server.roles, name='Member')
    await client.add_roles(member, Member_Role)
    await client.send_message(member.server, 'Welcome {} Please Read The Rules And Have Fun.'.format(member.mention))
    #await client.send_message(member.channel, '{} Welcome To {}!'.format(member.mention, member.server.id))
    
@client.command(pass_context=True)
async def admins():
    return

@client.command(pass_context=True)
async def NSFWgif(ctx):
    if ctx.message.author.id in Admins:
        channel = ctx.message.channel
        await client.send_typing(channel)
        number = random.randint(1600,1999)
        link = f"https://cdn.boob.bot/Gifs/{number}.gif"
        await client.say(link)
    else:
        await client.say('You Do Not Have Permission To Use This Command')

@client.command(pass_context=True)
async def urban(ctx, *, args):
    args = args.replace(' ', '+')
    if ctx.message.author.id in Admins:
        channel = ctx.message.channel
        await client.send_typing(channel)
        term = (args)
        link = f"https://www.urbandictionary.com/define.php?term={term}"
        try:
            await client.say(link)
        except:
            await client.say('Error!')
    else:
        await client.say('You Do Not Have Permission To Use This Command')

@client.command(pass_context=True)
async def dog(ctx):
    if ctx.message.author.id in Admins:
        api = "https://api.thedogapi.co.uk/v2/dog.php"
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as r:
                if r.status == 200:
                    response = await r.json()
                    embed = discord.Embed(description=None, color = random.choice(colors))
                    embed.set_author(name = "{} here is your random dog".format(ctx.message.author.name))
                    embed.set_image(url = response['data'][0]["url"])
                    await client.say(embed = embed)
    else:
        await client.say('You Do Not Have Permission To Use This Command')


@client.command(pass_context=True)
async def lottery(ctx, args):
    Win = ('{}-{}-{}'.format(random.randint(1, 99), random.randint(1, 99), random.randint(1, 99)))
    guess = (args)
    if ctx.message.author.id in Admins:
        try:
            await client.say('The Winning Numbers Are: {}\nYour Numbers: {}'.format(Win, guess))
            if guess == Win:
                money = random.randint(200000,10000000)
                await client.say('Congrats! You Won The Lottery! +${}'.format(money))
                db.execute('CREATE TABLE IF NOT EXISTS MoneyData(user TEXT, value REAL)')
                if int(ctx.message.author.id) in ('Money.db'):
                    c.execute('UPDATE MoneyData Set value = {} WHERE value = {}'.format(int(value) + int(money), int(money)))
                    conn.commit()
                if int(ctx.message.author.id) not in ('Money.db'):
                    db.execute('INSERT INTO MoneyData VALUES(?, ?)',
                                (ctx.message.author.id, money))
                    db.commit()
                    c.close()
                    db.close()
            if guess != Win:
                await client.say('{} Better Luck Next Time!'.format(ctx.message.author.mention))
        except:
            await client.say('Error!')
    else:
        await client.say('You Do Not Have Permission To Use This Command')
     
@client.command(pass_context=True)
async def My_Money(ctx):
    #if str(ctx.message.author.id) in ('Money.db'):
        await client.say('Devs Are Currently Working On Currency Commands!')
    
@client.command(pass_context=True)
async def feedback(ctx, *, msg:str):
    embed = discord.Embed(description = 'Used In Server: `{}({})`'.format(ctx.message.server,ctx.message.server.id), title = ':information_source:', color = random.choice(colors))
    embed.set_thumbnail(url = ctx.message.author.avatar_url)
    embed.add_field(name = 'Feedback:', value = '\''+msg+'\'')
    embed.set_footer(text = 'Feedback From {}'.format(ctx.message.author))
    await client.send_message(discord.Object(id='432375243248762880'), embed=embed)
    await client.say('{} Your Feedback Has Been Sent To A Private Dev Channel. Thank You.'.format(ctx.message.author.mention))

@client.command()
async def join(url:str):
    await client.accept_invite(url)
    await client.say('Joined: `{}`!'.format(url))

@client.command()
async def getui(uid:str):
    x = await client.get_user_info(uid)
    await client.say(x)

@client.command(pass_context=True)
async def Verify(ctx):
    x = open('VerifiedUsers.txt', 'r+')
    user=ctx.message.author.id
    VerifyRole = discord.utils.get(ctx.message.author.server.roles, name='Verified')
    if str(user+'\n') in x:
        if VerifyRole in ctx.message.author.roles:
            await client.say('You Have Already Been Verified')
        else:
            await client.say('Your ID Is In My System But You Somehow Lost Your Role. I Have Given You The Role And Updated My System!')
            await client.add_roles(ctx.message.author, VerifyRole)
    else:
        x.write('-----------------\n')
        x.write('UserName: {}\nID:\n'.format(ctx.message.author.name))
        x.write(user+'\n')
        x.close()
        await client.add_roles(ctx.message.author, VerifyRole)
        await client.say(':white_check_mark: You Have Been Verified. {}'.format(ctx.message.author.mention))

@client.command(pass_context=True)
async def CheckVerified(ctx):
    file = open('VerifiedUsers.txt', 'r+')
    x = (ctx.message.author.id+'\n')
    if x in file:
        await client.say('Your ID Is In My System, If You Do Not Have The Role Use The Command `-Verify`')
    else:
        await client.say('You Have Not Been Verified. Use The Command `-Verify` To Recieve The Verified Role.')

#@client.event
#async def on_message_delete(message):
    #await client.send_message(message.channel, '{} Deleted A Message!\nMessage Deleted: \'`{}`\''.format(message.author.mention, message.content))
    
@client.command(pass_context=True)
async def Prefix(ctx):
    await client.say(BOT_PREFIX)

@client.command(pass_context=True)
async def gayrate(ctx, user:discord.Member):
    if user is None:
        embed=discord.Embed(title='GayRate Machine!', description='{}%'.format(random.randint(1,100), colour = random.choice(colors)))
        await client.say(embed=embed)
    if user is not None:
        embed=discord.Embed(title='GayRate Machine!', description='{} is {}% Gay'.format(user.name, random.randint(1,100), colour = random.choice(colors)))
        await client.say(embed=embed)
    
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    
    client.run('NDI2NjEzMTcxMDg4OTE2NDky.DZYiHA.uajSAJfr9C82UfpICpalj2vNgNs')

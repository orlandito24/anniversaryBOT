import discord
import asyncio
from discord.ext import commands, tasks
from datetime import datetime
import os
import random

# token of bot
bot_token = 'ODIwMjM4NDMyMjU2MTMxMDcy.YEyQkQ.m26N8XSVQ259qGivWgHZTAqFtCE'

# client bot thing
bot = commands.Bot(command_prefix = "!",intents = discord.Intents.all())
bot.remove_command("help")

# print(datetime.datetime.today().day)

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    await bot.get_channel(820240672291291148).send('**~ Look bby, i🐛 did a thing 💞 ~**\n type **!help** for commands!')

# Start command: displays all commands avaliable
# each needs to begin with !*blank*
@bot.command()
async def help(ctx):
    await ctx.send('***here lies the anniversary bot commands!***📜\n\n'
                    '**!help** -- prints bot commands 🤖\n'
                    '**!date** -- tells what date our anniversary is 📅\n'
                    '**!today** -- tells whether today is our anniversary or not ❓\n'
                    '**!together** -- tells how long we\'ve been together ♾️\n'
                    '**!next** -- tells how long till next anniversary ⌛\n'
                    '**!kill** -- kills da bot 🤖🔫\n')

# Start command: displays all commands avaliable
# each needs to begin with !*blank*
@bot.command()
async def date(ctx):
    await ctx.send('date of anniversary: **November 20th, 2019**💐')

# Start command: displays all commands avaliable
# each needs to begin with !*blank*
@bot.command()
async def together(ctx):
    x = datetime.today() - datetime(2019, 11, 20)
    days = x.days
    seconds = x.seconds

    year = days // 365
    days = days - (365* year)
    month = days // 30
    days = days - (30 * month)
    hours = seconds // 3600
    seconds = seconds - (3600 * hours)
    minutes = seconds // 60
    seconds = seconds - (60 * minutes)
    await ctx.send('*~you two 🥧 **cutie pies** 🥧 have been together for...~*')
    await ctx.send('***' + str(year) + '*** years, ***' + str(month) + '*** months, ***' + str(days) + '*** days, ***' + str(hours) + '*** hours, ***' + str(minutes) + '*** minutes, ***' + str(seconds) + '*** seconds '+'😱')


@bot.command()
async def next(ctx):

    x = datetime.today()
    if x.month == 12:
        if x.day >= 20:
            y = datetime(year=x.year+1,month=1,day=20)
        else:
            y = datetime(year=x.year,month=x.month,day=20)
    else:
        if x.day >= 20:
            y = datetime(year=x.year,month=x.month+1,day=20)
        else:
            y = datetime(year=x.year,month=x.month,day=20)
    z = y-x
    days = z.days
    seconds = z.seconds
    hours = seconds // 3600
    seconds = seconds - (3600 * hours)
    minutes = seconds // 60
    seconds = seconds - (60 * minutes)
    await ctx.send('*~get hyyppeedd💯, your next anniversary is in...~*')
    await ctx.send('⏱️ ***'+ str(days) + '*** days, ***' + str(hours) + '*** hours, ***' + str(minutes) + '*** minutes, ***' + str(seconds) + '*** seconds ')

# Kill_Bot command: ends the game that is currently gonig onskips the timer for lobby creation
@bot.command()
async def kill(ctx):
    await ctx.send('bye love birds 🐥💖🐥')
    await ctx.send('i die now ⚰️')
    await bot.logout()

# UNDER CONSTRUCTION
@bot.command()
async def today(ctx):
    if datetime.today().day != 20:
        await ctx.send('**no, its not today** 😢')
    else:
        await ctx.send('**yea it is! YAYAY! don\'t forget to give kithes** 💋')

bot.run(bot_token)

# # if our day = 0 its not our aniv, if 1 then our aniv
# our_day = 0
# @tasks.loop(count=None,reconnect=True)
# async def checker():
#     global our_day
#     if datetime.today().day == 20:
#         our_day = 1
#     else:
#         our_day = 0

# checker.start()
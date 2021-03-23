from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime
import asyncio
import discord

client = discord.Client()
bot = commands.Bot(command_prefix='*$')
token = os.environ['DISCORD_BOT_TOKEN']

# UTC
dateTimeList = ['05:00']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@tasks.loop(seconds=30)
async def time_check():

    check = datetime.now().strftime('%H:%M')
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    channel = bot.get_channel(820269526733160451)

    if check in dateTimeList:
        print("loopcheck2")
        if datetime.now().day % 2 == 0:

            print(now)
            await channel.send('@everyone\n本日のギルドマイレージは\n【パターン１】\nラモー戦場１回入場（ヴォルクス）\nラモー戦場１回入場（黒結晶）\nラモー戦場２回入場（ヴォルクス）\nラモー戦場２回入場（黒結晶）\n古代遺跡５回完了\n古代遺跡１５回完了')
            await asyncio.sleep(60)
        else:
            print(now)
            await channel.send('test')
            await asyncio.sleep(60)

time_check.start()
bot.run(token)

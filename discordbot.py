from discord.ext import commands
import os
import traceback
import time
from discord.ext import tasks
from datetime import datetime
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channel = os.environ['CHANNEL_ID']


dateTimeList_1 = ['2021/03/15 02:40:00', '2021/03/17 20:00:00', '2021/03/19 20:00:00', '2021/03/21 20:00:00', '2021/03/23 20:00:00', '2021/03/25 20:00:00', '2021/03/27 20:00:00', '2021/03/29 20:00:00', '2021/03/31 20:00:00']

dateTimeList_2 = ['2021/03/16 20:00:00', '2021/03/18 20:00:00', '2021/03/20 20:00:00', '2021/03/22 20:00:00', '2021/03/24 20:00:00', '2021/03/26 20:00:00', '2021/03/28 20:00:00', '2021/03/30 20:00:00']


bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


bot.command()
async def ping(ctx):
    await ctx.send('pong')


async def SendMessage_1():
    await channel.send('@everyone\n本日のギルドマイレージは\n【パターン２】\n闘技場へ１回入場\n闘技場へ２回入場\n薬草を５回採集する\n石を５回採鉱する\n木を５回伐採する\n古代遺跡１０回完了')


async def SendMessage_2():
    await channel.send('@everyone\n本日のギルドマイレージは\n【パターン１】\nラモー戦場１回入場（ヴォルクス）\nラモー戦場１回入場（黒結晶）\nラモー戦場２回入場（ヴォルクス）\nラモー戦場２回入場（黒結晶）\n古代遺跡５回完了\n古代遺跡１５回完了')

bot.run(token)

tasks.loop(seconds=1)
async def time_check_1():

    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    if now in dateTimeList_1:
        print(now)
        await SendMessage_1()

        await time.sleep(10)

tasks.loop(seconds=1)
async def time_check_2():

    now = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    if now in dateTimeList_2:
        print(now)
        await SendMessage_2()

        await time.sleep(87900)

asyncio.run(time_check_1())
asyncio.run(time_check_2())
        
tasks.loop.start()

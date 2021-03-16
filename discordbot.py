from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime
import asyncio

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channel = ("820269526733160451")


dateTimeList = ['2021/03/17 20:00', '2021/03/19 20:00', '2021/03/21 20:00', '2021/03/23 20:00', '2021/03/25 20:00', '2021/03/27 20:00', '2021/03/29 20:00', '2021/03/31 20:00', '2021/03/16 23:25', '2021/03/18 20:00', '2021/03/20 20:00', '2021/03/22 20:00', '2021/03/24 20:00', '2021/03/26 20:00', '2021/03/28 20:00', '2021/03/30 20:00']


bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


bot.run(token)

tasks.loop(seconds=5)
async def time_check():

    now = datetime.now().strftime('%Y/%m/%d %H:%M')


    if now in dateTimeList:
        if datetime.now().day % 2 == 0:

            print(now)
            channel.send('@everyone\n本日のギルドマイレージは\n【パターン１】\nラモー戦場１回入場（ヴォルクス）\nラモー戦場１回入場（黒結晶）\nラモー戦場２回入場（ヴォルクス）\nラモー戦場２回入場（黒結晶）\n古代遺跡５回完了\n古代遺跡１５回完了')
            await asyncio.sleep(60)
        else:
            print(now)
            channel.send('@everyone\n本日のギルドマイレージは\n【パターン２】\n闘技場へ１回入場\n闘技場へ２回入場\n薬草を５回採集する\n石を５回採鉱する\n木を５回伐採する\n古代遺跡１０回完了')
            await asyncio.sleep(60)
    else:
        return

asyncio.run(time_check())

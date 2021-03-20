from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime
import asyncio
import discord

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

# UTC
dateTimeList = ['2021/03/18 11:45', '2021/03/19 11:00', '2021/03/21 11:00', '2021/03/23 11:00', '2021/03/25 11:00', '2021/03/27 11:00', '2021/03/29 11:00', '2021/03/31 11:00', '2021/03/18 11:00', '2021/03/20 11:00', '2021/03/22 11:00', '2021/03/24 11:00', '2021/03/26 11:00', '2021/03/28 11:00', '2021/03/30 11:00']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@tasks.loop(seconds=30)
async def time_check():

    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    channel = bot.get_channel(639384765962649601)
    role = discord.utils.find(lambda r: r.name == 'Slaughter', channel.guild.roles)

    if now in dateTimeList:
        print("loopcheck2")
        if datetime.now().day % 2 == 0:

            print(now)
            await channel.send(role.mention + '\n本日のギルドマイレージは\n【パターン１】\nラモー戦場１回入場（ヴォルクス）\nラモー戦場１回入場（黒結晶）\nラモー戦場２回入場（ヴォルクス）\nラモー戦場２回入場（黒結晶）\n古代遺跡５回完了\n古代遺跡１５回完了')
            await asyncio.sleep(60)
        else:
            print(now)
            await channel.send(role.mention + '\n本日のギルドマイレージは\n【パターン２】\n闘技場へ１回入場\n闘技場へ２回入場\n薬草を５回採集する\n石を５回採鉱する\n木を５回伐採する\n古代遺跡１０回完了')
            await asyncio.sleep(60)

time_check.start()
bot.run(token)

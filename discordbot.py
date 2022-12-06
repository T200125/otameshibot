from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime
import asyncio
import discord

prefix = '*$'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), case_insensitive=True, self_bot=True)
token = os.environ['DISCORD_BOT_TOKEN']
channel_id = 1048971317875048489

# UTC
dateTimeList = ['05']

text_channel_list = []
for guild in bot.guilds:
    for channel in guild.channels:
        text_channel_list.append(channel)

print(text_channel_list)

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


async def channelid():
    await bot.fetch_channel(channel_id)
    yield

@tasks.loop(seconds=10)
async def time_check():

    check = datetime.now().strftime('%H')
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    channel = channelid()
    print(channel)

    if check in dateTimeList:
        print("loopcheck2")
        if datetime.now().day % 2 == 0:
            print(now)
            await channel.send('@everyone\n本日のギルドマイレージは\n薬草を５回採集する\n石を５回採鉱する\n木を５回伐採する\n古代遺跡５回完了\n古代遺跡１０回完了\n古代遺跡１５回完了')
            print('message sent')
            await asyncio.sleep(60)

asyncio.run(time_check())
bot.run(token)

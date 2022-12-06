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
channel_id = 599260116612808724

# UTC
dateTimeList = ['06']

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

@tasks.loop(seconds=10)
async def time_check():

    check = datetime.now().strftime('%H')
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    print(now)
    channel = bot.get_channel('channelid')

    if check in dateTimeList:
        print("loopcheck2")
        if datetime.now().day % 2 == 0:
            print(now)
            channel.send('test')
            print('message sent')
            await asyncio.sleep(600)

asyncio.run(time_check())
bot.run(token)

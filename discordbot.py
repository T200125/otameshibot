from discord.ext import commands
import os
import traceback
from discord.ext import tasks
import asyncio
import discord

prefix = '*$'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all(), case_insensitive=True, self_bot=True)
token = os.environ['DISCORD_BOT_TOKEN']

# UTC
dateTimeList = ['11:00']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@tasks.loop(seconds=10)
async def time_check():

    for guild in client.guilds:
        for channel in guild.channels:
            print(guild, channel)

await asyncio.sleep(100)

asyncio.run(time_check())
bot.run(token)

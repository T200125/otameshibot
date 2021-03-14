from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channel = os.environ['CHANNEL_ID']
client = discord.Client()


dateTimeList_1 = [
'2021/03/15 20:00',
'2021/03/17 20:00',
'2021/03/19 20:00',
'2021/03/21 20:00',
'2021/03/23 20:00',
'2021/03/25 20:00',
'2021/03/27 20:00',
'2021/03/29 20:00',
'2021/03/31 20:00'
]


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')



bot.run(token)

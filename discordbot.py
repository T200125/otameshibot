from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
channel = os.environ['CHANNEL_ID']


dateTimeList1 = [
'2021/03/14 14:53',
'2021/03/16 20:00',
'2021/03/18 20:00',
'2021/03/20 20:00',
'2021/03/22 20:00',
'2021/03/24 20:00',
'2021/03/26 20:00', 
'2021/03/28 20:00',
'2021/03/30 20:00',
]

dateTimeList2 = [
'2021/03/15 20:00',
'2021/03/17 20:00',
'2021/03/19 20:00',
'2021/03/21 20:00',
'2021/03/23 20:00',
'2021/03/25 20:00',
'2021/03/27 20:00', 
'2021/03/29 20:00',
'2021/03/31 20:00',
]

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@tasks.loop(seconds=60)
async def time_check():
    sleepTime = 0
    # 現在の時刻
    now = datetime.now().strftime('%Y/%m/%d %H:%M')
    if now in dateTimeList1 :
        print(now)
        await channel.send('本日のギルドマイレージは\n【パターン１】\nラモー戦場１回入場（ヴォルクス）\nラモー戦場１回入場（黒結晶）\nラモー戦場２回入場（ヴォルクス）\nラモー戦場２回入場（黒結晶）\n古代遺跡５回完了\n古代遺跡１５回完了')


#ループ処理実行
loop.start()

bot.run(token)

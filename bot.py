from email.policy import default
from math import perm
from multiprocessing import context
from random import Random, random, sample
from telnetlib import SEND_URL
from unittest import result
import hikari
import lightbulb
import random
import os
from dotenv import load_dotenv

load_dotenv()

bot = lightbulb.BotApp(
    token = os.getenv("DISCORD_TOKEN"),
    default_enabled_guilds=
    (
    707938586988642376, 
    965307477698707506, 
    767743597809500160, 
    134028939764039681,
    )
)



@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent):
    if isinstance(event.exception, lightbulb.CommandIsOnCooldown): 
        await event.context.respond(f"Hey, dont spam! <:mayagun:978841590644752464>", flags=hikari.MessageFlag.EPHEMERAL)
    if isinstance(event.exception, lightbulb.MaxConcurrencyLimitReached):
        await event.context.respond(f"You're trying to run too many commands at the same time! <:mayagun:978841590644752464>", flags=hikari.MessageFlag.EPHEMERAL)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started!')

Greeting_list = (
    "Im awake! <:mayamad:769351954685231144>",
    "<a:Mayapeek:984626950825996389>",
    "Good morning! <a:MayaWaveLeft:963294293777338399>",
    "Good morning~ <:mayasleepy:963562283219427389>",
    "I dont wanna get up! <a:MayaTantrum:852257288630566952>",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('ping', 'check if maya is awake!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond(random.choice(Greeting_list))



Maya_list = (
    "https://imgur.com/a/5BCZbU6",
    "https://imgur.com/a/3eBuE73",
    "https://imgur.com/a/k4XJV5M",
    "https://imgur.com/a/yYDLbqj",
    "https://imgur.com/a/9BFjAjl",
    "https://imgur.com/KW9Q9Mm",
    "https://imgur.com/a/HqcTUCg",
    "https://imgur.com/a/CdCkFr0",
    "https://imgur.com/a/WXCR5zV",
    "https://imgur.com/a/DS84qv4",
    "https://imgur.com/a/EvZ1b0m",
    "https://imgur.com/a/irFHIDK",
    "https://imgur.com/a/NyIPM4R",
    "https://imgur.com/a/BNLsC5r",
    "https://imgur.com/a/dFw597F",
    "https://imgur.com/a/dbYVa4Q",
    "https://imgur.com/a/aCcqucN",
    "https://imgur.com/a/Kq6TNC0",
    "https://imgur.com/a/zDPyggR",
    "https://imgur.com/a/hz3Pern",
    "<:Mayaya:853546054951501847> You got the rare **Rainbow Maya!** https://imgur.com/a/2tLSihF",
    "https://imgur.com/a/T6xsgZR",
    "https://imgur.com/a/FaMSgzs",
    "https://imgur.com/a/wtNvfUX",
    "https://imgur.com/a/DRzgfKF",
    "https://imgur.com/a/hobDGt0",
    "https://imgur.com/a/8bq9DF0",
    "https://imgur.com/a/4nzTh5A",
    "https://imgur.com/a/pUcXGrY",
    "https://imgur.com/a/5eBptvR",
    "https://imgur.com/a/flvnl5G",
    )

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('maya', 'provides an adorable maya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def maya(ctx):
    await ctx.respond(random.choice(Maya_list))



Megu_list = (
    "https://imgur.com/a/z1qwl9E",
    "https://imgur.com/a/GqD3XhJ",
    "https://imgur.com/a/xU8hRFF",
    "https://imgur.com/a/0RQIsK1",
    "https://imgur.com/a/se3CwbZ",
    "https://imgur.com/a/QPcUvPo",
    "https://imgur.com/a/pvSEMY9",
    "https://imgur.com/a/5haYKhL",
    "https://imgur.com/a/7drA2yE",
    "https://imgur.com/a/RnvmedE",
    "https://imgur.com/a/7uJCZ2G",
    "https://imgur.com/a/01iQRwr",
    "https://imgur.com/a/f7XuoCZ",
    "https://imgur.com/a/XwBJI37",
    "https://imgur.com/a/gTks9ZN",
    "https://imgur.com/a/GyGU97d",
    "https://imgur.com/a/w2iRZN5",
    "https://imgur.com/a/hu0VihG",
    "https://imgur.com/a/4nzTh5A",
    "https://imgur.com/a/0QEZ2F7",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('megu', 'provides an adorable megu image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def megu(ctx):
    await ctx.respond(random.choice(Megu_list))



Chino_list = (
    "https://imgur.com/a/6cqBEWq",
    "https://imgur.com/a/tEIgGw9",
    "https://imgur.com/a/Kjo9OXN",
    "https://imgur.com/a/MIonahM",
    "https://imgur.com/a/XLuDsVo",
    "https://imgur.com/a/AW8lRNW",
    "https://imgur.com/a/Ai3nD70",
    "https://imgur.com/a/uikfBd9",
    "https://imgur.com/a/QXIuY8F",
    "https://imgur.com/a/JdHjJS7",
    "https://imgur.com/a/XTQAumA",
    "https://imgur.com/a/y1xyhMH",
    "https://imgur.com/a/AV4ESDK",
    "https://imgur.com/a/5CiDTfT",
    "https://imgur.com/a/8zBwhQm",
    "https://imgur.com/a/XJENwHW",
    "https://imgur.com/a/AdpkkdQ",
    "https://imgur.com/a/ymUT5W8",
    "https://imgur.com/a/IomSPJJ",
    "https://imgur.com/a/IS9tGSI",
    "https://imgur.com/a/H6qTR2s",
    "https://imgur.com/a/wQG96Co",
    "https://imgur.com/a/zxR9P69",
    "https://imgur.com/a/qaIquS1",
    "https://imgur.com/a/tSY1Nao",
    "https://imgur.com/a/YKrcnpu",
    "https://imgur.com/a/hkQOZfb",
    "https://imgur.com/a/vw8Ajr1",
    "https://imgur.com/a/xpdwQfv",
    "https://imgur.com/a/6EnAEiV",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chino', 'provides an adorable chino image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chino(ctx):
    await ctx.respond(random.choice(Chino_list))
    


Chimame_list = (
    "https://imgur.com/a/G05Z4zI",
    "https://imgur.com/a/VwznUqY",
    "https://imgur.com/a/l9Vt9hm",
    "https://imgur.com/a/5uvsrNI",
    "https://imgur.com/a/z6zyizP",
    "https://imgur.com/a/DZP80ef",
    "https://imgur.com/a/HdmLapI",
    "https://twitter.com/mozukun43/status/1314877808246575106",
    "https://imgur.com/a/43PXfyu",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chimame', 'provides an adorable chimame image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chimame(ctx):
    await ctx.respond(random.choice(Chimame_list))



Cocoa_list = (
    "https://imgur.com/a/lFRRdjg",
    "https://imgur.com/a/fisXPfp",
    "https://imgur.com/a/XTlucbx",
    "https://imgur.com/a/FNBgnIo",
    "https://imgur.com/a/zHR70hV",
    "https://imgur.com/a/Hbk5MTr",
    "https://imgur.com/a/Aomv8cQ",
    "https://imgur.com/a/QgauP2Z",
    "https://imgur.com/a/SWYqfeI",
    "https://imgur.com/a/PJnw7OK",
    "https://imgur.com/a/OEk7kbn",
    "https://imgur.com/a/6gCOTeT",
    "https://imgur.com/a/NRtPPwO",
    "https://imgur.com/a/KCfW6tL",
    "https://imgur.com/a/Btg6djp",
    "https://imgur.com/a/B2kfIwk",
    "https://imgur.com/a/BUeZdlS",
    "https://imgur.com/a/uKRcesl",
    "https://imgur.com/a/CMbUTbB",
    "https://imgur.com/a/1SeAp3g",
    "https://imgur.com/a/uPY7lhx",
    "https://imgur.com/a/kOBBw8r",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('cocoa', 'provides an adorable cocoa image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cocoa(ctx):
    await ctx.respond(random.choice(Cocoa_list))



Rize_list = (
    "https://imgur.com/a/ECLvtE3",
    "https://imgur.com/a/ScpMpBY",
    "https://imgur.com/a/Qpc0xSB",
    "https://imgur.com/a/9jflDSd",
    "https://imgur.com/a/zndxii3",
    "https://imgur.com/a/Qo0fdYu",
    "https://imgur.com/a/Q9dRgbv",
    "https://imgur.com/a/3j79cAm",
    "https://imgur.com/a/dIcjHsl",
    "https://imgur.com/a/GdKMm7t",
    "https://imgur.com/a/dXeZY8c",
    "https://imgur.com/a/uV4bVZF",
    "https://imgur.com/a/WGGqnUh",
    "https://imgur.com/a/I4UCK1X",
    "https://imgur.com/a/gA44Xon",
    "https://imgur.com/a/lJKB5Qo",
    "https://imgur.com/a/oQm65ua",
    "https://imgur.com/a/U2CHvQ4",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('rize', 'provides an adorable rize image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def rize(ctx):
    await ctx.respond(random.choice(Rize_list))



Syaro_list = (
    "https://imgur.com/a/Q9dRgbv",
    "https://imgur.com/a/2K8D2kP",
    "https://imgur.com/a/5ZQNxbw",
    "https://imgur.com/a/nbPmNNG",
    "https://imgur.com/a/kPNTX2v",
    "https://imgur.com/a/Dsh0Dyb",
    "https://imgur.com/a/j7AxQ9F",
    "https://imgur.com/a/0gXpjHe",
    "https://imgur.com/a/Djgd0xu",
    "https://imgur.com/a/7KlwBaR",
    "https://imgur.com/a/94p3d9S",
    "https://imgur.com/a/ocM4oZr",
    "https://imgur.com/a/bz5TuUn",
    "https://imgur.com/a/BFUK4wB",
    "https://imgur.com/a/IWkdws2",
    "https://imgur.com/a/zMUqKCy",
    "https://imgur.com/a/7vheXL8",
    "https://imgur.com/a/1yBcFiw",
    "https://imgur.com/a/5gsEEos",
    "https://imgur.com/a/srUXXka",
    "https://imgur.com/a/hkQOZfb",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('syaro', 'provides an adorable syaro image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def syaro(ctx):
    await ctx.respond(random.choice(Syaro_list))



Chiya_list = (
    "https://imgur.com/a/PBFUaPd",
    "https://imgur.com/a/EPrx3Y7",
    "https://imgur.com/a/mBrdyLp",
    "https://imgur.com/a/pzE6Qdu",
    "https://imgur.com/a/DDEpZhO",
    "https://imgur.com/a/LoC8SKp",
    "https://imgur.com/a/C11kaVW",
    "https://imgur.com/a/MPmTheX",
    "https://imgur.com/a/wQG96Co",
    "https://imgur.com/a/SvX5QqJ",
    "https://imgur.com/a/r7fqXba",
    "https://imgur.com/a/R9eHyXG",
    "https://imgur.com/a/0aKAX2p",
    "https://imgur.com/a/GEuYag7",
    "https://imgur.com/a/IJSYspj",
    "https://imgur.com/a/sBaeqWE",
    "https://imgur.com/a/s5gXkC3",
    "https://imgur.com/a/NovbC60",
    "https://imgur.com/a/eKeiL8B",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chiya', 'provides an adorable chiya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chiya(ctx):
    await ctx.respond(random.choice(Chiya_list))



@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('patmaya', 'pats maya!')
@lightbulb.implements(lightbulb.SlashCommand)
async def patmaya(ctx):
    await ctx.respond('<a:mayapat1:855215364370595840>')



@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('patmegu', 'pats megu!')
@lightbulb.implements(lightbulb.SlashCommand)
async def patmegu(ctx):
    await ctx.respond('<a:MeguPat:904726832027422720>')



@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('patchino', 'pats chino!')
@lightbulb.implements(lightbulb.SlashCommand)
async def patchino(ctx):
    await ctx.respond('<a:patchino:997143091175751791>')



cqc_list = (
    "I-is this CQC?! <:MayaShock:804760846068744252>",
    "I can do CQC and stuff too! <:MayaSmug:741219402363437076>",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('cqc', 'Use CQC!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cqc(ctx):
    await ctx.respond(random.choice(cqc_list))

bot.run()
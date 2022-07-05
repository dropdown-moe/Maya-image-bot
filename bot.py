from random import Random, random, sample
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

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started!')

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("pong!")

Maya_list = (
        "https://imgur.com/a/5BCZbU6",
        "https://imgur.com/a/HdmLapI",
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

    )


@bot.command
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
)


@bot.command
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
)

@bot.command
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
    "https://twitter.com/mozukun43/status/1314877808246575106",
)

@bot.command
@lightbulb.command('chimame', 'provides an adorable chimame image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chimame(ctx):
    await ctx.respond(random.choice(Chimame_list))

bot.run()
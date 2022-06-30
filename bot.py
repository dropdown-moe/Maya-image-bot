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
    default_enabled_guilds=(707938586988642376, 965307477698707506, 767743597809500160)
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started!')

@bot.command
@lightbulb.command('ping', 'Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond("pong!")

original_list = (
        "https://imgur.com/a/5BCZbU6",
        "https://imgur.com/a/HdmLapI",
        "https://imgur.com/a/3eBuE73",
        "https://imgur.com/a/VwznUqY",
        "https://imgur.com/a/G05Z4zI",
        "https://imgur.com/a/k4XJV5M",
        "https://imgur.com/a/yYDLbqj",
        "https://imgur.com/a/9BFjAjl",
        "https://imgur.com/KW9Q9Mm",
        "https://imgur.com/a/5uvsrNI",
        "https://imgur.com/a/l9Vt9hm",
        "https://imgur.com/a/z6zyizP",
        "https://imgur.com/a/HqcTUCg",
        "https://imgur.com/a/CdCkFr0",
        "https://imgur.com/a/WXCR5zV",
        "https://imgur.com/a/DS84qv4",
        "https://imgur.com/a/EvZ1b0m",
        "https://imgur.com/a/DZP80ef",
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
    await ctx.respond(random.choice(original_list))

bot.run()
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
    default_enabled_guilds=(707938586988642376, 965307477698707506)
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
    )


@bot.command
@lightbulb.command('maya', 'provides an adorable maya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def maya(ctx):
    await ctx.respond(random.choice(original_list))

bot.run()
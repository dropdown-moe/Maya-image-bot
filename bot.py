from random import Random, random, sample
from multiprocessing import context
from email.policy import default
from secrets import choice
from dotenv import load_dotenv
from telnetlib import SEND_URL
from unittest import result
from math import perm
import lightbulb
import listodata
import hikari
import random
import os

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



banned_users_list = (
    
)

@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent):
    if isinstance(event.exception, lightbulb.CommandIsOnCooldown): 
        await event.context.respond(f"Command is on cooldown.", flags=hikari.MessageFlag.EPHEMERAL)
        print("Command cooldown error")
    if isinstance(event.exception, lightbulb.MaxConcurrencyLimitReached):
        await event.context.respond(
            f"Too many commands running at the same time! <:MayaHowRude:798609231393587240>", flags=hikari.MessageFlag.EPHEMERAL
            )
        print("Concurrency limit reached")

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started!')

# Greetings
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('ping', 'check if maya is awake!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Greeting_list))
    print("Ping command invoked")

# Maya
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('maya', 'provides an adorable maya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def maya(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Maya_list))
    print("Maya command invoked")

# Megu
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('megu', 'provides an adorable megu image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def megu(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Megu_list))
    print("Megu command invoked")

# Chino
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chino', 'provides an adorable chino image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chino(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Chino_list))
    print("Chino command invoked")

# Chimame
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chimame', 'provides an adorable chimame image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chimame(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Chimame_list))
    print("Chimame command invoked")

# Cocoa
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('cocoa', 'provides an adorable cocoa image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cocoa(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Cocoa_list))
    print("Cocoa command invoked")

# Rize
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('rize', 'provides an adorable rize image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def rize(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Rize_list))
    print("Rize command invoked")

# Syaro
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('syaro', 'provides an adorable syaro image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def syaro(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Syaro_list))
    print("Syaro command invoked")

# Chiya
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chiya', 'provides an adorable chiya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chiya(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Chiya_list))
    print("Chiya command invoked")

# CQC
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('cqc', 'Use CQC!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cqc(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.cqc_list))
    print("CQC command invoked")

# Fuyu
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('fuyu', 'provides an adorable fuyu image! (mostly manga stuff)')
@lightbulb.implements(lightbulb.SlashCommand)
async def fuyu(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    await ctx.respond(random.choice(listodata.Fuyu_list))
    print("Fuyu command invoked")

# i tried to get all the list stuff and such into listodata
# but it didnt seem to work so unless you have some magic trick dont try to move it
RPS_response_list = (
    "Rock",
    "Paper",
    "Scissors",
)

@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.UserBucket)
@lightbulb.decorators.option("choice", "your play", choices = ("Rock", "Paper", "Scissors"), required=True)
@lightbulb.command('rps', 'Play Rock Paper Scissors with Maya!',)
@lightbulb.implements(lightbulb.SlashCommand)
async def rps(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    bot_choice = random.choice(RPS_response_list)
    print("RPS command invoked")
    
    if ctx.options.choice == bot_choice:
        await ctx.respond(f"{bot_choice}, Its a tie... <:mayaded:787784902602129419>")
        return
    
    win = (
    ctx.options.choice == "Rock" and bot_choice == "Scissors" or
    ctx.options.choice == "Paper" and bot_choice == "Rock" or
    ctx.options.choice == "Scissors" and bot_choice == "Paper"
)
    if win:
        await ctx.respond(f"{bot_choice}... Ah, no fair!!! <a:MayaTantrum:852257288630566952>")
    else:
        await ctx.respond(f"{bot_choice}, I won! better luck next time! <:MayaSmug:741219402363437076>")
        print("someone just got owned by maya")
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.option("choice", "What you want maya to rate.", required=True)
@lightbulb.command('rate', 'Make Maya rate something!')
@lightbulb.implements(lightbulb.SlashCommand)
async def rate(ctx):
    if ctx.author.id in (banned_users_list):
        await ctx.respond("`You are banned from using commands.`", flags=hikari.MessageFlag.EPHEMERAL)
        return
    print("Rate command invoked")
    
    if ctx.options.choice in (
        "@everyone", "@Everyone"
        ):
        await ctx.respond(
            "Nice try bucko <a:MayaTssk:1000491767650582539>", flags=hikari.MessageFlag.EPHEMERAL
            )
        return

    if ctx.options.choice in (
        "Maya", "maya", "Maya Jouga", "maya jouga", "Jouga Maya", "jouga maya", "Myself", "myself", "me", "me"
        ):
        await ctx.respond(
            "Ehh Myself? uhhh, I dont know. <:MayaLaugh:981702800562073600>"
            )
        return

    if ctx.options.choice in (
        "Megu", "megu", "Megumi Natsu", "megumi natsu", "Natsu Megumi", "natsu megumi"
        ):
        await ctx.respond(
            "Megu? We've been best friends since we were both little. <:MayaLaugh:981702800562073600>"
            )
        return

    if ctx.options.choice in (
        "Chino", "chino", "Chino Kafuu", "chino kafuu", "Kafuu Chino", "kafuu chino"
        ):
        await ctx.respond(
            "Chino? Shes a bit quiet but a friend nontheless! <:MayaSalute:741219403118674000>"
            )
        return

    if ctx.options.choice in (
        "Rize", "rize", "Rize Tedeza", "rize tedeza", "Tedeza Rize", "tedeza rize"
        ):
        await ctx.respond(
            "Rize? She's super cool! She knows CQC and stuff! <:MayaSugoi:741219402770546759>"
            )
        return
    if ctx.options.choice in (
        "Cocoa", "cocoa", "Cocoa Hoto", "cocoa hoto", "Hoto Cocoa", "hoto cocoa"
    ):
        await ctx.respond(
            "Cocoa? She's a bit of an airhead but cool. <:MayaLaugh:981702800562073600>"
        )
        return

    if ctx.options.choice in (
        "Syaro", "syaro", "Syaro Kirima", "syaro kirima", "Kirima Syaro", "kirima syaro"
    ):
        await ctx.respond(
            "Syaro? She's super mature and responsible, cool... <:MayaSugoi:741219402770546759>"
        )
        return

    if ctx.options.choice in (
        "Chiya", "chiya", "Chiya Ujimatsu", "chiya ujimatsu", " Ujimatsu Chiya", "ujimatsu Chiya"
    ):
        await ctx.respond(
            "Chiya? She's kind of an airhead too but a fun person. <:mayasmirk:769351955565772822>"
        )
        return

    if ctx.options.choice in (
        "Tippy", "tippy"
    ):
        await ctx.respond(
            "Tippy? that's Chino's rabbit, i feel like i would get XP for defeating it! <:MayaXD:982772380902490132>"
        )
        return

    if ctx.options.choice in (
        "Fuyu", "fuyu", "Fuyu Fuiba", "fuyu fuiba", "Fuiba Fuyu", "fuiba fuyu"
    ):
        await ctx.respond(
        "Fuyu...? who? <:mayaded:787784902602129419>"
        )
        return
    
    if ctx.options.choice in (
        "Aoyama", "aoyama", 
        "Aoyama Midori", 
        "aoyama midori", 
        "Midori Aoyama", 
        "midori aoyama", 
        "Aoyama Blue Mountain", 
        "aoyama blue mountain"
    ):
        await ctx.respond(
            "Aoyama? I think Syaro told me about her, told me to be wary of her... <:mayaded:787784902602129419>"
            )
        return
    if ctx.options.choice in (
        "Anko", "anko"
    ):
        await ctx.respond(
            "Anko? that's Chiya's rabbit, he's a bit strage, apparently he pounces to attack whenever he sees Syaro <:mayaded:787784902602129419>"
        )
        return
    if ctx.options.choice in (
        "Wild Geese", "wild geese"
    ):
        await ctx.respond(
            "Wild Geese? that's Syaro's pet rabbit he's like the final boss after defeating Tippy! <:MayaSugoi:741219402770546759>"
        )
        return

    else: 
        await ctx.respond(f"I rate {ctx.options.choice} {random.choice(range(1, 11))}/10 <:mayasmirk:769351955565772822>")

bot.run()

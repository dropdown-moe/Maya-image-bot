# Support server https://discord.gg/bYMjhdADc6
# If you ever have any questions feel free to ask in the #bot-questions channel

from random import Random, random, sample
from multiprocessing import context
from email.policy import default
from secrets import choice
from urllib import response
from dotenv import load_dotenv
from telnetlib import SEND_URL
from unittest import result
from math import perm
from tinydb import TinyDB, Query
from tinydb.operations import add, increment 
import tinydb
import lightbulb
import listodata
import hikari
import random
import os
import json
import math
import chatbot
import bannedusers

db = TinyDB("db.json")
# This defines the database i use

load_dotenv()

bot = lightbulb.BotApp(
    token = os.getenv("DISCORD_TOKEN"),
    default_enabled_guilds=
    (
    707938586988642376, 
    965307477698707506, 
    767743597809500160, 
    134028939764039681,
    1001491591623606373,
    )
)
# These are server ID's for servers that commands work in, if a servers ID is not this this list commands will not work in it

@bot.listen(lightbulb.CommandErrorEvent)
async def on_error(event: lightbulb.CommandErrorEvent):
    if isinstance(event.exception, lightbulb.CommandIsOnCooldown): 
        print("command cooldown error")
        await event.context.respond(f"Oi, Don't spam! <:mayagun:978841590644752464>", flags=hikari.MessageFlag.EPHEMERAL)
        # This is an error condition that triggers if a person tries to send too many commands too quickly
    if isinstance(event.exception, lightbulb.MaxConcurrencyLimitReached):
        print("Concurrency limit reached")
        await event.context.respond(
            f"Too many commands running at the same time! <:MayaHowRude:798609231393587240>", flags=hikari.MessageFlag.EPHEMERAL
            )
        # This is an error condition that triggers if too many commands are trying to run at the same time
    if isinstance(event.exception, lightbulb.CheckFailure):
        await event.context.respond(f"This command is restricted to the dev only for now", flags=hikari.MessageFlag.EPHEMERAL)
        # this is an error condition that triggers if certain checks arent met, i am only using it to restrict certain commands to only myself for now
@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('bot has started!')
    # This just prints that the bot has started
# Greetings
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
# This sets how many instances of this command can run at the same time, if 2 people use this command at the same time one will return an error
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
# This sets the length of the cooldown and how many times a command has to be used for the cooldown to trigger
# The bucket represents on what basis the cooldown is applied, this one is applied on a server basis
@lightbulb.command('poke', 'check if maya is awake! (use as ping command)')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return
    # This checks if the user ID of whoever invoked the command is in a banned users file i have,
    # if it is then command will reply with an ephemeral error message instead of the normal response

    data = Query()
    if db.search(data.commandname == "ping"):
        # This Queries my database for a command called 'ping'
        db.update(increment("count"), data.commandname == "ping")
        # This increments the counter attached to the ping command by 1
        print("Ping command invoked")
        await ctx.respond("Oi, stop that! <:MayaBlech:741219402124492840>")
        return
        # This represents what the bot will actually send in the channel
    else:
        db.insert({"type": "commandcounter", "commandname": "ping", "count":1})
        print("Ping command invoked")
        # If the above code doesn't find a instance of a Ping command in the database this code inserts said data,
        # this is redundant after the command has been invoked just once but i will keep the code just in case regardless
    await ctx.respond("Oi, stop that! <:MayaBlech:741219402124492840>")

# Maya
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('maya', 'provides an adorable maya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def maya(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "maya"):
        db.update(increment("count"), data.commandname == "maya")
        await ctx.respond(random.choice(listodata.Maya_list))
        print("Maya command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "maya", "count":1})
    await ctx.respond(random.choice(listodata.Maya_list))
    print("Maya command invoked")

# Megu
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('megu', 'provides an adorable megu image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def megu(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "megu"):
        db.update(increment("count"), data.commandname == "megu")
        await ctx.respond(random.choice(listodata.Megu_list))
        print("Megu command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "megu", "count":1})
    await ctx.respond(random.choice(listodata.Megu_list))
    print("Megu command invoked")

# Chino
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chino', 'provides an adorable chino image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chino(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "chino"):
        db.update(increment("count"), data.commandname == "chino")
        await ctx.respond(random.choice(listodata.Chino_list))
        print("Chino command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "chino", "count":1})
    await ctx.respond(random.choice(listodata.Chino_list))
    print("Chino command invoked")

# Chimame
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chimame', 'provides an adorable chimame image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chimame(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "chimame"):
        db.update(increment("count"), data.commandname == "chimame")
        await ctx.respond(random.choice(listodata.Chimame_list))
        print("Chimame command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "chimame", "count":1})
    await ctx.respond(random.choice(listodata.Chimame_list))
    print("Chimame command invoked")

# Cocoa
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('cocoa', 'provides an adorable cocoa image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def cocoa(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "cocoa"):
        db.update(increment("count"), data.commandname == "cocoa")
        await ctx.respond(random.choice(listodata.Cocoa_list))
        print("Cocoa command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "cocoa", "count":1})
    await ctx.respond(random.choice(listodata.Cocoa_list))
    print("Cocoa command invoked")

# Rize
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('rize', 'provides an adorable rize image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def rize(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "rize"):
        db.update(increment("count"), data.commandname == "rize")
        await ctx.respond(random.choice(listodata.Rize_list))
        print("Rize command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "rize", "count":1})
    await ctx.respond(random.choice(listodata.Rize_list))
    print("Rize command invoked")

# Syaro
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('syaro', 'provides an adorable syaro image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def syaro(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "syaro"):
        db.update(increment("count"), data.commandname == "syaro")
        await ctx.respond(random.choice(listodata.Syaro_list))
        print("Syaro command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "syaro", "count":1})
    await ctx.respond(random.choice(listodata.Syaro_list))
    print("Syaro command invoked")

# Chiya
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('chiya', 'provides an adorable chiya image!')
@lightbulb.implements(lightbulb.SlashCommand)
async def chiya(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "chiya"):
        db.update(increment("count"), data.commandname == "chiya")
        await ctx.respond(random.choice(listodata.Chiya_list))
        print("Chiya command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "chiya", "count":1})
    await ctx.respond(random.choice(listodata.Chiya_list))
    print("Chiya command invoked")

# Fuyu
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.GuildBucket)
@lightbulb.command('fuyu', 'provides an adorable fuyu image! (mostly manga stuff)')
@lightbulb.implements(lightbulb.SlashCommand)
async def fuyu(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    if db.search(data.commandname == "fuyu"):
        db.update(increment("count"), data.commandname == "fuyu")
        await ctx.respond(random.choice(listodata.Fuyu_list))
        print("Fuyu command invoked")
        return
    else:
        db.insert({"type": "commandcounter", "commandname": "fuyu", "count":1})
    await ctx.respond(random.choice(listodata.Fuyu_list))
    print("Fuyu command invoked")

# i tried to get all the list stuff and such into listodata
# but it didnt seem to work so unless you have some magic trick dont try to move it
RPS_response_list = (
    "Rock",
    "Paper",
    "Scissors",
)

# RPS
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=2, bucket=lightbulb.UserBucket)
@lightbulb.decorators.option("choice", "your play", choices = ("Rock", "Paper", "Scissors"), required=True)
# This is an option decorator which allow people to input something before sending the command
# The 'choices=' allows you to set specific options for the user to choose from, if this isnt added the user can input anything
@lightbulb.command('rps', 'Play Rock Paper Scissors with Maya!',)
@lightbulb.implements(lightbulb.SlashCommand)
async def rps(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are not allowed to use commands`", flags=hikari.MessageFlag.EPHEMERAL)
        return

    bot_choice = random.choice(RPS_response_list)
    print("RPS command invoked")
    
    if ctx.options.choice == bot_choice:
        data = Query()
        if db.search(data.condition == "tie"):
            db.update(increment("count"), data.condition == "tie")
            await ctx.respond(f"{bot_choice}, Its a tie... <:mayaded:787784902602129419>")
            return
        else:
            db.insert({"type": "rpscounter", "condition": "tie", "count":1})
        await ctx.respond(f"{bot_choice}, Its a tie... <:mayaded:787784902602129419>")
        return
        # This code checks if the bot's choice matches the Authors choice and sends the Tie response if it does

    win = (
    ctx.options.choice == "Rock" and bot_choice == "Scissors" or
    ctx.options.choice == "Paper" and bot_choice == "Rock" or
    ctx.options.choice == "Scissors" and bot_choice == "Paper"
    )
    # These are all the conditions for the Author winning
    if win:
        data = Query()
        if db.search(data.condition == "lose"):
            db.update(increment("count"), data.condition == "lose")
            await ctx.respond(f"{bot_choice}... Ah, no fair!!! <a:MayaTantrum:852257288630566952>")
            return
        else:
            db.insert({"type": "rpscounter", "condition": "lose", "count":1})
        await ctx.respond(f"{bot_choice}... Ah, no fair!!! <a:MayaTantrum:852257288630566952>")
        # if any of the win conditions are met this response will send   
    else:
        data = Query()
        if db.search(data.condition == "win"):
            db.update(increment("count"), data.condition == "win")
            await ctx.respond(f"{bot_choice}, I won! better luck next time! <:MayaSmug:741219402363437076>")
            return
        else:
            db.insert({"type": "rpscounter", "condition": "win", "count":1})
        await ctx.respond(f"{bot_choice}, I won! better luck next time! <:MayaSmug:741219402363437076>")
        print("someone just got owned by maya")
        # If none of the win conditions are met this response will send

# Rate
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.option("choice", "What you want maya to rate.", required=True)
@lightbulb.command('rate', 'Make Maya rate something!')
@lightbulb.implements(lightbulb.SlashCommand)
async def rate(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
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
        "Maya", "maya", "Maya Jouga", "maya jouga", "Jouga Maya", "jouga maya", "Myself", "myself", "Me", "me"
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
            "Anko? that's Chiya's rabbit, he's a bit strage, apparently he pounces to attack whenever he sees Syaro... <:mayaded:787784902602129419>"
        )
        return
    if ctx.options.choice in (
        "Wild Geese", "wild geese"
    ):
        await ctx.respond(
            "Wild Geese? that's Syaro's pet rabbit he's like the final boss after defeating Tippy! <:MayaSugoi:741219402770546759>"
        )
        return
    if ctx.options.choice in (
        "Chimame", "chimame", "Chimame Tai", "chimame tai"
    ):
        await ctx.respond(
            "I initially didn't like the name, but its grown on me since. <:mayasmirk:769351955565772822>"
        )
        return
    if ctx.options.choice in (
        "Takahiro", "takahiro", "Takahiro Kafuu", "takahiro kafuu", "Kafuu Takahiro", "kafuu takahiro"
    ):
        await ctx.respond(
            "Takahiro? That's Chino's Dad, Me and Megu interviewed him for a school project once. <:MayaXD:982772380902490132>"
        )
        return
    # All of the above code checks if the Authors choice contains certain words and if they do, sends a custom response
    else: 
        await ctx.respond(f"I rate {ctx.options.choice} {random.choice(range(1, 11))}/10 <:mayasmirk:769351955565772822>")
    # If none of the special responses are triggered this code takes whatever the authors input was and rates it a random number out of 10

# Chatbot, (This command is a work in progress)
# Most of the code here was contributed by contributors on the support discord
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=5, uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.option("choice", "what you want to say to maya. (WIP)", required=True)
@lightbulb.command('say', 'say something to maya')
@lightbulb.implements(lightbulb.SlashCommand)
async def say(ctx):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("`You are banned from using commands.`", flags=hikari.MessageFlag.EPHEMERAL)
        return
    x = ctx.options.choice.lower()
    # ctx.options.choice represents whatever the user input
    is_topic_exist = False
    # Boolean flag if topic exists

    def is_slice_in_list(s,l):
        len_s = len(s)
        return any(s == l[i:len_s+i] for i in range(len(l) - len_s+1))
    # This function checks if `s` is a sublist of 'l'

    for topic, values in chatbot.Q_POSB.items():
        for value in values:
            if (is_slice_in_list(value.split(), x.split())):
            # checks if `userInput' contains the words from 'value' (in order)
                is_topic_exist = True
                await ctx.respond(random.choice(chatbot.maya[topic]))
                break
        if is_topic_exist:
            break
            # break the loop as topic has been found
    if not is_topic_exist: 
        await ctx.respond("Ehh, I'm not sure how to respond. <:mayaded:787784902602129419>")
        # If the input doesn't match any topic

# Command usage
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=15, uses=1, bucket=lightbulb.UserBucket)
@lightbulb.command("usage", "display how many times each command has been used.")
@lightbulb.implements(lightbulb.SlashCommand)
async def usage(ctx: lightbulb.context):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("you are not allowed to use commands", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    db.search(data.commandname == "ping")
    command_name1 = db.get(data.commandname == "ping")
    command_count1 = command_name1["count"]
    
    data = Query()
    db.search(data.commandname == "maya")
    command_name2 = db.get(data.commandname == "maya")
    command_count2 = command_name2["count"]

    data = Query()
    db.search(data.commandname == "megu")
    command_name3 = db.get(data.commandname == "megu")
    command_count3 = command_name3["count"]
    
    data = Query()
    db.search(data.commandname == "chino")
    command_name4 = db.get(data.commandname == "chino")
    command_count4 = command_name4["count"]

    data = Query()
    db.search(data.commandname == "chimame")
    command_name5 = db.get(data.commandname == "chimame")
    command_count5 = command_name5["count"]

    data = Query()
    db.search(data.commandname == "cocoa")
    command_name6 = db.get(data.commandname == "cocoa")
    command_count6 = command_name6["count"]

    data = Query()
    db.search(data.commandname == "rize")
    command_name7 = db.get(data.commandname == "rize")
    command_count7 = command_name7["count"]

    data = Query()
    db.search(data.commandname == "syaro")
    command_name8 = db.get(data.commandname == "syaro")
    command_count8 = command_name8["count"]

    data = Query()
    db.search(data.commandname == "chiya")
    command_name9 = db.get(data.commandname == "chiya")
    command_count9 = command_name9["count"]

    data = Query()
    db.search(data.commandname == "fuyu")
    command_name10 = db.get(data.commandname == "fuyu")
    command_count10 = command_name10["count"]
    # The above code simply Retreives all the Count data from my database, there likely is a more efficient way of doing this that i am not aware of so feel free to improve it
    
    global message_channel_id
    embed = hikari.Embed(
    title = "Command usage list. <:mayawink:769351954929287219>",
    color = hikari.Color(616152),
    description = f"/poke `{command_count1}`\n/maya `{command_count2}`\n/megu `{command_count3}`\n/chino `{command_count4}`\n/chimame `{command_count5}`\n/cocoa `{command_count6}`\n/rize `{command_count7}`\n/syaro `{command_count8}`\n/chiya `{command_count9}`\n/fuyu `{command_count10}`")
    # The mess above just makes an embed

    await ctx.respond(embed=embed)

# RPS stats
@bot.command
@lightbulb.decorators.set_max_concurrency(uses=1, bucket=lightbulb.UserBucket)
@lightbulb.decorators.add_cooldown(length=15, uses=1, bucket=lightbulb.UserBucket)
@lightbulb.command("rpsstats", "Show RPS Stats.")
@lightbulb.implements(lightbulb.SlashCommand)
async def rpsstats(ctx: lightbulb.context):
    if ctx.author.id in (bannedusers.bannedusers):
        await ctx.respond("you are not allowed to use commands", flags=hikari.MessageFlag.EPHEMERAL)
        return

    data = Query()
    db.search(data.condition == "win")
    RPScondition1 = db.get(data.condition == "win")
    RPScounter1 = RPScondition1["count"]

    data = Query()
    db.search(data.condition == "tie")
    RPScondition2 = db.get(data.condition == "tie")
    RPScounter2 = RPScondition2["count"]

    data = Query()
    db.search(data.condition == "lose")
    RPScondition3 = db.get(data.condition == "lose")
    RPScounter3 = RPScondition3["count"]
    # Similarly to the Usage command this code simply gets all the count data for the RPS command
    global message_channel_id
    embed = hikari.Embed(
    title = "RPS Stats. <:mayawink:769351954929287219>",
    color = hikari.Color(616152),
    description = f"Maya has `{RPScounter1}` Wins in RPS\nMaya has `{RPScounter2}` Ties in RPS\nMaya has `{RPScounter3}` Losses in RPS")
    
    await ctx.respond(embed=embed)



bot.run(
    status=hikari.Status.ONLINE,
    activity=hikari.Activity(
        name="With Megu!",
        type=hikari.ActivityType.PLAYING,
    ),
)

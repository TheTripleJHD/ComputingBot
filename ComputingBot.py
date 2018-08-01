import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random
import re
import aiohttp


bot = commands.Bot(command_prefix="!", case_insensitive="true",)
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Bot is ready!")
    await bot.change_presence(
    activity=discord.Activity(name='What is love - Twice',type=discord.ActivityType.listening),status=discord.Status.online)
   
@bot.listen()
async def on_message(message):
     text = message.content.upper()
     text.split()
     if re.search(r'\b(da)?vid\b', text, re.I):
        await message.add_reaction('\N{SMILING FACE WITH HEART-SHAPED EYES}') 
        
@bot.listen()
async def on_message(message):
     text = message.content.upper()
     text.split()
     if re.search(r'\b(zinnia)\b', text, re.I):
        await message.add_reaction('\N{ANGRY FACE}')
        
@bot.listen()
async def on_message(message):
     text = message.content.upper()
     text.split()
     if re.search(r'\b(weng)\b', text, re.I) or re.search(r'\b(yulei)\b', text, re.I):
        await message.add_reaction('\N{WHITE RIGHT POINTING BACKHAND INDEX}')
        await message.add_reaction('\N{OK HAND SIGN}')
        await bot.say("Call me BIG")
        
@bot.command()
async def what(ctx):
    await ctx.send(":computer:")

@bot.command()
async def helpme(ctx):
    await ctx.send("List of helpful commands:")
    await ctx.send("!ping - What is your ping?")
    await ctx.send("!cute - Who is the cutest?")
    await ctx.send("!what - What is this discord all about?")
    await ctx.send("!say - Want me to say something?")
    await ctx.send("!gay - Check how gay you are!")
    await ctx.send("!love - Do you want some love?")
    await ctx.send("!rainbow - Rainboww!!")
    await ctx.send("!zinnia - Find out who she has traumatised")
    
@bot.command()
async def duck(ctx):
    num = round(random.uniform(0.00,100.00), 2)
    if num <= 50:
        url = "https://random-d.uk/api/v1/randomimg"
        async with aiohttp.request("GET", url) as f:   
            img = await f.read()
        await ctx.send(file=discord.File(img, "duck.png"))
    else:
        url = "https://random-d.uk/api/v1/randomgif"
        async with aiohttp.request("GET", url) as f:
            img = await f.read()
        await ctx.send(file=discord.File(img, "duck.gif"))

@bot.command()
async def ping(ctx):
    await ctx.send(ctx.author.mention + " Pong!")

@bot.command()
async def cute(ctx):
    await ctx.send("David is cute")
   
@bot.command()
async def zinnia(ctx):
    await ctx.send("Poor Gideon... :sob:")

@bot.command()
async def say(ctx, *, something):
    await ctx.send(something)

@bot.event
async def on_member_join(member):
    guild = member.guild
    await member.send("Welcome to {}!".format(guild.name))
    
@bot.command()
async def gay(ctx):
    name = str(ctx.author)
    num = round(random.uniform(0.00,100.00), 2)
    if name =='zinnia#8516':
        await ctx.send("Sorry but you're a girl. :3")
        await ctx.send("But if you were a guy you would be " + num + "% gay.")
    elif name =='ɥʇɹɐpᴉs#4852':
         await ctx.send("Sid is that even a question? :)")  
    elif num >= 95.00:
        start = " You are just gay kys."
        end = "% gay."
        text = start + end
        gay = " Estimated to be "
        text = start + gay + str(num) + end
        await ctx.send(ctx.author.mention + text)
      
    elif num >= 5.00 and num < 95.00:
        end = "% Gay."
        start = " You are "
        text = start + str(num) + end
        await ctx.send(ctx.author.mention + text)
        
    else:   
        start = " Lucky! "
        end = "You are only "
        gay = "% gay."
        text = start + end + str(num) + gay 
        await ctx.send(ctx.author.mention + text)
           
@bot.command()
async def rainbow(ctx):
    await ctx.message.add_reaction(emoji = "💙")
    await ctx.message.add_reaction(emoji = "💚")
    await ctx.message.add_reaction(emoji = "💛")
    await ctx.message.add_reaction(emoji = "💖")
    await ctx.message.add_reaction(emoji = "💜")
    await ctx.message.add_reaction(emoji = "🖤")
    
bot.run(os.getenv('TOKEN'))

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random


bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Bot is ready!")
    await bot.change_presence(
    activity=discord.Activity(name='What is love - Twice',type=discord.ActivityType.listening),status=discord.Status.online)
   
@bot.event
async def on_message(ctx):
    if ctx.message == 'vid':
        await ctx.message.add_reaction(emoji = "😍")
    

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
    num = round(random.uniform(0.00,100.00), 2)
    end = "% Gay."
    start = " You are "
    text = start + str(num) + end
    await ctx.send(ctx.author.mention + text)
    
@bot.command()
async def love(ctx):
    await ctx.message.add_reaction(emoji = "😍")
    
@bot.command()
async def rainbow(ctx):
    await ctx.message.add_reaction(emoji = "💙")
    await ctx.message.add_reaction(emoji = "💚")
    await ctx.message.add_reaction(emoji = "💛")
    await ctx.message.add_reaction(emoji = "💖")
    await ctx.message.add_reaction(emoji = "💜")
    await ctx.message.add_reaction(emoji = "🖤")

bot.run(os.getenv('TOKEN'))

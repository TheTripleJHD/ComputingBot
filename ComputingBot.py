import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import random
from random import *
import re
import aiohttp


bot = commands.Bot(command_prefix="~", case_insensitive="true",)
bot.remove_command('help')


@bot.event
async def on_ready():
    print("Bot is ready!")
    await bot.change_presence(
    activity=discord.Activity(name='Summoners-War',type=discord.ActivityType.playing),status=discord.Status.online)
   
@bot.listen()
async def on_message(message):
    if message.author != bot.user:
       text = message.content.upper()
       text.split()
       if re.search(r'\b(da)?vid\b', text, re.I):
           await message.add_reaction('\N{SMILING FACE WITH HEART-SHAPED EYES}') 
        
@bot.listen()
async def on_message(message):
     if message.author != bot.user:
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
        
@bot.listen()
async def on_message(message):
    if message.author != bot.user:
       text = message.content.upper()
       text.split()
       if re.search(r'\b(pur)?lem\b', text, re.I):
           await message.add_reaction('\N{SMILING FACE WITH HEART-SHAPED EYES}') 
        
@bot.command()
async def what(ctx):
    await ctx.send(":computer:")

@bot.command()
async def helpme(ctx):
    await ctx.author.send("```List of helpful commands:\n~ping - What is your ping?\n~summon - Summon a monster\n~cute - Who is the cutest?\n~what - What is this discord all about?\n~say - Want me to say something?\n~gay - Check how gay you are!\n~rainbow - Rainboww!!\n~zinnia - Find out who she has traumatised\n~doggo - Awww how cute are dogs?\n~ducc - Waddle waddle..\n~dicc - Big Dicc Energy checker```")
@bot.command()
async def doggo(ctx):
    num = randint(1,4)
    if num == 1:
        url = "http://loremflickr.com/1280/720/dog"   
    elif num == 2:
        url = "http://loremflickr.com/640/480/dog"
    else:
        url = "http://loremflickr.com/320/240/dog"
        
    async with aiohttp.request("GET", url) as f:   
        img = await f.read()
    await ctx.send(file=discord.File(img, "nofilter.jpg"))
    
@bot.command()
async def ducc(ctx):
    num = randint(0,100)
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
    num = round(uniform(0,100), 2)
    if name =='iced1#4281':
        text = " Darren you're soooo gay there is no number."
        await ctx.send(ctx.author.mention + text)
    elif name =='zinnia#8516':
        start = " But if you were a guy you would be "
        end = "% gay."
        text = start + str(num) + end
        await ctx.send("Sorry but you're a girl. :3")
        await ctx.send(ctx.author.mention + text)
    elif name =='!ɥʇɹɐpᴉs#4852':
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
async def dicc(ctx):
    name = str(ctx.author)
    num = randint(0,100)
    
    if name =='zinnia#8516':
        start = ' Oh wait you do, big dicc energy is currently at '
        end = "%."
        text = start + str(num) + end
        await ctx.send("Do you even have one?")
        await ctx.send(ctx.author.mention + text)
    elif num >= 80:
        text = ' Good job! Your big dicc energy exceeds past 80%'
        await ctx.send(ctx.author.mention + text)
    else:
        start = ' Sorry, but your big dicc energy is weak asf.'
        end = " Currently at " + str(num) + "%."
        text = start + end
        await ctx.send(ctx.author.mention + text)
    
    
           
@bot.command()
async def rainbow(ctx):
    await ctx.message.add_reaction(emoji = "💙")
    await ctx.message.add_reaction(emoji = "💚")
    await ctx.message.add_reaction(emoji = "💛")
    await ctx.message.add_reaction(emoji = "💖")
    await ctx.message.add_reaction(emoji = "💜")
    await ctx.message.add_reaction(emoji = "🖤")
    
@bot.command()
async def summon(ctx):
    await ctx.send("Summoning...")
    star = choices(population=[5, 4, 3], weights=[0.005, 0.08, 0.915], k=1)
    name = str(ctx.author)
    
    if name == 'Triple__J#8312':
        star[0] = 5
    
    if star[0] == 5:
        type = randint(1,3)
        
        if type == 1:
            fire = choices(population=['Valkyrja', 'Dragon', 'Pheonix', 'Chimera', 'Oracle', 'Occult Girl', 'Dragon Knight',
                                       'Monkey King', 'Archangel', 'Beast Monk' , 'Hell Lady', 'Pioneer', 'Polar Queen',
                                       'Ifruit', 'Sea Emperor', 'Dessert Queen', 'Fairy King', 'Unicorn',
                                       'Paladin', 'Druid'], k=1)
                           
            await ctx.send(ctx.author.mention + " You have summoned a fire " + fire[0] + "! :star::star::star::star::star:")
        elif type == 2:
            water = choices(population=['Valkyrja', 'Dragon', 'Chimera', 'Oracle', 'Occult Girl', 'Dragon Knight',
                                       'Monkey King', 'Archangel', 'Beast Monk' , 'Hell Lady', 'Pioneer', 'Polar Queen',
                                       'Sea Emperor', 'Dessert Queen', 'Fairy King', 'Panda Warrior', 'Unicorn',
                                       'Paladin', 'Druid', 'Lightning Emperor'], k=1)
                           
            await ctx.send(ctx.author.mention + " You have summoned a water " + water[0] + "! :star::star::star::star::star:") 
        else:
            wind = choices(population=['Dragon', 'Pheonix', 'Chimera', 'Oracle', 'Occult Girl', 'Dragon Knight',
                                       'Monkey King', 'Archangel', 'Beast Monk' , 'Hell Lady', 'Pioneer', 'Polar Queen',
                                       'Sea Emperor', 'Dessert Queen', 'Fairy King', 'Panda Warrior', 'Unicorn',
                                       'Paladin', 'Druid', 'Lightning Emperor'], k=1)
                           
            await ctx.send(ctx.author.mention + " You have summoned a wind " + wind[0] + "! :star::star::star::star::star:")
    elif star[0] == 4:
        type = randint(1,3)
        
        if type == 1:
            fire = choices(population=['Anubis', 'Assassin', 'Barbaric King', 'Boomerang Warrior', 'Brownie Magician',
                                      'Chakram Dancer', 'Death Knight', 'Dice Magician', 'Dryad',
                                      'Harp Magician', 'Horus', 'Jack-O-Lantern', 'Joker', 'Kobold Bomber', 'Kung Fu Girl'
                                      'Lich', 'Magic Knight', 'Mermaid', 'Neostone Agent', 'Neostone Fighter',
                                      'Nine-Tailed Fox', 'Ninja', 'Phantom Theif', 'Pierret', 'Pirate Captain',
                                      'Rakshasa', 'Samurai', 'Sky Dancer', 'Sniper MK.I', 'Succubus', 'Sylph',
                                      'Sylphid', 'Undine', 'Vampire', 'Epikion Priest'], k=1)
                           
            await ctx.send(ctx.author.mention + " You have summoned a fire " + fire[0] + "! :star::star::star::star:")
        elif type == 2:
            water = choices(population=['Anubis', 'Assassin', 'Barbaric King', 'Boomerang Warrior', 'Brownie Magician',
                                      'Chakram Dancer', 'Death Knight', 'Dice Magician', 'Dryad',
                                      'Harp Magician', 'Horus', 'Jack-O-Lantern', 'Joker', 'Kobold Bomber', 'Kung Fu Girl'
                                      'Lich', 'Magic Knight', 'Mermaid', 'Neostone Agent', 'Neostone Fighter',
                                      'Nine-Tailed Fox', 'Ninja', 'Phantom Theif', 'Pierret', 'Pirate Captain',
                                      'Rakshasa', 'Samurai', 'Sky Dancer', 'Sniper MK.I', 'Succubus', 'Sylph',
                                      'Sylphid', 'Undine', 'Vampire', 'Taoist'], k=1)
                           
            await ctx.send(ctx.author.mention + " You have summoned a water " + water[0] + "! :star::star::star::star:") 
        else:
            wind = choices(population=['Anubis', 'Assassin', 'Barbaric King', 'Boomerang Warrior', 'Brownie Magician',
                                      'Chakram Dancer', 'Death Knight', 'Dice Magician', 'Dryad', 'Giant Warrior',
                                      'Harp Magician', 'Horus', 'Jack-O-Lantern', 'Joker', 'Kobold Bomber', 'Kung Fu Girl'
                                      'Lich', 'Magic Knight', 'Mermaid', 'Neostone Agent', 'Neostone Fighter',
                                      'Nine-Tailed Fox', 'Ninja', 'Phantom Theif', 'Pierret', 'Pirate Captain',
                                      'Rakshasa', 'Samurai', 'Sky Dancer', 'Sniper MK.I', 'Succubus', 'Sylph',
                                      'Sylphid', 'Undine', 'Vampire', 'Taoist', 'Harg'], k=1)
                           
            await ctx.send(ctx.author.mention + " You have summoned a wind " + wind[0] + "! :star::star::star::star:")
    else:
        type = randint(1,3)
        
        if type == 1:
            fire = choices(population=['Fairy', 'Harpy', 'Inugami', 'Salamander', 'Serpent', 'Golem', 'Griffon', 'Inferno', 
                                      'High Elemental', 'Bearman', 'Werewolf', 'Viking', 'Amazon', 'Martial Cat', 
                                      'Vagabond', 'Magical Archer', 'Bounty Hunter', 'Imp Champion', 'Mystic Witch', 'Grim Reaper', 'Living Armor', 
                                      'Drunken Master', 'Minotauros', 'Lizardman', 'Taoist', 'Beast Hunter', 'Penguin Knight', 'Battle Mammoth',
                                      'Cow Girl', 'Charger Shark', 'Martial Artist', 'Mummy', 'Frankenstein', 'Elven Ranger', 'Harg', 'Giant Warrior'], k=1)  
            
            await ctx.send(ctx.author.mention + " You have summoned a fire " + fire[0] + "! :star::star::star:")
        elif type == 2:
            water = choices(population=['Fairy', 'Harpy', 'Inugami', 'Salamander', 'Serpent', 'Golem', 'Griffon', 'Inferno', 
                                      'High Elemental', 'Bearman', 'Werewolf', 'Viking', 'Amazon', 'Martial Cat', 'Epikion Priest', 
                                      'Vagabond', 'Magical Archer', 'Bounty Hunter', 'Imp Champion', 'Mystic Witch', 'Grim Reaper', 'Living Armor', 
                                      'Drunken Master', 'Minotauros', 'Lizardman', 'Beast Hunter', 'Penguin Knight', 'Battle Mammoth',
                                      'Cow Girl', 'Charger Shark', 'Martial Artist', 'Mummy', 'Frankenstein', 'Elven Ranger', 'Harg', 'Giant Warrior'], k=1)
                           
            await ctx.send(ctx.author.mention + " You have summoned a water " + water[0] + "! :star::star::star:") 
        else:
            wind = choices(population=['Fairy', 'Harpy', 'Inugami', 'Salamander', 'Serpent', 'Golem', 'Griffon', 'Inferno', 
                                      'High Elemental', 'Bearman', 'Werewolf', 'Viking', 'Amazon', 'Martial Cat', 'Epikion Priest', 
                                      'Vagabond', 'Magical Archer', 'Bounty Hunter', 'Imp Champion', 'Mystic Witch', 'Grim Reaper', 'Living Armor', 
                                      'Drunken Master', 'Minotauros', 'Lizardman', 'Beast Hunter', 'Penguin Knight', 'Battle Mammoth',
                                      'Cow Girl', 'Charger Shark', 'Martial Artist', 'Mummy', 'Frankenstein', 'Elven Ranger'], k=1)
                           
            await ctx.send(ctx.author.mention + " You have summoned a wind " + wind[0] + "! :star::star::star:")
            
@bot.command()
async def git(ctx):
    await ctx.send(ctx.author.mention + " " + "https://github.com/TheTripleJHD/ComputingBot/edit/master/ComputingBot.py")
    
        
                              
bot.run(os.getenv('TOKEN'))

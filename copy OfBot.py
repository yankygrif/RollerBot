import discord
from discord.ext import commands
import datetime
import random

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a RollerBot")

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)
    
@bot.command()
async def roll(ctx, string, bonus=0):
    if "d" in string:
        inf=string.split("d")
    elif "D" in string:
        inf=string.split("D")
    if int(bonus)<=0 or int(bonus)>=0:
        bonus=int(bonus)
    else:
        bonus=0
    amount=int(inf[0])
    number=int(inf[1])
    suma=0
    for i in range(amount):
        a=random.randint(1,number)
        message="Rolled for "+str(a+bonus)
        await ctx.send(message)
        suma=suma+a
    if amount>=2:
        total="Total sum is equal to="+str(suma)
        await ctx.send(total)

@bot.command()
async def damage(ctx, dicetype, disetype2, damage, bonus=0, bonus2=0, crit=False):

    if "d" in dicetype:
        inf=dicetype.split("d")
    elif "D" in dicetype:
        inf=dicetype.split("D")

    if "d" in disetype2:
        inf2=disetype2.split("d")
    elif "D" in disetype2:
        inf2=disetype2.split("D")

    if "d" in damage:
        damage=damage.split("d")
    elif "D" in damage:
        damage=damage.split("D")

    if int(bonus)<=0 or int(bonus)>=0:
        bonus=int(bonus)
    else:
        bonus=0

    if int(bonus2)<=0 or int(bonus2)>=0:
        bonus2=int(bonus2)
    else:
        bonus2=0
    res1=random.randint(1,int(inf[1]))+bonus
    res2=random.randint(1,int(inf2[1]))+bonus2
    message="\n1-st Rolled for:"+str(res1)+"\n2-nd Rolled for:"+str(res2)
    
    if res1>=res2:
        dmgroll=random.randint(1,int(damage[1]))
        if crit==True and dmgroll>=int(damage[1]):
            dmgroll=dmgroll+random.randint(1,int(damage[1]))
            msg=message+"\nCrit damage="+str(dmgroll)
            await ctx.send(msg)
        else:
            msg=message+"\nDamage="+str(dmgroll)
            await ctx.send(msg)
    else:
        msg=message+"\nNo damage looser"
        await ctx.send(msg)
            
@bot.command()
async def source(ctx):
    await ctx.send("https://drive.google.com/file/d/1K4XEXykRd3z8T5nmNOvizsBJLvnxDHtw/view?usp=sharing")
    

# Events
@bot.event
async def on_ready():
    print("sus")


@bot.listen()
async def on_message(message):
    print(message)

    if "суслик:" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('Видишь суслика?')
        await bot.process_commands(message)
    if "нет." in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('Вот и я не вижу.')
        await message.channel.send('А он есть...')
        await bot.process_commands(message)
    if "хост" in message.content.lower():
        await message.channel.send('Пидор?')
        await bot.process_commands(message)
    if "commands" in message.content.lower():
        await message.channel.send('>_help')
        await bot.process_commands(message)
        
    
bot.run('NTk5MjYyNjQ2MDk2ODg3ODM5.XSio1A.cgqoYtVDNrTaKfQl9G5PnegCqVg')

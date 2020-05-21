# bot.py
import os
import random

import discord
from discord.ext import commands

import config

bot = commands.Bot(command_prefix='!')


positions4 = {
  'Captain':"",
  'Tactical':"",
  'Engineering+':"",
  'Operations':""
  }
  
positions6 = {
  'Captain':"",
  'Helms':"",
  'Weapons':"",
  'Engineering':"",
  'Science':"",
  'Relay':""
}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:

      print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
        
      )
      for member in guild.members:
                print(member) # or do whatever you wish with the member detail	
                
    print("READY")

@bot.command(name='EXIT', help='exit the bot', hidden=True)
async def bot_exit(ctx):
    if ctx.author == bot.user:
        return

    print(ctx.author.id)
    if ctx.author.id != 449257714770509844:
      await ctx.send("Unauthorized use Will be reported")
      print("Unauthorixed access to exit by: {}".format(ctx.author))
      return	
    
    print("Exiting per {}".format(ctx.author))
    await ctx.send("EXIT Starting")
    
    
    exit()
    await ctx.send("EXIT FAILED")
    
@bot.command(name='resetRoles', help='Resets the roles', pass_context=True)
@commands.has_role('Game Admin')
async def reset_roles(ctx):
    if ctx.author == bot.user:
        return
    guild=ctx.guild
    print("Starting resetRoles")
    #find all the users with one of our roles and remove it.
    for member in guild.members:
      print(member.roles) # or do whatever you wish with the member detail
      for role in member.roles:
        
        if role.name == 'Playing':
          print("Removing Playing role from {}".format(member))
          await ctx.send("Removing {} from {}".format(role.name, member.name))
          await member.remove_roles(role,reason ="Request by {}".format(ctx.message.author))
    
@bot.command(name='playing', help='Sets your role to playing for the next match')
async def set_playing(ctx):
    if ctx.author == bot.user:
        return 
    guild=ctx.guild
    print("Starting add playing")
	
    role = discord.utils.get(ctx.guild.roles, name='Playing')
    await ctx.author.add_roles(role)
    await ctx.send("Thank you for playing")

@bot.command(name='notPlaying', help='Removesyour playing role.')
async def not_playing(ctx):
    if ctx.author == bot.user:
        return 
    guild=ctx.guild
    print("Starting add playing")
	
    role = discord.utils.get(ctx.guild.roles, name='Playing')
    await ctx.author.remove_roles(role)
    await ctx.send("Sorry you aren't playing")

    
@bot.command(name='randomPositions', help='Assigns Random positions', pass_context=True)
@commands.has_role('Game Admin')
async def reset_roles(ctx):

    if ctx.author == bot.user:
        return
    guild=ctx.guild 
    
    
    print("Starting randomPositions")
    
    #Lets get the folks who are playing
    role = discord.utils.get(ctx.guild.roles, name='Playing')
    players=role.members
    random.shuffle(players)
    numPlayers=len(players)
#     print(numPlayers)
#     for player in players:
#       print(player.name)


    if numPlayers == 1:
        await ctx.send("You don't need my help to play with yourself")
        return
    elif numPlayers == 2:
      print("Orgainizing 2 Player Ship")
      ship = positions4
      ship['Captain'] = players[0] 
      ship['Tactical'] = players[1] 
      ship['Engineering+'] = players[0] 
      ship['Operations'] = players[1] 
    elif numPlayers == 3:
      print("Orgainizing 3 Player Ship")
      ship = positions4
      ship['Captain'] = players[0]
      ship['Tactical'] = players[1]
      ship['Engineering+'] = players[2]
      ship['Operations'] = players[2]
    elif numPlayers == 4 :
      print("Orgainizing 4 Player Ship")
      ship=positions4
      ship['Captain'] = players[0]
      ship['Tactical'] = players[1] 
      ship['Engineering+'] = players[2] 
      ship['Operations'] = players[3]
    elif numPlayers == 5:
      print("Orgainizing 4 Player Ship")
      ship['Captain'] = players[0]
      ship['Helms'] = players[1]
      ship['Weapons'] = players[2]
      ship['Engineering'] = players[3]
      ship['Science'] = players[4]
      ship['Relay'] = players[4]
    else:
      print("Orgainizing 4 Player Ship")
      ship['Captain'] = players[0]
      ship['Helms'] = players[1]
      ship['Weapons'] = players[2]
      ship['Engineering'] = players[3]
      ship['Science'] = players[4]
      ship['Relay'] = players[5]

    for position, player in ship.items():
        try:
            temp="{}: {}".format(position, player.name)
        except:
            temp="{}: EMPTY".format(position)
        await ctx.send(temp)
	
print('Starting -=-=-=-=-=-=-=-')
bot.run(config.DISCORD_TOKEN)


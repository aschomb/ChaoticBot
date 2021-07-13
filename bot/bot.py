import discord
from discord.ext import commands
from dpytools.checks import *

client = commands.Bot(command_prefix = "$")
client.remove_command("help")

cogs_load = ['animals.py','fun.py','help.py','moderation.py','status.py','tools.py']
#cogs_no_load = {'exceptions.py'}

@client.command()
@only_these_users(736309573924683917,290926756397842432)
async def load(ctx, extension):
  try:
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Cog **{extension}** has been loaded.")
  except:
    await ctx.send(f"Cog **{extension}** has already been loaded, or you may not have permission to load cogs.")

@client.command()
@only_these_users(736309573924683917,290926756397842432)
async def unload(ctx, extension):
  try:
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f"Cog **{extension}** has been unloaded.")
  except:
    await ctx.send(f"Cog **{extension}** has already been unloaded, or you may not have permission to unload cogs.")

@client.command()
@only_these_users(736309573924683917,290926756397842432)
async def reload(ctx, extension):
  try:
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Cog **{extension}** has been reloaded.")
  except:
    await ctx.send(f"Error loading cog **{extension}**, or you may not have permission to reload cogs.")

@client.command()
@only_these_users(736309573924683917,290926756397842432)
async def reloadall(ctx):
  try:
    for filename in cogs_load:
        client.unload_extension(f'cogs.{filename[:-3]}')
    
    for filename in cogs_load:
        client.load_extension(f'cogs.{filename[:-3]}')
    
    em = discord.Embed(title="**Cogs:**", description = f"{cogs_load}")
    await ctx.send("All cogs have been reloaded.\n")
    await ctx.send(embed = em)
  except:
      await ctx.send(f"Error reloading all cogs, or you may not have permission to reload all cogs.")

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="$help to see menu"))
  print(f"Logged in as {client.user}")


for filename in cogs_load:
    client.load_extension(f'cogs.{filename[:-3]}')

with open('/root/ChaoticBot/token.txt') as f:
    token = f.readline()

client.run(str(token))

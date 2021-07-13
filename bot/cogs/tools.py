import discord
import time
import json

from discord.ext import commands
from discord.utils import get

ecolor = 0xe91e63

popTimer: float
gameTimer: float
movieTimer: float

with open("/root/ChaoticBot/bot/timers.json", 'r', encoding='utf-8') as data:
    timers_json = json.load(data)
    data.close()

def getTimers():
    for var in timers_json["Timers"][0]["times"]:
        if var["name"] == "populate":
            global popTimer
            popTimer = var["time"]
        if var["name"] == "gamenight":
            global gameTimer
            gameTimer = var["time"]
        if var["name"] == "movienight":
            global movieTimer
            movieTimer = var["time"]
getTimers()

def setTimer(role, time):
    with open("/root/ChaoticBot/bot/timers.json", 'r', encoding='utf-8') as data:
        data_json = json.load(data)
        data.close()

    for var in data_json["Timers"][0]["times"]:
        if role == "populate":
            if var["name"] == "populate":
                var["time"] = time
                break
        if role == "gamenight":
            if var["name"] == "gamenight":
                var["time"] = time
                break
        if role == "movienight":
            if var["name"] == "movienight":
                var["time"] = time
                break

    with open("/root/ChaoticBot/bot/timers.json","w", encoding='utf-8') as data_file:
        json.dump(data_json, data_file)
        data_file.close()
    
    getTimers()

class tools(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        time1 = time.perf_counter()
        await ctx.trigger_typing()
        time2 = time.perf_counter()
        ping = round((time2-time1)*1000)
        await ctx.send(f"Ping - {ping}")

    @commands.command()
    async def setCD(self, ctx, role: str, time: float):
        if role == "populate" or "gamenight" or "movienight":
            setTimer(role, time)
            em = discord.Embed(title="**Cooldown Set**", color=ecolor)
            em.add_field(name="**Role**", value=f"{role}", inline=True)
            em.add_field(name="**Cooldown**", value = "{:.2f} hrs or {:.2f} m".format(time/3600, time/60))
            await ctx.send(embed=em)
        else:
            await ctx.send("Specified role does not exit")

    @commands.command()
    @commands.cooldown(1.0, popTimer, commands.BucketType.guild)
    # take ping permissions from regular users, give permission to bot
    async def populate(self, ctx):
        populator = get(ctx.guild.roles, name='Populator')
        await ctx.send(f"{ctx.author.mention} has pinged {populator.mention}!")

    @populate.error
    async def populate_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, this command is still on cooldown!")
            time = error.retry_after
            await ctx.send('Try again in {:.2f} hours or {:.2f} minutes!'.format(time/3600, time/60))

    @commands.command()
    @commands.cooldown(1.0, gameTimer, commands.BucketType.guild)
    # take ping permissions from regular users, give permission to bot
    async def gamenight(self, ctx):
        gamer = get(ctx.guild.roles, name='Gamenight')
        await ctx.send(f"{ctx.author.mention} has pinged {gamer.mention}!")

    @gamenight.error
    async def gamenight_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, this command is still on cooldown!")
            time = error.retry_after
            await ctx.send('Try again in {:.2f} hours or {:.2f} minutes!'.format(time/3600, time/60))

    @commands.command()
    @commands.cooldown(1.0, 0.0, commands.BucketType.guild)
    # take ping permissions from regular users, give permission to bot
    async def dnd(self, ctx):
        wizards = get(ctx.guild.roles, name='DnD')
        await ctx.send(f"{ctx.author.mention} has pinged {wizards.mention}!")

    @dnd.error
    async def dnd_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, this command is still on cooldown!")
            time = error.retry_after
            await ctx.send('Try again in {:.2f} hours or {:.2f} minutes!'.format(time/3600, time/60))

    @commands.command()
    @commands.cooldown(1.0, movieTimer, commands.BucketType.guild)
    # take ping permissions from regular users, give permission to bot
    async def movienight(self, ctx):
        watchers = get(ctx.guild.roles, name='Movienight')
        await ctx.send(f"{ctx.author.mention} has pinged {watchers.mention}!")

    @movienight.error
    async def movienight_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, this command is still on cooldown!")
            time = error.retry_after
            await ctx.send('Try again in {:.2f} hours or {:.2f} minutes!'.format(time/3600, time/60))

    #@commands.command()
    #async def testCoolDown(self, ctx, time):
    #    cooldown = time
    #    await ctx.send(f"test role Pinging cooldown set to {cooldown}")
    # 
    #@commands.command()
    #@commands.cooldown(1.0, {cooldown}, commands.BucketType.guild)
    ## take ping permissions from regular users, give permission to bot
    #async def pingtest(self, ctx):
    #    populator = get(ctx.guild.roles, name='Populator')
    #    await ctx.send(f"{ctx.author.mention} has pinged {populator.mention}!")

def setup(client):
    client.add_cog(tools(client))

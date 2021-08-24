import discord
import time
import json

#from bin import *
from datetime import datetime
from pytz import timezone
from discord.ext import commands
from discord.utils import get

ecolor = 0xe91e63
tz = timezone('EST')

# initializes the 3 timer variables to floats
popTimer: float
gameTimer: float
movieTimer: float
tf2Timer: float

# initially opens and reads json file for timers
with open("/root/ChaoticBot/bot/timers.json", 'r', encoding='utf-8') as data:
    timers_json = json.load(data)
    data.close()

# used for resyncing timer variables with what is in the json file
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
        if var["name"] == "tf2":
            global tf2Timer
            tf2Timer = var["time"]

# for resyncing the variables on start
getTimers()

# modifying method for setting variables in code and in the json file
def setTimer(role, time):
    # reads current json data
    with open("/root/ChaoticBot/bot/timers.json", 'r', encoding='utf-8') as data:
        data_json = json.load(data)
        data.close()
    
    # sets input timer in the json file to the input time
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
        if role == "tf2":
            if var["name"] == "tf2":
                var["time"] = time
                break

    # writes times to json
    with open("/root/ChaoticBot/bot/timers.json","w", encoding='utf-8') as data_file:
        json.dump(data_json, data_file)
        data_file.close()
    
    # syncs variables to json timers
    getTimers()


class tools(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    #@commands.command()
    #async def test(self, ctx):
    #    raise TestEror()

    # testing the bot's latency ontop of the Discord API
    @commands.command()
    async def ping(self, ctx):
        time1 = time.perf_counter()
        await ctx.trigger_typing()
        time2 = time.perf_counter()
        ping = round((time2-time1)*1000)
        await ctx.send(f"Ping - {ping}")

    # for setting cooldowns on the role ping commands (the next 6, ping command paired with it's error)
    @commands.command()
    async def setCD(self, ctx, role: str, time: float):
        if role == "populate" or "gamenight" or "movienight" or "tf2":
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
        time_now = datetime.now()
        time = float(f"{time_now.hour}.{time_now.minute}")
        if (time > 12.00) and (time < 23.59):
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

    @commands.command()
    @commands.cooldown(1.0, tf2Timer, commands.BucketType.guild)
    async def tf2(self, ctx):
        tf2ers = get(ctx.guild.roles, name='TF2')
        await ctx.send(f"{ctx.author.mention} has pinged {tf2ers.mention}!")
    
    @tf2.error
    async def tf2_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, this command is still on cooldown!")
            time = error.retry_after
            await ctx.send('Try again in {:.2f} hours or {:.2f} minutes!'.format(time/3600, time/60))
    
    @commands.command()
    async def server(self, ctx):    
        
        #guild = ctx.guild
        
        em = discord.Embed(title="Server Information", color=ecolor, timestamp=datetime.now(tz))

        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
                    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        fields = [("Name", ctx.guild.name, True),
                  ("Owner", ctx.guild.owner, True),
                  ("Region", ctx.guild.region, True),
                  ("Created", ctx.guild.created_at.strftime("%m/%d/%Y"), True),
                  ("Members", len(ctx.guild.members), True),
                  ("Banned", len(await ctx.guild.bans()), True),
                  ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
                  ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
                  ("Statuses", f":green_circle: {statuses[0]} :orange_circle: {statuses[1]} :red_circle: {statuses[2]} :white_circle: {statuses[3]}", True),
                  ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            em.add_field(name=name, value=value, inline=inline)
        
        #em = discord.Embed(title=f"**Server Information**", color=ecolor)
        #em.add_field(name="**Name**", value=f"{guild.name}", inline=True)
        #em.add_field(name="**Owner**", value=f"{guild.owner.display_name} ({guild.owner})", inline=True)
        #em.add_field(name="**Date Created**", value=guild.created_at.strftime("%m/%d/%Y"), inline=True)
                

        #em.add_field(name="**User Count**", value=f"{guild.member_count} Users", inline=True)
        #em.add_field(name="**Online**", value=f" Users", inline=True)
        await ctx.send(embed=em)

    # test commands

    #@commands.command()
    #async def guildname(self, ctx):
    #    await ctx.send(ctx.guild.name)
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

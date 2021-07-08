import discord, time
from discord.ext import commands
from discord.utils import get
popTimer, gameTimer, movieTimer = 0.0, 0.0, 0.0

def setTimer(role, time):
    if (role == "populate"):
        global popTimer
        popTimer = time
    if (role == "gamenight"):
        global gameTimer
        gameTimer = time
    if (role == "movienight"):
        global movieTimer
        movieTimer = time

class tools(commands.Cog):

    def __init__(self, client):
        self.client = client

    #global popTimer, gameTimer, moveTimer
    
    @commands.command()
    async def ping(self, ctx):
        time1 = time.perf_counter()
        await ctx.trigger_typing()
        time2 = time.perf_counter()
        ping = round((time2-time1)*1000)
        await ctx.send(f"Ping - {ping}")

    @commands.command()
    async def setCD(self, ctx, role: str, time: float):
        setTimer(role, time)
        #if (role == "populate"):
        #    popTimer = time
        #if (role == "gamenight"):
        #    gameTimer = time
        #if (role == "movienight"):
        #    movieTimer = time
        #await ctx.send(popTimer)

    @commands.command()
    @commands.cooldown(1.0, popTimer, commands.BucketType.guild)
    # take ping permissions from regular users, give permission to bot
    async def populate(self, ctx):
        populator = get(ctx.guild.roles, name='Populator')
        await ctx.send(f"{popTimer}")
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
    @commands.cooldown(1.0, movieTimer, commands.BucketType.guild)
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
    @commands.cooldown(1.0, 7200.0, commands.BucketType.guild)
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

import discord
import hashlib
import random
import time
import re
from discord.ext import commands
from datetime import datetime

ecolor = 0xe91e63

t = int(time.time() * 1000.0)
random.seed(((t & 0xff000000) >> 24) + ((t & 0x00ff0000) >> 8) + ((t & 0x0000ff00) << 8) + ((t & 0x000000ff) << 24))

def strip_global_mentions(message, ctx=None):
    #if ctx:
    #    perms = ctx.message.channel.permissions_for(ctx.message.author)
    #    if perms.mention_everyone:
    #        return message
    remove_everyone = re.compile(re.escape("@everyone"), re.IGNORECASE)
    remove_here = re.compile(re.escape("@here"), re.IGNORECASE)
    message = remove_everyone.sub("everyone", message)
    message = remove_here.sub("here", message)
    return message

class fun(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # the bot repeats whatever string is entered by the user
    @commands.command()
    async def say(self, ctx, *, message: str):
        try:
            await ctx.message.delete()
        except:
            pass
        em = discord.Embed(title=f"{ctx.author.display_name}'s message", color = ecolor)
        em.add_field(name="Message:", value = strip_global_mentions(message , ctx))
        time_now = datetime.now()
        time_formatted = time_now.strftime("%m/%d/%Y at %H:%M:%S")
        em.set_footer(text=f"Used at {time_formatted}")
        await ctx.send(embed=em)
        #await ctx.send(strip_global_mentions(message,ctx))

    @commands.command()
    async def reverse(self, ctx, *, msg: str):
        await ctx.send("`{}`".format(strip_global_mentions(msg[::-1], ctx)))
   
    # ----- Encryption Commands -----
    @commands.command()
    async def md5(self, ctx, *, msg:str):
        await ctx.send("`{}`".format(hashlib.md5(bytes(msg.encode("utf-8"))).hexdigest()))

    @commands.command()
    async def sha1(self, ctx, *, msg:str):
        await ctx.send("`{}`".format(hashlib.sha1(bytes(msg.encode("utf-8"))).hexdigest()))

    @commands.command()
    async def sha224(self, ctx, *, msg:str):
        await ctx.send("`{}`".format(hashlib.sha224(bytes(msg.encode("utf-8"))).hexdigest()))
    
    @commands.command()
    async def sha256(self, ctx, *, msg:str):
        await ctx.send("`{}`".format(hashlib.sha256(bytes(msg.encode("utf-8"))).hexdigest()))

    @commands.command()
    async def sha384(self, ctx, *, msg:str):
        await ctx.send("`{}`".format(hashlib.sha384(bytes(msg.encode("utf-8"))).hexdigest()))

    @commands.command()
    async def sha512(self, ctx, *, msg:str):
        await ctx.send("`{}`".format(hashlib.sha512(bytes(msg.encode("utf-8"))).hexdigest()))
    # ------------------------------
    
    # ----- Gambling Commands -----
    @commands.command()
    async def rolldice(self, ctx):
        await ctx.send("``You rolled a {}!``".format(random.randint(1,6)))

    @commands.command(aliases=["flip", "coin","cf"])
    async def coinflip(self, ctx):
        coinsides = ["Heads", "Tails"]
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    @commands.command(aliases=["slots", "bet"])
    @commands.cooldown(rate=1, per=1.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")
    # -----------------------------

    # ----- Random -----
    @commands.command()
    async def piss(self, ctx):
        await ctx.send("Shit?")
        time.sleep(1)
        await ctx.send("Maybe cum?")

    @commands.command()
    async def penis(self, ctx, user: discord.Member):
       # random.seed(user.id)
        randShaft = random.randint(0,30)
        penis = "8" + "=" * randShaft + "D"
        em = discord.Embed(title  = f"{user.display_name}'s Penis size:", description = f"{penis}", color=ecolor)
        
        if (randShaft == 30):
            em.set_footer(text="Your penis size is massive!")
        if (randShaft < 30 and  randShaft >= 25):
            em.set_footer(text="Your penis size is big!")
        if (randShaft <= 25 and randShaft > 15):
            em.set_footer(text="Your penis size is above average!")
        if (randShaft == 15):
            em.set_footer(text="Your penis size is average!")
        if (randShaft < 15 and randShaft >= 5):
            em.set_footer(text="Your penis size is below average!")
        if (randShaft <= 5 and randShaft > 0):
            em.set_footer(text="Your penis size is small!")
        if (randShaft == 0):
            em.set_footer(text="I didn't even know a penis that small was possible")

        await ctx.send(embed = em)
    # ------------------

def setup(client):
    client.add_cog(fun(client))
    

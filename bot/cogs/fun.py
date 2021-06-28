import discord, re, random, hashlib, time
from discord.ext import commands
ecolor = 0xe91e63
random.seed()

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

    @commands.command()
    async def say(self, ctx, *, message : str):
        try:
            await ctx.message.delete()
        except:
            pass
        await ctx.send(strip_global_mentions(message,ctx))

    @commands.command()
    async def rolldice(self, ctx):
        await ctx.send("You rolled a {}!".format(random.randint(1, 6)))

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

    @commands.command()
    async def reverse(self, ctx, *, msg:str):
        await ctx.send(strip_global_mentions(msg[::-1], ctx))
    
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

    @commands.command()
    async def piss(self, ctx):
        await ctx.send("Shit?")
        time.sleep(1)
        await ctx.send("Maybe cum?")

    @commands.command()
    async def penis(self, ctx, user: discord.Member):
        random.seed(user.id)
        penis = "8" + "=" * random.randint(0,30) + "D"
        em = discord.Embed(title  = f"{user.display_name}'s Penis size:", description = f"{penis}", color=ecolor)
        await ctx.send(embed = em)

   # @commands.command()
   # async def tictactoe(self, ctx

def setup(client):
    client.add_cog(fun(client))
    

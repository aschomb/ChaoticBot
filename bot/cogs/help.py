import discord
from discord.ext import commands
ecolor = 0xe91e63

class helpmenu(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = "__Help Menu__", description = "Use $help <command> for more information on a command!", color = ecolor)
        em.add_field(name = "Animals", value = "axolotl\nbird\nbirb\ncat\ncow\ndog\nduck\nfox\nfrog\nlizard\nkangaroo\nkoala\npanda\npenguin\nrabbit\nraccoon\nred panda", inline = True)
        em.add_field(name = "Fun", value = "coinflip\nmd5\npenis\nreverse\nrolldice\nsay\nslots\nsha1\nsha224\nsha256\nsha384\nsha512", inline = True)
        em.add_field(name = "Moderation", value = "addrole\nannounce\nban\ndm\nkick\nremoverole\nunban", inline = True)
        em.add_field(name = "Tools", value = "dnd\ngamenight\nmovienight\nping\npopulate", inline = True)
        await ctx.send(embed = em)

    @help.command()
    async def say(self, ctx):
        em = discord.Embed(title = "__Say__", description = "Make the bot say whatever you want.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$say [message]")
        await ctx.send(embed = em)

    @help.command()
    async def rolldice(self, ctx):
        em = discord.Embed(title = "__Rolldice__", description = "Roll a dice.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$rolldice")
        await ctx.send(embed = em)

    @help.command()
    async def md5(self, ctx):
        em = discord.Embed(title = "__Md5__", description = "Encyrpt a message in the MD5 algorithm.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$md5 [message]")
        await ctx.send(embed = em)

    @help.command()
    async def sha1(self, ctx):
        em = discord.Embed(title = "__Sha1__", description = "Encyrpt a message in the SHA1 algorithm.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$sha1 [message]")
        await ctx.send(embed = em)

    @help.command()
    async def sha224(self, ctx):
        em = discord.Embed(title = "__Sha224__", description = "Encyrpt a message in the SHA224 algorithm.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$sha224 [message]")
        await ctx.send(embed = em)

    @help.command()
    async def sha256(self, ctx):
        em = discord.Embed(title = "__Sha256__", description = "Encyrpt a message in the SHA256 algorithm.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$sha256 [message]")
        await ctx.send(embed = em)
    
    @help.command()
    async def sha384(self, ctx):
        em = discord.Embed(title = "__Sha384__", description = "Encyrpt a message in the SHA384 algorithm.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$sha384 [message]")
        await ctx.send(embed = em)

    @help.command()
    async def sha512(self, ctx):
        em = discord.Embed(title = "__Sha512__", description = "Encyrpt a message in the SHA512 algorithm.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$sha512 [message]")
        await ctx.send(embed = em)

    @help.command()
    async def reverse(self, ctx):
        em = discord.Embed(title = "__Reverse__", description = "Reverses a given string or phrase.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$reverse [message]")
        await ctx.send(embed = em)\
        
    @help.command()
    async def coinflip(self, ctx):
        em = discord.Embed(title = "__Coinflip__", description = "Flips a coin.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$coinflip")
        await ctx.send(embed = em)
    @help.command()
    async def cf(self, ctx):
        em = discord.Embed(title = "__Coinflip__", description = "Flips a coin.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$cf")
        await ctx.send(embed = em)
    @help.command()
    async def coin(self, ctx):
        em = discord.Embed(title = "__Coinflip__", description = "Flips a coin.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$coin")
        await ctx.send(embed = em)
    @help.command()
    async def flip(self, ctx):
        em = discord.Embed(title = "__Coinflip__", description = "Flips a coin.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$flip")
        await ctx.send(embed = em)

    @help.command()
    async def slots(self, ctx):
        em = discord.Embed(title = "__Slot__", description = "Play a round of the slot machine.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$slot (also works with $slots and $bet)")
        await ctx.send(embed = em)

    @help.command()
    async def ping(self, ctx):
        em = discord.Embed(title = "__Ping__", description = "Find out the bot's latency.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$ping")
        await ctx.send(embed = em)
    
    @help.command()
    async def populate(self, ctx):
        em = discord.Embed(title = "__Populate__", description = "Ping the populator role for TTT.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$populate")
        await ctx.send(embed = em)

    @help.command()
    async def kick(self, ctx):
        em = discord.Embed(title = "__Kick__", description = "Kick a player from the Discord server.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$kick <user> [reason]")
        await ctx.send(embed = em)

    @help.command()
    async def addrole(self, ctx):
        em = discord.Embed(title = "__Addrole__", description = "Adds a role to the given player.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$addrole <@user> [role name]")
        await ctx.send(embed = em)
    
    @help.command()
    async def removerole(self, ctx):
        em = discord.Embed(title = "__Removerole__", description = "Removes a role to the given player.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$removerole <@user> [role name]")
        await ctx.send(embed = em)

    @help.command()
    async def dm(self, ctx):
        em = discord.Embed(title = "__Dm__", description = "DMs the given player through the bot.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$dm <@user> [message]")
        await ctx.send(embed = em)
    
    @help.command()
    async def announce(self, ctx):
        em = discord.Embed(title = "__Announce__", description = "Announces a message in a given text channel. <<WIP>>", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$announce <channel name> [message]")
        await ctx.send(embed = em)
    
    @help.command()
    async def ban(self, ctx):
        em = discord.Embed(title = "__Ban__", description = "Bans a player for a given reason.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$ban <user> [reason]")
        await ctx.send(embed = em)

    @help.command()
    async def unban(self, ctx):
        em = discord.Embed(title = "__Unban__", description = "Unbans a given player.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$unban <user>")
        await ctx.send(embed = em)

    @help.command()
    async def penis(self, ctx):
        em = discord.Embed(title = "__Penis__", description = "Tells you a given player's penis size.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$penis <user>")
        await ctx.send(embed = em)

    @help.command()
    async def animal(self, ctx):
        em = discord.Embed(title = "__Animal__", description = "Retrieves a picture of a given animal.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$animal <animal>")
        em.add_field(name="**Accepted Animals**:", value = "axolotl\nbird\nbirb\ncat\ncow\ndog\nduck\nfox\nfrog\nlizard\nkangaroo\nkoala\npanda\npenguin\nrabbit\nraccoon\nred panda")
        await ctx.send(embed = em)

    @help.command()
    async def dnd(self, ctx):
        em = discord.Embed(title = "__DnD__", description = "Pings the users with the DnD role.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$dnd")
        await ctx.send(embed = em)

    @help.command()
    async def gamenight(self, ctx):
        em = discord.Embed(title = "__Gamenight__", description = "Pings the users with the Gamenight role.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$gamenight")
        await ctx.send(embed = em)

    @help.command()
    async def movienight(self, ctx):
        em = discord.Embed(title = "__Movienight__", description = "Pings the users with the Movienight role.", color = ecolor)
        em.add_field(name = "**Syntax**", value = "$movienight")
        await ctx.send(embed = em)



def setup(client):
    client.add_cog(helpmenu(client))
    

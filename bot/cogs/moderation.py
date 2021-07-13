import discord
import re

from discord.ext import commands
from dpytools.checks import *

ecolor = 0xe91e63

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.has_permissions(kick_members=True)
    @commands.is_owner()
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await member.kick(reason=reason)
        #await ctx.send(f'User {member} has been kicked for {reason}.')
        em = discord.Embed(title=f"**Kicked {member.display_name}!**", description= f"Reason:{reason}\nBy: {ctx.author.display_name}", color = ecolor)
        await ctx.send(embed = em)
        await member.send(embed = em)
    
    # ----- Ban related -----
    @commands.has_permissions(ban_members=True)
    @commands.is_owner()
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason = "No reason provided"):
        await member.ban(reason = reason)
        ban = discord.Embed(title=f"**Banned {member.display_name}!**", description = f"Reason: {reason}\nBy: {ctx.author.mention}", color=ecolor)
        await ctx.send(embed=ban)
        await member.send(embed = ban)
    
    @commands.has_permissions(ban_members=True)
    @commands.is_owner()
    @commands.command()
    async def banlist(self, ctx):
        banned_users = await ctx.guild.bans()
        for ban in banned_users:
            #await ctx.send(ban)
            #em = discord.Embed(title="**Ban List**",color=ecolor)
            #em.add_field(name="**Users**", value=ban[1].name + '#'  + ban[1].discriminator, inline=True)
            #em.add_field(name="**ID**", value=str(ban[1].id), inline=True)
            await ctx.send("User: " + ban[1].name + '#' + ban[1].discriminator + '\nID: ' + str(ban[1].id) + '\nReason: ' + ban.reason)
        #await ctx.send(embed = em)    

    @commands.has_permissions(ban_members=True)
    @commands.is_owner()
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator, *_ = member.split('#') + [None]
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
            #if (user.id == member.id):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                await member.send(f"{member.mention}, you have been unbanned by {ctx.author.display_name}")
                return
        await ctx.send("User was not banned/found.")
    # -----------------------

    # ----- Role related -----
    @commands.command()
    @commands.is_owner()
    @only_these_users(736309573924683917,290926756397842432)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f"Role {role} has been added to {member.display_name}.")
        except:
            await ctx.send("Error adding role.")

    @commands.command()
    @commands.is_owner()
    @only_these_users(736309573924683917,290926756397842432)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f"Role {role} has been removed from {member.display_name}.")
        except:
            await ctx.send("Error removing role.")
    # ------------------------

    @commands.command()
    @only_these_users(736309573924683917,290926756397842432)
    async def dm(self, ctx, user: discord.User, *, msg):
        await ctx.send('Successful.')
        await user.send(f'{msg}')

    @commands.command()
    @only_these_users(736309573924683917,290926756397842432)
    async def announce(self, ctx, channel: discord.TextChannel, *, title, message):
        em = discord.Embed(description = f"{message}")
        await channel.send(embed = em)
   
    #@commands.Cog.listener()
    #async def on_message(self, message):
        #slurs = ["fag","faggot","nigger","nigga"]
        #msg = message.content
        #msg = msg.lower()
        #user = message.author
        ##if any(word in msg.lower() for word in slurs):
        #pattern = re.compile(r'{}'.format(msg))
        ##if ((msg.startswith("$reload") == False) or (msg.startswith("$unload") == False) or (msg.startswith("$load") == False) or (msg.startswith("$reloadall") == False) and (message.author.id != 290926756397842432)):
        ##if (user.id != 290926756397842432):
        #for word in slurs:
            #if re.fullmatch(pattern, word):
                #await message.delete()
                #em = discord.Embed(title="Message deleted",color=ecolor)
                #em.add_field(name="**Warning**",value=f"You can't say that word",inline=True)
                #em.add_field(name="**Message Content**",value=f"{message.content}", inline=True)
                ##em.add_field(name="**Disclaimer**",value="You may not have intended for your message to contain a slur, if this was a mistake, ignore it.", inline=True)
                #em.set_footer(text="Disclaimer: Not every deleted message purposely contained a slur, the bot just happened to pick it up.  If that is the case, just ignore this.")
                #await user.send(embed=em)
            ##await user.send(f"{message.author.mention}, you can't say that.{message.content}")
            ##await user.send(f"{message.content}")
            ##await message.channel.send(f"{message.author.mention}, you can't say that.")

def setup(client):
    client.add_cog(moderation(client))

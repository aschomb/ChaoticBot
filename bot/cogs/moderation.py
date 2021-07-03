import discord
from discord.ext import commands
ecolor = 0xe91e63

class moderation(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked for {reason}.')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason = "No reason provided"):
        await member.ban(reason = reason)
        ban = discord.Embed(title=f"Banned {member.display_name}!", description = f"Reason: {reason}\nBy: {ctx.author.mention}", color=ecolor)
        await ctx.channel.send(embed=ban)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @commands.command()
    @commands.is_owner() 
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f"Role {role} has been added to {member.display_name}.")
        except:
            await ctx.send("Error adding role.")

    @commands.command()
    @commands.is_owner()
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f"Role {role} has been removed from {member.display_name}.")
        except:
            await ctx.send("Error removing role.")

    @commands.command()
    async def dm(self, ctx, user: discord.User, *, msg):
        await ctx.send('Successful.')
        await user.send(f'{msg}')

    @commands.command()
    async def announce(self, ctx, channel: discord.TextChannel, *, title, message):
        em = discord.Embed(description = f"{message}")
        await channel.send(embed = em)
   
    @commands.Cog.listener()
    async def on_message(self, message):
        slurs = ["fag","faggot","nigger","nigga"]
        msg = message.content
        if any(word in msg.lower() for word in slurs):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, you can't say that.")

    #@commands.command()
    #async def mute(self, ctx, member: discord.Member, *, reason = None):
    #    text_channel_list = []
    #    for guild in client.guilds:
    #        for channel in guild.text_channels:
    #            text_channel_list.append(channel)
    #    
    #    for channel in text_channel_list:
    #        await ctx.channel.set_permissions(member, send_messages=False)
    #
    #    mute = discord.Embed(title=f"Muted {member.display_name}!", description = f"Reason: {reason}\nBy: {ctx.author.mention}")
    #    await ctx.channel.send(embed=mute)
    
    #@commands.command()
    #async def unnmute(self, ctx, member: discord.Member):
    #    text_channel_list = []
    #    for guild in client.guilds:
    #        for channel in guild.text_channels:
    #            text_channel_list.append(channel)
    #    
    #    for channel in text_channel_list:
    #        await ctx.channel.set_permissions(member, send_messages=True)
    #
    #    mute = discord.Embed(title=f"Unmuted {member.display_name}!", description = f"By: {ctx.author.mention}")
    #    await ctx.channel.send(embed=mute)

def setup(client):
    client.add_cog(moderation(client))

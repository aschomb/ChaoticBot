import discord
from datetime import datetime
import valve.source
from valve.source.a2s import ServerQuerier
from discord.ext import commands, tasks
from mcstatus import MinecraftServer
ttt_server = ("208.103.169.70", 27021)
mc_server = MinecraftServer.lookup("158.62.204.28:25565")
ecolor = 0xe91e63

class status(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.selfTTT.start()

    # ----- User commands -----
    @commands.command(aliases=['statusTTT','tttstatus','TTTstatus'])
    async def statusttt(self, ctx):
        # Queries the TTT server based on its IP and port
        try:
            with ServerQuerier(ttt_server) as server:
               
                # Contains info about the gamemode, version, players, max players, etc.
                ttt_info = server.info()                
                ttt_players = server.players()
                
                # adds every player to a list
                players = []
                for player in server.players()["players"]:
                    players.append("__" + player["name"]+ "__")
                
                player_count = len(players)
                ttt_map = server.info()["map"]
                max_players = server.info()["max_players"]
        
        # in case server is not responding
        except valve.source.NoResponseError:
            await ctx.send(f"``Server {ttt_server[0]}:{ttt_server[1]} timed out!  No Response.``")
            return 0 

        em = discord.Embed(title="**{server_name}**".format(**ttt_info), color = ecolor)
        em.set_thumbnail(url="https://i.imgur.com/eUgcNDX.png")
        em.add_field(name="**Map**", value=f"{ttt_map}", inline=True)
        em.add_field(name="**Player Count**", value=f"{player_count}/{max_players}", inline=True)
        em.add_field(name="**Connect**", value="[[Connect]](https://tinyurl.com/syw85zst)", inline=True)
        
        # states if players are online, and if they are, their usernames
        if (player_count == 0):
            em.add_field(name="**Online Players**", value="No one is online.", inline=True)
        
        if (player_count > 0):
            playerString = '\n'.join(players)
            em.add_field(name="**Online Players**", value= playerString, inline=True)

        time_now = datetime.now()
        time_formatted = time_now.strftime("%d/%m/%Y %H:%M:%S")
        em.set_footer(text=f"Last Updated: {time_formatted}")
        await ctx.send(embed = em)
    
    @commands.command(aliases=['statusMC','mcstatus','MCstatus'])
    async def statusmc(self, ctx):
        em = discord.Embed(title="**ChaoticCove**", color = ecolor)
        mc_status = mc_server.status()
        em.set_thumbnail(url="https://i.imgur.com/8fDbAlM.png")
        mc_player_count = mc_status.players.online
        em.add_field(name="**Player Count**", value = f"{mc_player_count} players online")
        mc_latency = mc_status.latency
        em.add_field(name="**Latency**", value = f"{mc_latency}")
        em.add_field(name="**IP**", value = "158.62.204.28")
        if mc_player_count == 0:
            em.add_field(name="**Online Players:**", value ="No one is online.")
        if mc_player_count > 0:
            mc_query = mc_server.query() 
            #mc_players = '\n'.join(mc_query.players.names)
            em.add_field(name="**Online Players:**", value = "__{0}__".format("\n".join(mc_query.players.names)))
        time_now = datetime.now()
        time_formatted = time_now.strftime("%d/%m/%Y %H:%M:%S")
        em.set_footer(text=f"Last Updated: {time_formatted}")
        await ctx.send(embed = em)
    # -------------------------


    # ----- Self updating statuses -----
    @tasks.loop(minutes=1.0)
    async def selfTTT(self):
        await self.client.wait_until_ready()
        tttmessage = await self.client.get_channel(847228889435471893).fetch_message(864646038497001503)
        # Queries the TTT server based on its IP and port
        try:
            with ServerQuerier(ttt_server) as server:
               
            # Contains info about the gamemode, version, players, max players, etc.
                ttt_info = server.info()                
                ttt_players = server.players()
                
                # adds every player to a list
                players = []
                for player in server.players()["players"]:
                    players.append("__" + player["name"]+ "__")
                
                player_count = len(players)
                ttt_map = server.info()["map"]
                max_players = server.info()["max_players"]
        
        # in case server is not responding
        except valve.source.NoResponseError:
            time_now = datetime.now()
            time_formatted = time_now.strftime("%d/%m/%Y  %H:%M:%S")
            print(f"No response at {time_formatted}.")

        newEmbedTTT = discord.Embed(title="**{server_name}**".format(**ttt_info), color = ecolor)
        newEmbedTTT.set_thumbnail(url="https://i.imgur.com/eUgcNDX.png")
        newEmbedTTT.add_field(name="**Map**", value=f"{ttt_map}", inline=True)
        newEmbedTTT.add_field(name="**Player Count**", value=f"{player_count}/{max_players}", inline=True)
        newEmbedTTT.add_field(name="**Connect**", value="[[Connect]](https://tinyurl.com/syw85zst)", inline=True)
        
        # states if players are online, and if they are, their usernames
        if (player_count == 0):
            newEmbedTTT.add_field(name="**Online Players**", value="No one is online.", inline=True)
        
        if (player_count > 0):
            playerString = '\n'.join(players)
            newEmbedTTT.add_field(name="**Online Players**", value= playerString, inline=True)

        time_now = datetime.now()
        time_formatted = time_now.strftime("%d/%m/%Y %H:%M:%S")
        newEmbedTTT.set_footer(text=f"Last Updated: {time_formatted}")
  
        await tttmessage.edit(embed = newEmbedTTT)
    
    @tasks.loop(minutes=1.0)
    async def selfMC(self):
        await self.client.wait_until_ready()
        mcmessage = await self.client.get_channel(channelID).fetch_message(messageID)
       
        newEmbedMC = discord.Embed(title="**ChaoticCove**", color = ecolor)
        mc_status = mc_server.status()
        newEmbedMC.set_thumbnail(url="https://i.imgur.com/8fDbAlM.png")
        mc_player_count = mc_status.players.online
        newEmbedMC.add_field(name="**Player Count**", value = f"{mc_player_count} players online")
        mc_latency = mc_status.latency
        newEmbedMC.add_field(name="**Latency**", value = f"{mc_latency}")
        newEmbedMC.add_field(name="**IP**", value = "158.62.204.28")
        if mc_player_count == 0:
            newEmbedMC.add_field(name="**Online Players:**", value ="No one is online.")
        if mc_player_count > 0:
            mc_query = mc_server.query() 
            #mc_players = '\n'.join(mc_query.players.names)
            newEmbedMC.add_field(name="**Online Players:**", value = "__{0}__".format("\n".join(mc_query.players.names)))
        time_now = datetime.now()
        time_formatted = time_now.strftime("%d/%m/%Y %H:%M:%S")
        newEmbedMC.set_footer(text=f"Last Updated: {time_formatted}")
        
        await mcmessage.edit(embed = newEmbedMC)
 
    # ----------------------------------
    

def setup(client):
    client.add_cog(status(client))

import discord
import asyncio
import requests

import matplotlib.pyplot as plt
import numpy as np

from datetime import datetime, timedelta
from bs4 import BeautifulSoup

import valve.source
from valve.source.a2s import ServerQuerier

from discord.ext import commands, tasks

from mcstatus import MinecraftServer

from dpytools.checks import *
import cchardet


ttt_server = ("208.103.169.70", 27021)
tf2_server = ("131.153.29.243", 27015)
mc_server = MinecraftServer.lookup("158.62.204.28:25565")

ecolor = 0xe91e63

class status(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        #self.selfTTT.start()
        #self.selfMC.start()
    
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
                    players.append("__" + player["name"] + "__")
                
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
        time_formatted = time_now.strftime("%m/%d/%Y at %H:%M:%S")
        em.set_footer(text=f"Last Updated: {time_formatted}")
        await ctx.send(embed = em)
        
    @commands.command(aliases=['statusTF2','TF2Status','tf2status'])
    async def statustf2(self, ctx):
        try:
            with ServerQuerier(tf2_server) as server:

                tf2_info = server.info()
                tf2_players = server.players()

                players = []
                for player in server.players()["players"]:
                    players.append("__" + player["name"] + "__")
                
                player_count = len(players)
                tf2_map = server.info()["map"]
                max_players = server.info()["max_players"]

        except valve.source.NoResponseError:
            await ctx.send(f"``Server {tf2_server[0]}:{tf2_server[1]} timed out!  No Response.``")
            return 0

        em = discord.Embed(title="**{server_name}**".format(**tf2_info), color=ecolor)
        em.set_thumbnail(url="https://i.imgur.com/eUgcNDX.png")
        em.add_field(name="**Map**", value=f"{tf2_map}", inline=True)
        em.add_field(name="**Player Count**", value=f"{player_count}/{max_players}", inline=True)
        em.add_field(name="**Connect**", value="[[Connect]](https://tinyurl.com/36x3a6ns)", inline=True)

        if (player_count == 0):
            em.add_field(name="**Online Players**", value = "No one is online.", inline=True)

        if (player_count > 0):
            playerString = '\n'.join(players)
            em.add_field(name="**Online Players**", value = playerString, inline=True)

        time_now = datetime.now()
        time_formatted = time_now.strftime("%m/%d/%Y at %H:%M:%S")
        em.set_footer(text=f"Last Updated: {time_formatted}")
        await ctx.send(embed=em)



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
    
    #@commands.command()
    #@only_these_users(736309573924683917,290926756397842432)
    #async def initTTT(self, ctx): 
    #    
    #    await self.client.wait_until_ready() 
    #    requests_session = requests.Session()
    #    html = requests_session.get("https://www.battlemetrics.com/servers/gmod/11437227").text
    #    soup = BeautifulSoup(html, "lxml")
    #    server_name = soup.find("h2", {'class':"css-u0fcdd"}).text
    #    player_count = soup.find("dt", text="Player count").findNext("dd").string
    #    curMap = soup.find("dt", text="Map").findNext("dd").string
    #    address = soup.find("dt", text="Address").findNext("span").text
    #    servStatus = soup.find("dt", text="Status").findNext("dd").string
    #    if servStatus == "online":
    #        servStatus = "Online"
    #    servRank = soup.find("dt", text="Rank").findNext("dd").string
    #    country = soup.find("dt", text="Country").findNext("dd").string
    #    tttInit = discord.Embed(title=f"**{server_name}**", color=ecolor)
    #    tttInit.set_thumbnail(url="https://i.imgur.com/eUgcNDX.png")
    #    tttInit.add_field(name="**Map**", value=curMap, inline=True)
    #    tttInit.add_field(name="**Player Count**", value=player_count, inline=True)
    #    tttInit.add_field(name="**Connect**", value="[[Connect]](https://tinurl.com/syw85zst)", inline=True)
    #    tttInit.add_field(name="**Status**", value=servStatus, inline=True)
    #    tttInit.add_field(name="**Rank**", value=servRank, inline=True)
    #    tttInit.add_field(name="**Address**", value=address, inline=True)
    #    tttInit.add_field(name="**Online Players**", value="WIP", inline=True) 
    #   
    # 
    #    time_now = datetime.now()
    #    time_formatted = time_now.strftime("%m/%d/%Y %H:%M:%S")
    #    tttInit.set_footer(text=f"Last Updated: {time_formatted}")
    #
    #    tttmessage = await ctx.send(embed=tttInit)
    #    
    #    self.selfTTT.start(tttmessage)
    #    #await self.selfTTT(tttmessage)


    
    #@tasks.loop(minutes=1.0)
    #async def selfTTT(self, msg):
    #    try: 
    #        await self.client.wait_until_ready() 
    #        requests_session = requests.Session()
    #        page = requests_session.get("https://www.battlemetrics.com/servers/gmod/11437227").text
    #        soup = BeautifulSoup(page, "lxml")
    #        server_name = soup.find("h2", {"class": "css-u0fcdd"}).text
    #        player_count = soup.find("dt", text="Player count").findNext("dd").string
    #        curMap = soup.find("dt", text="Map").findNext("dd").string
    #        address = soup.find("dt", text="Address").findNext("span").text
    #        servStatus = soup.find("dt", text="Status").findNext("dd").string
    #        if servStatus == "online":
    #            servStatus = "Online"
    #        servRank = soup.find("dt", text="Rank").findNext("dd").string
    #        country = soup.find("dt", text="Country").findNext("dd").string
    #        newTTT = discord.Embed(title=f"**{server_name}**", color=ecolor)
    #        newTTT.set_thumbnail(url="https://i.imgur.com/eUgcNDX.png")
    #        newTTT.add_field(name="**Map**", value=curMap, inline=True)
    #        newTTT.add_field(name="**Player Count**", value=player_count, inline=True)
    #        newTTT.add_field(name="**Connect**", value="[[Connect]](https://tinurl.com/syw85zst)", inline=True)
    #        newTTT.add_field(name="**Status**", value=servStatus, inline=True)
    #        newTTT.add_field(name="**Rank**", value=servRank, inline=True)
    #        newTTT.add_field(name="**Address**", value=address, inline=True)
    #        newTTT.add_field(name="**Online Players**", value="WIP", inline=True)
    #    
    #        
    #        time_now = datetime.now()
    #        time_formatted = time_now.strftime("%m/%d/%Y %H:%M:%S")
    #        newTTT.set_footer(text=f"Last Updated: {time_formatted}")
    #        await msg.edit(embed=newTTT)
    #    except:
    #        pass



    @commands.command()
    @only_these_users(736309573924683917,290926756397842432)
    # what this command does is it initializes a status embed message to a channel and then auto refreshes it
    async def initTTT(self, ctx):
        
        await self.client.wait_until_ready()
        
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

        initEmbedTTT = discord.Embed(title="**{server_name}**".format(**ttt_info), color = ecolor)
        initEmbedTTT.set_thumbnail(url="https://i.imgur.com/eUgcNDX.png")
        initEmbedTTT.add_field(name="**Map**", value=f"{ttt_map}", inline=True)
        initEmbedTTT.add_field(name="**Player Count**", value=f"{player_count}/{max_players}", inline=True)
        initEmbedTTT.add_field(name="**Connect**", value="[[Connect]](https://tinyurl.com/syw85zst)", inline=True)
        
        # states if players are online, and if they are, their usernames
        if (player_count == 0):
            initEmbedTTT.add_field(name="**Online Players**", value="No one is online.", inline=True)
        
        if (player_count > 0):
            playerString = '\n'.join(players)
            initEmbedTTT.add_field(name="**Online Players**", value= playerString, inline=True)
        
        #html = requests.get('https://www.gametracker.com/server_info/208.103.169.70:27021/').text
        #soup = BeautifulSoup(html, 'html.parser')
        #img_tag = soup.find('img', {"class": "item_260x170"})
        #image = img_tag['src']
        #initEmbedTTT.set_image(url="https:" + image)
        
        
        now = datetime.now().date()
        yesterday = now - timedelta(days=1)
        url = 'https://api.battlemetrics.com/servers/11437227'
        player_data_request = requests.get(url + f'/player-count-history?start={yesterday.year:04d}-{yesterday.month:02d}-{yesterday.day:02d}T12%3A00%3A00Z&stop={now.year:04d}-{now.month:02d}-{now.day:02d}T12%3A00%3A00Z&resolution=60')
        #print(player_data_request)
        
        time_stamps = []
        player_counts = []
        for date in player_data_request.json()['data']:
            time_stamps.append(date['attributes']['timestamp'])
            player_counts.append(date['attributes']['value'])
        
        #print(time_stamps)
        #print(player_counts)
        
        #xpoints = np.array(time_stamps)
        xpoints = time_stamps
        #ypoints = np.array(player_counts)
        ypoints = player_counts
        #plt.plot(time_stamps,player_counts)
        plt.plot(xpoints, ypoints)
        plt.grid()
        #plt.savefig('player_count_history.png')
        plt.savefig('/root/ChaoticBot/bot/cogs/player_count_history.png')
        
        graph = discord.File("/root/ChaoticBot/bot/cogs/player_count_history.png", filename="graph.png")
        initEmbedTTT.set_image(url="attachment://graph.png")
    
        time_now = datetime.now()
        time_formatted = time_now.strftime("%m/%d/%Y %H:%M:%S")
        initEmbedTTT.set_footer(text=f"Last Updated: {time_formatted}")
  
        tttmessage = await ctx.send(file = graph, embed = initEmbedTTT)

    
        try:
            self.selfTTT.start(tttmessage)
        except RuntimeError:
            await tttmessage.delete() 
            await ctx.send(f"{ctx.author.mention}, TTT status is already running elsewhere (if this is not the case, contact Joker).")

    @tasks.loop(minutes=1.0)
    # this is the looping task for any initialized status message using the command above
    async def selfTTT(self, msg):    
        await self.client.wait_until_ready()
        # Queries the TTT server based on its IP and port
        try:
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

            #html = requests.get('https://www.gametracker.com/server_info/208.103.169.70:27021/').text
            #soup = BeautifulSoup(html, 'html.parser')
            #img_tag = soup.find('img', {"class": "item_260x170"})
            #image = img_tag['src']
            #newEmbedTTT.set_image(url="https:" + image)

            now = datetime.now().date()
            yesterday = now - timedelta(days=1)
            url = 'https://api.battlemetrics.com/servers/11437227'
            player_data_request = requests.get(url + f'/player-count-history?start={yesterday.year:04d}-{yesterday.month:02d}-{yesterday.day:02d}T12%3A00%3A00Z&stop={now.year:04d}-{now.month:02d}-{now.day:02d}T12%3A00%3A00Z&resolution=60')
            #print(player_data_request)
        
            time_stamps = []
            player_counts = []
            for date in player_data_request.json()['data']:
                time_stamps.append(date['attributes']['timestamp'])
                player_counts.append(date['attributes']['value'])
        
            #print(time_stamps)
            #print(player_counts)
        
            #xpoints = np.array(time_stamps)
            xpoints = time_stamps
            #ypoints = np.array(player_counts)
            ypoints = player_counts
            #plt.plot(time_stamps,player_counts)
            plt.plot(xpoints, ypoints)
            plt.grid()
            #plt.savefig('player_count_history.png')
            plt.savefig('/root/ChaoticBot/bot/cogs/player_count_history.png')
            
            graph = discord.File("/root/ChaoticBot/bot/cogs/player_count_history.png", filename="graph.png")
            newEmbedTTT.set_image(url="attachment://graph.png")
 
                
            time_now = datetime.now()
            time_formatted = time_now.strftime("%m/%d/%Y %H:%M:%S")
            newEmbedTTT.set_footer(text=f"Last Updated: {time_formatted}")
    
            await msg.edit(embed = newEmbedTTT)

        except:
            pass

    
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

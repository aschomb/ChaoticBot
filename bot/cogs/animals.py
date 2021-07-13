import discord
import aiohttp
import random
import time
#import sys
import os
from discord.ext import commands

# embed color
ecolor = 0xe91e63

# more random, random seed
t = int(time.time() * 1000.0)
random.seed(((t & 0xff000000) >> 24) + ((t & 0x00ff0000) >>  8) + ((t & 0x0000ff00) <<  8) + ((t & 0x000000ff) << 24))

#sys.path.append('/root/ChaoticBot/bot/cogs')
#import exceptions

class animals(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    # one command for all of the animals, can be used 2 times ever 2 seconds
    @commands.cooldown(2.0,2.0,commands.BucketType.user)
    @commands.command()
    async def animal(self, ctx, *, an):
        animals = ["cat","dog","lizard","duck","fox","panda","redpanda","red panda","bird","birb","kangaroo","frog","raccoon","rabbit","bunny"]        
        async with aiohttp.ClientSession() as req:
        
        # ----- API Animals -----
            if (an.lower() == "cat"):
                async with req.get('https://some-random-api.ml/img/cat') as cat:
                    cat = await cat.json()
                    await req.close()
                    em = discord.Embed(title=f"Cat Requested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=cat['link']))

            if (an.lower() == "dog"):
                async with req.get('https://some-random-api.ml/img/dog') as dog:
                    dog = await dog.json()
                    await req.close()
                    em = discord.Embed(title=f"Dog requested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=dog['link']))
                    
            if (an.lower() == "lizard"):
                async with req.get('https://nekos.life/api/lizard') as lizard:
                    lizard = await lizard.json()
                    await req.close()
                    em = discord.Embed(title=f"Lizard requested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=lizard['url']))

            if (an.lower() == "duck"):
                async with req.get('https://random-d.uk/api/v1/random') as duck:
                    duck = await duck.json()
                    await req.close()
                    em = discord.Embed(title=f"Duck requested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=duck['url']))

            if (an.lower() == "fox"):
                async with req.get('https://some-random-api.ml/img/fox') as fox:
                    fox = await fox.json()
                    await req.close()
                    em = discord.Embed(title=f"Fox requested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=fox['link']))

            if (an.lower() == "panda"):
                async with req.get('https://some-random-api.ml/img/panda') as panda:
                    panda = await panda.json()
                    await req.close()
                    em = discord.Embed(title=f"Panda requested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=panda['link']))

            if ((an.lower() == "red panda") or (an.lower() == "redpanda")):
                async with req.get('https://some-random-api.ml/img/red_panda') as redpanda:
                    redpanda = await redpanda.json()
                    await req.close()
                    em = discord.Embed(title=f"Red Panda requested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=redpanda['link']))

            if (an.lower() == "koala"):
                async with req.get('https://some-random-api.ml/img/koala') as koala:
                    koala = await koala.json()
                    await req.close()
                    em = discord.Embed(title=f"Koala requested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=koala['link']))

            if ((an.lower() == "bird") or (an.lower() ==  "birb")):
                async with req.get('https://some-random-api.ml/img/birb') as birb:
                    birb = await birb.json()
                    await req.close()
                    em = discord.Embed(title=f"Bird reqested by {ctx.author.display_name}:", color=ecolor)
                    await ctx.send(embed = em.set_image(url=birb['link']))
            # ----------------------

                
            # ----- File Animals -----
            if (an.lower() == "kangaroo"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/images/kangaroo/')
                random_image = random.choice(image)
                kangarooImg = discord.File("/root/ChaoticBot/bot/images/kangaroo/" + random_image, filename="kangImg.jpg")
                em = discord.Embed(title=f"Kangaroo requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://kangImg.jpg")
                await ctx.send(file = kangarooImg, embed=em)

            if (an.lower() == "frog"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/images/frogs/')
                random_image = random.choice(image)
                frogImg = discord.File("/root/ChaoticBot/bot/images/frogs/"  + random_image, filename="frImg.jpg")
                em = discord.Embed(title=f"Frog requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://frImg.jpg")
                await ctx.send(file = frogImg, embed=em)

            if (an.lower() == "raccoon"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/images/raccoons')
                random_image = random.choice(image)
                raccoonImg = discord.File("/root/ChaoticBot/bot/images/raccoons/" + random_image, filename="raccImg.jpg")
                em = discord.Embed(title=f"Raccoon requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://raccImg.jpg")
                await ctx.send(file = raccoonImg, embed=em)

            if ((an.lower() == "rabbit") or (an.lower() == "bunny")):
                if (an.lower() == "rabbit"):
                    aname = "Rabbit"
                    em = discord.Embed(title=f"Rabbit requested by {ctx.author.display_name}:", color=ecolor)
                if (an.lower() == "bunny"):
                    aname = "Bunny"
                    em = discord.Embed(title=f"Bunny requested by {ctx.author.display_name}:", color=ecolor)
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/images/rabbits/')
                random_image = random.choice(image)
                rabbitImg = discord.File("/root/ChaoticBot/bot/images/rabbits/" + random_image, filename="rabbImg.jpg")
                em.set_image(url="attachment://rabbImg.jpg")
                await ctx.send(file = rabbitImg, embed=em)

            if (an.lower() == "penguin"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/images/penguins')
                random_image = random.choice(image)
                penguinImg = discord.File("/root/ChaoticBot/bot/images/penguins/" + random_image, filename="penImg.jpg")
                em = discord.Embed(title=f"Penguin requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://penImg.jpg")
                await ctx.send(file = penguinImg, embed=em)

            if (an.lower() == "axolotl"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/images/axolotl')
                random_image = random.choice(image)
                axolotlImg = discord.File("/root/ChaoticBot/bot/images/axolotl/" + random_image, filename="axImg.jpg")
                em = discord.Embed(title=f"Axolotl requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://axImg.jpg")
                await ctx.send(file = axolotlImg, embed=em)
            # -----------------------

    @animal.error
    async def animal_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(ctx.author.mention)
            em = discord.Embed(title=f"Command is on cooldown", description=f"Try again in {error.retry_after:.2f}s")
            await ctx.send(embed=em)

def setup(client):
    client.add_cog(animals(client))
    

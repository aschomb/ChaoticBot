import discord, aiohttp, random, os
from discord.ext import commands
ecolor = 0xe91e63
random.seed()

class animals(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.cooldown(2.0,2.0,commands.BucketType.user)
    @commands.command()
    async def animal(self, ctx, *, an):
        async with aiohttp.ClientSession() as req:
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

            if (an.lower() == "kangaroo"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/cogs/kangaroo/')
                random_image = random.choice(image)
                kangarooImg = discord.File("/root/ChaoticBot/bot/cogs/kangaroo/" + random_image, filename="kangImg.jpg")
                em = discord.Embed(title=f"Kangaroo requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://kangImg.jpg")
                #await ctx.send(f"Kangaroo requested by {ctx.author.display_name}:")
                #await ctx.send(file=kangarooImg)
                await ctx.send(file = kangarooImg, embed=em)


            if (an.lower() == "frog"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/cogs/frogs/')
                random_image = random.choice(image)
                frogImg = discord.File("/root/ChaoticBot/bot/cogs/frogs/"  + random_image, filename="frImg.jpg")
                em = discord.Embed(title=f"Frog requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://frImg.jpg")
                #await ctx.send(f"Frog requested by {ctx.author.display_name}:")
                #await ctx.send(file=frogImg)
                await ctx.send(file = frogImg, embed=em)

            if (an.lower() == "raccoon"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/cogs/raccoons')
                random_image = random.choice(image)
                raccoonImg = discord.File("/root/ChaoticBot/bot/cogs/raccoons/" + random_image, filename="raccImg.jpg")
                em = discord.Embed(title=f"Raccoon requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://raccImg.jpg")
                #await ctx.send(f"Raccoon requested by {ctx.author.display_name}:")
                #await ctx.send(file=raccoonImg)
                await ctx.send(file = raccoonImg, embed=em)

            if ((an.lower() == "rabbit") or (an.lower() == "bunny")):
                if (an.lower() == "rabbit"):
                    aname = "Rabbit"
                    em = discord.Embed(title=f"Rabbit requested by {ctx.author.display_name}:", color=ecolor)
                if (an.lower() == "bunny"):
                    aname = "Bunny"
                    em = discord.Embed(title=f"Bunny requested by {ctx.author.display_name}:", color=ecolor)
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/cogs/rabbits/')
                random_image = random.choice(image)
                rabbitImg = discord.File("/root/ChaoticBot/bot/cogs/rabbits/" + random_image, filename="rabbImg.jpg")
                em.set_image(url="attachment://rabbImg.jpg")
                #await ctx.send(f"{aname} requested by {ctx.author.display_name}:")
                #await ctx.send(file=rabbitImg)
                await ctx.send(file = rabbitImg, embed=em)

            if (an.lower() == "penguin"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/cogs/penguins')
                random_image = random.choice(image)
                penguinImg = discord.File("/root/ChaoticBot/bot/cogs/penguins/" + random_image, filename="penImg.jpg")
                em = discord.Embed(title=f"Penguin requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://penImg.jpg")
                #await ctx.send(f"Penguin requested by {ctx.author.display_name}:")
                #await ctx.send(file=penguinImg)
                await ctx.send(file = penguinImg, embed=em)

            if (an.lower() == "axolotl"):
                await req.close()
                image = os.listdir('/root/ChaoticBot/bot/cogs/axolotl')
                random_image = random.choice(image)
                axolotlImg = discord.File("/root/ChaoticBot/bot/cogs/axolotl/" + random_image, filename="axImg.jpg")
                em = discord.Embed(title=f"Axolotl requested by {ctx.author.display_name}:", color=ecolor)
                em.set_image(url="attachment://axImg.jpg")
                #await ctx.send(f"Axolotl requested by {ctx.author.display_name}:")
                #await ctx.send(file=axolotlImg)
                await ctx.send(file = axolotlImg, embed=em)

    @animal.error
    async def animal_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(ctx.author.mention)
            em = discord.Embed(title=f"Command is on cooldown", description=f"Try again in {error.retry_after:.2f}s")
            await ctx.send(embed=em)

def setup(client):
    client.add_cog(animals(client))
    

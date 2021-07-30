import discord
import random
import time
import numpy as np
import numba as nb
from sympy import *
import sympy as sp

from discord.ext import commands

ecolor = 0xe91e63

t = int( time.time() * 1000.0 )
random.seed( ((t & 0xff000000) >> 24) + ((t & 0x00ff0000) >>  8) + ((t & 0x0000ff00) <<  8) + ((t & 0x000000ff) << 24)   )

class calculator(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    

    @commands.command(aliases=['ff','fourfunction','fourf','ffunction'])
    async def fourfunc(self, ctx, operation, *nums):
        if operation not in ['+', '-', '*', '/']:
            await ctx.send("Please type a valid operation type.")
        var =  f' {operation} '.join(nums)
        op: str 
        if operation == '+':
            op = "Addition"
        if operation == '-':
            op = "Subtraction"
        if operation == '/':
            op = "Division"
        
        em =  discord.Embed(title=f"{op} Calculator", color=ecolor)
        em.add_field(name=f"Requested by {ctx.author.display_name}", value=f"{var} = {eval(var)}", inline=True)
        await ctx.send(embed=em)
     
    @commands.command()
    async def factor(self, ctx, num: int):
        if (num < 1000000):
            factors = [x for x in range(2, num//2+1) if num%x == 0]
            em = discord.Embed(title="Simple Factor Calculator", color=ecolor)
            em.add_field(name=f"Requested by {ctx.author.display_name}", value = f"**Factors of {num}:** \n{factors}", inline=True)
            await ctx.send(embed = em)
        else:
            await ctx.send(f"{ctx.author.mention}, use a smaller integer.")
   
    @commands.command()
    async def derive(self, ctx, *, equation):
        x = sp.Symbol('x')
        f = sp.sympify(equation)
        f_prime = f.diff(x)
        em = discord.Embed(title="Derivative Calculator", color=ecolor)
        em.add_field(name=f"Requested by {ctx.author.display_name}", value = f"Derivative of {f}: \n{f_prime}", inline=True)
        await ctx.send(embed = em)
        #await ctx.send(f_prime)





def setup(client):
    client.add_cog(calculator(client))

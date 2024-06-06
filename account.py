import random
import time
import discord
from discord.ext import commands
import json


class Account(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Account cog loaded!")
    
    @commands.command()
    async def me(self, ctx: commands.Context, user: discord.Member=None):
        if user == None: user = ctx.author
        with open("./db/stats.json") as f:
            db = json.load(f)
#             db[message.author.mention]["nac"]
# db[message.author.mention]["swear"]
# db[message.author.mention]["good"]
# db[message.author.mention]["neutr"]
# db[message.author.mention]["vata"
            desc = f"# {user.mention} STATS:\nПоказник Нациста: {db[user.mention]['nac']}\nПоказник Сапожніка: {db[user.mention]['swear']}\nДоброта: {db[user.mention]['good']}\
                \nНейтралітет: {db[user.mention]['neutr']}\nПоказник Ватніка: {db[user.mention]['vata']}"
            emb = discord.Embed(colour=discord.Colour.random(seed=time.time()), title=f"Social credit", description=desc)
            await ctx.send(embed=emb)
import random
import discord
from discord.ext import commands
import chatgpt

user = "belkalox"

class Testing(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Testing cog loaded!")

    @commands.command()
    async def status(self, ctx: commands.Context, memb: discord.Member):
        await ctx.reply(f"Member ID: {memb.id}\nStatus: {memb.status}")

    @commands.command()
    async def send(self, ctx: commands.Context):
        msg = await ctx.send(f"Channel: {ctx.channel.id}")
        await ctx.send(content=msg.id, delete_after=10)
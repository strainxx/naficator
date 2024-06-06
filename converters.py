import random
import discord
from discord.ext import commands

bad = ["кароче", "тіпа", "курчик", "курде", "ето", "курва"]

def generate_shizo(arg):
    b = ""
    for i in arg:
        if i.upper() == "Э" or i.upper() == "Є":
            i = "е"
        if i.upper() == "Ы" or i.upper() == "И":
            i = "і"
        if random.randint(1, 15) == random.randint(1, 15):
            i = "ы"
        if i == " " and random.randint(1, 5) == 5:
            i = f" {random.choice(bad)} "
        b+=i
    return b

class Converters(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Converters cog loaded!")

    @commands.command()
    async def zovify(self, ctx: commands.Context, *, arg: str):
        print(f"{ctx.author.display_name} called ZOV!!!")
        b = ""
        for i in arg:
            if i.upper() == "З" or i.upper() == "С":
                i = "Z"
            if i.upper() == "O" or i.upper() == "0":
                i = "O"
            if i.upper() == "В":
                i = "V"
            b+=i
        await ctx.reply(b)

    @commands.command()
    async def ukr(self, ctx: commands.Context, *, arg: str):
        print(f"{ctx.author.display_name} called UKR 🇺🇦🇺🇦🇺🇦!!!")
        b = generate_shizo(arg)
        await ctx.reply(b)
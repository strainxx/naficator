import random
import string
import discord
from discord.ext import commands
import requests

answers = ["Нэт", "ДА", "Поч не солов'їною", "ти укр", "фу рососія", "чувачело youtube", "пацюк", "xoxol", "підор", "курва", "курчик", "курдe", "польща",
           "СВО", "війна", "навальний", "был в польше", "новальний", "двы форми слова", "жид", "ЗСУ", "ВСРФ", "Слава", "Росії", "Україні",
           "maxmnull", "trisha", "1488"]

def generate_ukr():
    return " ".join([random.choice(answers) for i in range(random.randint(1, 10))])

class AI(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("AI cog loaded!")


    @commands.command()
    async def ukrgpt(self, ctx: commands.Context, *, arg):
        await ctx.reply(generate_ukr())

    @commands.command()
    async def midchornii(self, ctx: commands.Context, *, arg):
        url = ""
        message = await ctx.reply("Generating image with UKR AI 🇺🇦🇺🇦🇺🇦")
        while True:
            url = f"https://i.imgur.com/{''.join([random.choice(string.ascii_lowercase+string.digits+string.ascii_uppercase) for i in range(5)])}.jpg"
            # r = requests.get(url).text
            # title = r[r.find('<title>') + 7 : r.find('</title>')]
            # print(title)
            break
            # if r == 429: break
        await message.edit(content=url)
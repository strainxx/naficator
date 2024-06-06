import random
import discord
from discord.ext import commands
import chatgpt
from api import jaccard
import json

z = "Заглыт))0"

swears = ["курва", "даун", "підор", "сука", "хуй", "хуєсос", "лох",]
vata = ["хохол", "укр", "іпсо"]
nac = ["гітлер", "пасхалка", "адольф", "1488"]
good = ["харош", "красава", "топ", "круто"]
neutr = ["похуй", "насрать", "поєбать", "ічо"]

min_j = 0.6

class Handlers(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Handlers cog loaded!")
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.name == z:
            await message.reply(chatgpt.generate_ukr())
        elif not message.author.bot:
            if message.content != "":
                with open(f"./db/stats.json", "r") as f:
                    db = json.load(f)
                    naci_koef = 0
                    swear_koef = 0
                    good_koef = 0
                    neutral_koef = 0
                    vata_koef = 0
                    try:
                        naci_koef = db[message.author.mention]["nac"]
                        swear_koef = db[message.author.mention]["swear"]
                        good_koef = db[message.author.mention]["good"]
                        neutral_koef = db[message.author.mention]["neutr"]
                        vata_koef = db[message.author.mention]["vata"]
                    except: pass

                    for word in message.content.split():
                        for swear in swears:
                            if jaccard.jaccard(word, swear) >= min_j:
                                swear_koef+=0.05
                        for vat in vata:
                            if jaccard.jaccard(word, vat) >= min_j:
                                vata_koef+=0.05
                        for n in nac:
                            if jaccard.jaccard(word, n) >= min_j:
                                naci_koef+=0.05
                        for g in good:
                            if jaccard.jaccard(word, g) >= min_j:
                                good_koef+=0.05
                        for neut in neutr:
                            if jaccard.jaccard(word, neut) >= min_j:
                                neutral_koef+=0.05

                    db[message.author.mention] = {
                        "nac": naci_koef,
                        "swear": swear_koef,
                        "good": good_koef,
                        "neutr": neutral_koef,
                        "vata": vata_koef
                    }
                    with open(f"./db/stats.json", "w") as wf:
                        json.dump(db, wf, ensure_ascii=False, indent=4)
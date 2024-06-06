import asyncio
import datetime
import random
import time
import discord
from discord.ext import commands, tasks
from collections import Counter
import converters
import chatgpt
import handlers
import testing
from datetime import date
import admin
import account
import requests
import player

imgs = ["https://gas-kvas.com/uploads/posts/2023-02/1675274093_gas-kvas-com-p-belka-art-risunok-8.jpg", "https://i.ytimg.com/vi/W2_Y3DMv7_U/hqdefault.jpg",
        "https://i.tlauncher.org/images/637107729865797404.png", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ8gwWruzZeYRefmBfRCeGy-S-VnNgTRbwbC6paYmb6TLQ02cFsDx1sBsC4MYlygoKeHlU&usqp=CAU",
        "https://ru-minecraft.ru/uploads/posts/2013-12/1387900700_zkvjt9m.png", "https://images.prom.ua/4085237298_w640_h640_pryaniki-na-palochke.jpg",
        "https://static.gameloop.com/img/28990ce1577b06b52603182494fcda0e.jpg?imageMogr2/thumbnail/undefinedx266/format/webp", "https://images.prom.ua/1057659411_w600_h600_1057659411.jpg"]
act = discord.Streaming(name="гастрономічний сушик | n!help", url="https://www.youtube.com/watch?v=vASaetH9zXU")

bckup = []

bot = commands.Bot(command_prefix="n!", intents=discord.Intents.all(), activity=act, status=discord.Status.do_not_disturb, help_command=None)
vc = None
msgB = None
mid = 1218227986281664573
init = False

@bot.event
async def on_ready():
    global init, vc, mid, msgB
    if not init:
        print("Starting...")
        print("FREEBELKA V1")
        # vc = await bot.fetch_channel(1218227667481006203)
        # msgB = await bot.get_channel(1218214712894947350).fetch_message(mid)
        print("Loading cogs")
        await bot.add_cog(converters.Converters(bot))
        await bot.add_cog(chatgpt.AI(bot))
        await bot.add_cog(handlers.Handlers(bot))
        await bot.add_cog(admin.Entry(bot))
        await bot.add_cog(account.Account(bot))
        await bot.add_cog(player.Player(bot))
        print("Started!")
        init = True

# Channel: 1218214712894947350
# 1218227986281664573
n = 0
lastOnline = "давно"

class HelpV(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.select(cls=discord.ui.Select, options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                label="AI",
                description="Безплатний доступ до укржпт 4"
            ),
            discord.SelectOption(
                label="Converters",
                description="Zрада неізбєна"
            ),
            discord.SelectOption(
                label="Дитяче порєво",
                description="👆👆👆👆🤟✅✅✅"
            )
        ])
    async def select_call(self, interaction: discord.Interaction, select,):
        emb = discord.Embed(title=f"Category: {select.values[0]}")
        emb.set_image(url=bot.user.avatar.url)
        if select.values[0] == "AI":
            emb.description = "## n!ukrgpt {prompt}- іі настоящій версія 4\n## n!midchornii {prompt} - мідчорній генерує кортінкі сушика"
        if select.values[0] == "Converters":
            emb.description = "## n!zovify {prompt}- ZV ZV СВО СВО\n## n!ukr {prompt} - ти укр"
        if select.values[0] == "Дитяче порєво":
            emb.description = f"# Данні успішно передані в поліцію!\n# @everyone {interaction.user.mention} вибрав Дитяче порєво!"
        return await interaction.response.send_message(embed=emb, delete_after=15)

@bot.command()
async def help(ctx: commands.Context):
    emb = discord.Embed(colour=discord.Colour.red(), title=f"{bot.user.display_name} Help", description="# Select category:\n\t## AI - іскуствєний інтілєкт чатгіпіті 4\n\t\
                        ## Converters - категOрія для ZиVчикіV ы уркыв\n\t## І всьо кароче")
    emb.set_image(url=bot.user.avatar.url)
    await ctx.send(embed=emb, view=HelpV(), delete_after=15)

@tasks.loop(seconds=60)
async def task_loop(ctx: commands.Context ,memb: discord.Member):
    global n, msgB, lastOnline, imgs
    n+=1
    bid = 852878630622855178
    today = datetime.datetime.now()
    d2 = today.strftime("%d/%m/%Y %H:%M:%S")
    if memb.status != discord.Status.offline and lastOnline == "давно":
        await ctx.send("@everyone БЄЛКА ЖИВИЙ!!")
        lastOnline = d2
    emb = discord.Embed(color=discord.Colour.dark_gold(), title="#FREEBELKA", description=f"Польскі омони випустіть бєлку пежее\n# Status: {memb.status}\n## Refreshed: {d2}\n# Last online: {lastOnline}")
    emb.set_footer(text="тэбя омоны били")
    emb.set_image(url=random.choice(imgs))
    # await msgB.edit(content=f"Free Belka from польскі омони\n--Status: {memb.status}\n--Date: {d2}\nLast online: {lastOnline}")
    await msgB.edit(content="", embed=emb)
    await vc.edit(name=f"BELKA: {memb.status}")
    print(f'Refreshed {n} times', end='\r')
    
@bot.command()
async def test(ctx: commands.Context, user: discord.Member):
    # task_loop.start(ctx, user)
    pass

@bot.command()
async def nuke_server(ctx: commands.Context):
    msg = await ctx.reply(content=f"ACTIVATED NUKE...")
    for i in range(10, 0, -1):
        await msg.edit(content=f"{i}...")
        await asyncio.sleep(1)
    await ctx.send("NUKING SERVER!!!!")
    for ch in ctx.guild.channels:
        bckup.append(ch.name)
        await ch.edit(name=converters.generate_shizo(ch.name))
        await asyncio.sleep(1)

@bot.command()
async def backup_nuke(ctx: commands.Context):
    emb = discord.Embed(title="Backing up...", description=f"### Progress:\n0/{len(bckup)}")
    msg = await ctx.send(embed=emb)
    i = 0
    for ch in ctx.guild.channels:
        emb.description = f"### Progress:\n{i+1}/{len(bckup)}"
        await ch.edit(name=bckup[i])
        await msg.edit(embed=emb)
        await asyncio.sleep(1)
        i+=1

@bot.command()
async def rn(ctx: commands.Context, *, newname: str):
    await ctx.message.delete()
    await ctx.guild.edit(name=newname)

@bot.command()
async def spfp(ctx: commands.Context, url: str):
    await ctx.message.delete()
    await ctx.guild.edit(icon=requests.get(url).content)

@bot.command()
async def sync(ctx: commands.Context):
    await ctx.reply(f"Synced {len(await bot.tree.sync())} commands!")

@bot.command()
async def load_testing(ctx: commands.Context):
    msg = await ctx.reply("🪐 Loading testing cog...")
    await bot.add_cog(testing.Testing(bot))
    # vc = await ctx.guild.create_voice_channel(f"BELKA: offline", position=0, user_limit=69)
    # await msg.edit(content=f"Loaded testing cog!\nVC ID: {vc.id}",delete_after=10)

bot.run()
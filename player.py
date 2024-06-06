import random
import discord
from discord.ext import commands
import converters

FFOPT = {'options': '-vn'}

class Player(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Play cog loaded!")

    @discord.app_commands.command(name="play_video", description="Сексапільні тьоті не тут ⛔⛔⛔")
    async def play_video(self, interaction: discord.Interaction, video: discord.Attachment):
        vc = await interaction.user.voice.channel.connect()
        await interaction.response.send_message(content="Соскі сосіскі рлау")
        await video.save("temp.mp4")
        vc.play(discord.FFmpegPCMAudio(source="temp.mp4", **FFOPT))
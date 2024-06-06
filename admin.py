import random
import discord
from discord.ext import commands
import chatgpt

class MenuBtn(discord.ui.Button):
    def __init__(self, *, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None, row: int | None = None):
        super().__init__(style=style, label=label, disabled=disabled, custom_id=custom_id, url=url, emoji=emoji, row=row)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content=f"Hello {interaction.message.author.display_name}!",view=MainPanel())
        return await super().callback(interaction)


class DeleteBtn(discord.ui.Button):
    def __init__(self, *, deletable, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None, row: int | None = None):
        super().__init__(style=style, label=label, disabled=disabled, custom_id=custom_id, url=url, emoji=emoji, row=row)
        self.deletable = deletable
    async def callback(self, interaction: discord.Interaction):
        try:
            await self.deletable.delete()
            await interaction.response.edit_message(content=f"# DELETED!", view=MainPanel())
        except:
            await interaction.response.edit_message(content=f"# FAILED TO DELETE!", view=MainPanel())
        # await interaction.response.edit_message(content=f"# DELETED!", view=MainPanel())
        return await super().callback(interaction)
    
class KickBtn(discord.ui.Button):
    def __init__(self, *, deletable: discord.Member, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None, row: int | None = None):
        super().__init__(style=style, label=label, disabled=disabled, custom_id=custom_id, url=url, emoji=emoji, row=row)
        self.deletable = deletable
    async def callback(self, interaction: discord.Interaction):
        try:
            await self.deletable.kick(reason="ADMIN PANEL")
            await interaction.response.edit_message(content=f"# DELETED!", view=MainPanel())
        except:
            await interaction.response.edit_message(content=f"# FAILED TO DELETE!", view=MainPanel())
        # await interaction.response.edit_message(content=f"# DELETED!", view=MainPanel())
        return await super().callback(interaction)
    
class BanBtn(discord.ui.Button):
    def __init__(self, *, deletable: discord.Member, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None, row: int | None = None):
        super().__init__(style=style, label=label, disabled=disabled, custom_id=custom_id, url=url, emoji=emoji, row=row)
        self.deletable = deletable
    async def callback(self, interaction: discord.Interaction):
        try:
            await self.deletable.ban(reason="ADMIN PANEL", delete_message_days=0)
            await interaction.response.edit_message(content=f"# DELETED!", view=MainPanel())
        except:
            await interaction.response.edit_message(content=f"# FAILED TO DELETE!", view=MainPanel())
        # await interaction.response.edit_message(content=f"# DELETED!", view=MainPanel())
        return await super().callback(interaction)

class GiveBtn(discord.ui.Button):
    def __init__(self, *, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None, row: int | None = None):
        super().__init__(style=style, label=label, disabled=disabled, custom_id=custom_id, url=url, emoji=emoji, row=row)
        # TODO: Give role

class RoleMgmt(discord.ui.View):
    def __init__(self, role: discord.Role):
        super().__init__()
        self.role = role
        delbtn = DeleteBtn(label="Delete", style=discord.ButtonStyle.red, deletable=self.role)
        gvbtn = GiveBtn(label="Gimme", style=discord.ButtonStyle.green)
        mnbtn = MenuBtn(label="<< Menu", style=discord.ButtonStyle.gray)
        self.add_item(delbtn)
        self.add_item(gvbtn)
        self.add_item(mnbtn)

class UserMgmt(discord.ui.View):
    def __init__(self, role: discord.Role):
        super().__init__()
        self.role = role
        delbtn = BanBtn(label="Ban", style=discord.ButtonStyle.red, deletable=self.role)
        gvbtn = KickBtn(label="Kick", style=discord.ButtonStyle.green, deletable=self.role)
        mnbtn = MenuBtn(label="<< Menu", style=discord.ButtonStyle.gray)
        self.add_item(delbtn)
        self.add_item(gvbtn)
        self.add_item(mnbtn)

class ChanMgmt(discord.ui.View):
    def __init__(self, role: discord.Role):
        super().__init__()
        self.role = role
        delbtn = DeleteBtn(label="Delete", style=discord.ButtonStyle.red, deletable=self.role)
        mnbtn = MenuBtn(label="<< Menu", style=discord.ButtonStyle.gray)
        self.add_item(delbtn)
        self.add_item(mnbtn)

class RoleBtn(discord.ui.Button):
    def __init__(self, *, role: discord.Role, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None, row: int | None = None):
        super().__init__(style=style, label=label, disabled=disabled, custom_id=custom_id, url=url, emoji=emoji, row=row)
        self.role = role
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content=f"# EDITING ROLE {self.role.mention}", view=RoleMgmt(self.role))
        return await super().callback(interaction)

class RolesPanel(discord.ui.View):
    def __init__(self, interaction: discord.Interaction):
        super().__init__()
        for role in interaction.guild.roles:
            btn = RoleBtn(role=role, style=discord.ButtonStyle.blurple, label=role.name, disabled=(not role.is_assignable() and not role.is_default()))
            self.add_item(btn)

class ChanBtn(discord.ui.Button):
    def __init__(self, *, chan: discord.GroupChannel, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None, row: int | None = None):
        super().__init__(style=style, label=label, disabled=disabled, custom_id=custom_id, url=url, emoji=emoji, row=row)
        self.chan = chan
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content=f"# EDITING CHANNEL #{self.chan.name}", view=ChanMgmt(self.chan))
        return await super().callback(interaction)

class ChanPanel(discord.ui.View):
    def __init__(self, interaction: discord.Interaction):
        super().__init__()
        for chan in interaction.guild.channels:
            btn = ChanBtn(chan=chan, style=(discord.ButtonStyle.red if chan.is_nsfw() else discord.ButtonStyle.blurple), label=chan.name)
            self.add_item(btn)

class UserBtn(discord.ui.Button):
    def __init__(self, *, user: discord.Member, style: discord.ButtonStyle = discord.ButtonStyle.secondary, label: str | None = None, disabled: bool = False, custom_id: str | None = None, url: str | None = None, emoji: str | discord.Emoji | discord.PartialEmoji | None = None, row: int | None = None):
        super().__init__(style=style, label=label, disabled=disabled, custom_id=custom_id, url=url, emoji=emoji, row=row)
        self.user = user
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.edit_message(content=f"# EDITING USER #{self.user.mention}", view=UserMgmt(self.user))
        return await super().callback(interaction)

class UserPanel(discord.ui.View):
    def __init__(self, interaction: discord.Interaction):
        super().__init__()
        for user in interaction.guild.members:
            bstyle = discord.ButtonStyle.green
            if user.status == discord.Status.do_not_disturb: bstyle = discord.ButtonStyle.red
            if user.status == discord.Status.offline: bstyle = discord.ButtonStyle.gray
            if user.status == discord.Status.idle: bstyle = discord.ButtonStyle.blurple
            btn = UserBtn(user=user, style=bstyle, label=user.display_name)
            self.add_item(btn)


class MainPanel(discord.ui.View):
    def __init__(self):
        super().__init__()
        # roles = discord.ui.Button(label="Roles", style=discord.ButtonStyle.success)
        # roles.callback = 
        # self.add_item(roles)
    @discord.ui.button(label="Roles", style=discord.ButtonStyle.success)
    async def roles_callback(self, interaction: discord.Interaction, button):
        await interaction.response.edit_message(content="# Roles Panel", view=RolesPanel(interaction))

    @discord.ui.button(label="Users", style=discord.ButtonStyle.success)
    async def users_callback(self, interaction: discord.Interaction, button):
        await interaction.response.edit_message(content="User Panel", view=UserPanel(interaction))
        
    @discord.ui.button(label="Channels", style=discord.ButtonStyle.blurple)
    async def server_callback(self, interaction: discord.Interaction, button):
        await interaction.response.edit_message(content="Channels Panel", view=ChanPanel(interaction))
    
    @discord.ui.button(label="Server", style=discord.ButtonStyle.danger)
    async def channs_callback(self, interaction: discord.Interaction, button):
        await interaction.response.edit_message(content="HELLO Server")
    
class Entry(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print("Admin panel cog loaded!")

    @discord.app_commands.command(name="admin_panel", description="Сексапільні тьоті тут ✅✅✅")
    async def admin_panel(self, interaction: discord.Interaction, password: str):
        pwd: bool = True if password == "сушик1" else False
        if not pwd:
            await interaction.response.send_message("WRONG PASSWORD")
        else:
            await interaction.response.send_message(content=f"# Hello {interaction.user.mention}! | Password: {pwd} (||{password}||) ",view=MainPanel(),ephemeral=True)

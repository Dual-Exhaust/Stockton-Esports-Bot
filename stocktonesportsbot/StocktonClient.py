import datetime

import discord
from discord.ext import commands

from stocktonesportsbot.classes.BackgroundTasks import BackgroundTasks
from stocktonesportsbot.classes.Info import Info
from stocktonesportsbot.classes.Logger import Logger
from stocktonesportsbot.classes.Queue import Queue
from stocktonesportsbot.classes.Roles import Roles
from stocktonesportsbot.classes.Stats import Dictionary, Fortnite, RocketLeague, LoLInfo


# create your own class that is basically a discord client but with your customizations
# commands.Bot is the super class
# This not only uses the functionality of commands.Bot but it acts as the middle ground between
# the main and the other classes
class StocktonClient(commands.Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # lets you use multiple prefixes
        self.command_prefix = self.get_prefix
        self.case_insensitive = True
        self.queue = None
        self.send_link = False
        self.roles = Roles()
        self.bg_task_change_status = self.loop.create_task(BackgroundTasks.change_status(self))

    # ==================================Using Multiple Prefixes=================================
    # The command prefixes
    @staticmethod
    async def get_prefix(message):
        prefixes = ['/', '=', '.']
        return prefixes

    # =========================Shows that the bot has connected=================================

    async def on_ready(self):
        print("Connected To Server.")
        print("Bot's Discord Username: " + str(self.user))
        Logger.log_event("Bot Joined", "An instance of the StocktonBot has joined the Stockton Esports server.",
                         str(datetime.datetime.now()))
    
    # ========================================Generic Command Error======================================
    @staticmethod
    async def on_command_error(ctx, error):
        await ctx.message.delete()
        await ctx.author.send('```Error: ' + str(error) + '```')
    # ==================================Welcome Message===================================================
    @staticmethod
    async def on_member_join(member):
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.add_field(name="__**Welcome!**__",
                        value="Welcome to the Stockton University Esports Server!\nThe only channel you can view right "
                              "now is #landing. There, you can read the _Acceptable Use Standards of the University & "
                              "the Rules_ of the Server.\nOnce you have read everything, please __type__ the command "
                              "_'/accept'_ in the #landing channel. By doing so you will be given access to the rest of"
                              " the channels in the server.\nEnjoy your stay and we look forward to seeing you "
                              "represent Stockton Esports in the future.")
        embed.add_field(name="__**Stockton Esports server directory:**__",
                        value="_#announcments_ - Where all important news and information is posted.\n_"
                              "#game-selection_ - Choose the games you have the most interest in and would like"
                              " to compete in\n_#content-creation-guide_ - Interested in Streaming your games?"
                              " This guide will help you get started.\n_#questions_ - Ask any questions you have here\n"
                              "_#game-suggestions_ - Suggest games you would like to see us compete in here\n_"
                              "#game-highlights_ -Post any game highlights you want us to see")
        embed.add_field(name="**Categories:**",
                        value="_Game Channels_ - All game channels for players to talk about their game\n"
                              "_ECAC_ - All things ECAC")
        embed.add_field(name="__**Invite Your Friends!**__",
                        value="If you have friends who are Stockton Students and who are into competitive gaming "
                              "and want to play for Stockton University please invite them to the discord "
                              "with the link provided: https://discordapp.com/invite/4QgYAXQ")
        await member.send(embed=embed)
        Logger.log_event("Member Join", str(member) + " has joined the server.", str(datetime.datetime.now()))

    # ======================================Queues============================================
    # Only one queue can be active at a time, its object is stored in self.queue

    async def start_queue(self, team_size, number_of_teams, channel):
        if self.queue is None:
            self.queue = Queue(team_size, number_of_teams)
            self.queue.set_queue_message_id(await channel.send(embed=self.queue.get_queue_message_embed()))

    async def end_queue(self):
        if self.queue is not None:
            await self.queue.get_queue_message().delete()
            self.queue = None

    async def add_player(self, player):
        if player not in self.queue.player_queue:
            self.queue.add_player(player)
            await self.queue.get_queue_message().edit(embed=self.queue.get_queue_message_embed())
            return True
        else:
            return False

    async def remove_player(self, player):
        if player in self.queue.player_queue:
            self.queue.remove_player(player)
            await self.queue.get_queue_message().edit(embed=self.queue.get_queue_message_embed())
            return True
        else:
            return False

    async def get_teams(self):
        return self.queue.get_teams_embed()

    # =========================Statistics=============================
    def set_send_link(self, boolean):
        arg = str(boolean).lower()
        if arg == "true":
            self.send_link = True
            return True
        elif arg == "false":
            self.send_link = False
            return True
        return False

    # Fortnite
    def get_fortnite_stats(self, user):
        output = "```"
        for element in Fortnite.get_user_data(user=user):
            output += (element.text + "\n")
        output += "```"
        if self.send_link is True:
            return output + "For more stats please visit this link: " + Fortnite.get_user_data_link(user=user)
        else:
            return output

    # Rocket League
    def get_rocket_league_stats(self, user):
        output = "```"
        for element in RocketLeague.get_user_data(user):
            output += " ".join(element.text.split()) + "\n"
        output += "```"
        if self.send_link is True:
            return output + "For more stats please visit this link: " + RocketLeague.get_user_data_link(user=user)
        else:
            return output

    # LoL Champ Builds
    def get_champ_build(self, champ):
        champ = LoLInfo(champ)
        if self.send_link is True:
            return champ.get_info() + "For more stats please visit this link: " + champ.get_data_link()
        else:
            return champ.get_info()

    # Set User ID's
    @staticmethod
    def set_user_profile_id(user, arg, dictionary):
        Dictionary.add_item(user, arg, dictionary)
        Logger.log_event("Add/Change User ID", str(user) + " added/changed their ID in " + str(dictionary) + " to: "
                         + str(arg), str(datetime.datetime.now()))

    # ===========================ROLES===================================================

    async def add_role(self, role, user):
        Logger.log_event("Add Role", str(user) + " attempted to add the role: " + str(role),
                         str(datetime.datetime.now()))
        return await self.roles.add_role(role=role, user=user)

    async def remove_role(self, role, user):
        Logger.log_event("Remove Role", str(user) + " attempted to remove the role: " + str(role),
                         str(datetime.datetime.now()))
        return await self.roles.remove_role(role=role, user=user)

    @staticmethod
    def log_accept(user):
        Logger.log_event("Accept Terms", str(user) + " accepted the terms of the server.", str(datetime.datetime.now()))

    # =================================Help===================================================
    @staticmethod
    def get_help(arg):
        if str(arg).lower() == "addrole":
            return Info.get_addrole_help()
        elif str(arg).lower() == "removerole":
            return Info.get_removerole_help()
        elif str(arg).lower() == "setsteamid" or str(arg).lower() == "setfnid":
            return Info.get_set_id_help()
        elif str(arg).lower() == "rlstats":
            return Info.get_rlstats_help()
        elif str(arg).lower() == "fnstats":
            return Info.get_fnstats_help()
        elif str(arg).lower() == "champ":
            return Info.get_champ_help()
        elif str(arg).lower() == "queue" or str(arg).lower() == "createq" or str(arg).lower() == "endq" \
                or str(arg).lower() == "joinq" or str(arg).lower() == "leaveq" or str(arg).lower() == "getq":
            return Info.get_queue_help()
        elif str(arg).lower() == 'default':
            return Info.get_help()

    # =============================React for roles============================================================
    # if bot is in multiple servers and user is in the same servers this breaks
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == 498913415415463946 or payload.channel_id == 507986344929263639:
            member = discord.utils.get(self.get_all_members(), name=self.get_user(payload.user_id).name)
        else:
            return
        if payload.emoji.name == 'agree':
            role = discord.utils.get(member.guild.roles, name="Auth-ed")
            await member.add_roles(role)
        if payload.emoji.name == 'Fortnite':
            role = discord.utils.get(member.guild.roles, name="Fortnite")
            await member.add_roles(role)
        if payload.emoji.name == 'GC':
            role = discord.utils.get(member.guild.roles, name="Rocket League")
            await member.add_roles(role)
        if payload.emoji.name == 'CSGO':
            role = discord.utils.get(member.guild.roles, name="CS:GO")
            await member.add_roles(role)
        if payload.emoji.name == 'HS':
            role = discord.utils.get(member.guild.roles, name="Hearthstone")
            await member.add_roles(role)
        if payload.emoji.name == 'LoL':
            role = discord.utils.get(member.guild.roles, name="League")
            await member.add_roles(role)
        if payload.emoji.name == 'SmashBall':
            role = discord.utils.get(member.guild.roles, name="SBU")
            await member.add_roles(role)
        if payload.emoji.name == 'Overwatch':
            role = discord.utils.get(member.guild.roles, name="Overwatch")
            await member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.channel_id == 507986344929263639:
            member = discord.utils.get(self.get_all_members(), name=self.get_user(payload.user_id).name)
        else:
            return
        if payload.emoji.name == 'Fortnite':
            role = discord.utils.get(member.guild.roles, name="Fortnite")
            await member.remove_roles(role)
        if payload.emoji.name == 'GC':
            role = discord.utils.get(member.guild.roles, name="Rocket League")
            await member.remove_roles(role)
        if payload.emoji.name == 'CSGO':
            role = discord.utils.get(member.guild.roles, name="CS:GO")
            await member.remove_roles(role)
        if payload.emoji.name == 'HS':
            role = discord.utils.get(member.guild.roles, name="Hearthstone")
            await member.remove_roles(role)
        if payload.emoji.name == 'LoL':
            role = discord.utils.get(member.guild.roles, name="League")
            await member.remove_roles(role)
        if payload.emoji.name == 'SmashBall':
            role = discord.utils.get(member.guild.roles, name="SBU")
            await member.remove_roles(role)
        if payload.emoji.name == 'Overwatch':
            role = discord.utils.get(member.guild.roles, name="Overwatch")
            await member.remove_roles(role)

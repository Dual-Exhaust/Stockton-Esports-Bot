# =======================IMPORTS=================================
import pickle
import bs4
import discord
import requests
import os
from discord.ext import commands

from stocktonesportsbot.classes.Info import Info
from stocktonesportsbot.StocktonClient import StocktonClient

import pandas as pd
from stocktonesportsbot.classes import Metrics, Twitter, Leaderboard

# This is the object that we use to manipulate the Twitter API
tw = Twitter.TweetData()

# ===============================================================


# ========================Initial Set Up=========================
# This is the bot object itself that we set commands for using decorators
client = StocktonClient(commands.Bot)

# We want to override help we have to first remove it
# as it is one of the default commands in the commands.Bot super class
client.remove_command('help')

print("Discord Py Version: " + discord.__version__)
print("Pickle Version: " + pickle.format_version)
print("BeautifulSoup Version: " + bs4.__version__)
print("Requests Version: " + requests.__version__)


# ===========================ROLES===========================================
@client.command(pass_context=True)
async def accept(ctx):
    await ctx.message.delete()
    channel = ctx.message.channel
    user = ctx.message.author
    client.log_accept(user)
    if channel.name == "landing":
        role = discord.utils.get(user.guild.roles, name="Auth-ed")
        await user.add_roles(role)


@client.command(pass_context=True)
async def addrole(ctx, role):
    await ctx.message.delete()
    user = ctx.message.author
    if await client.add_role(role=role, user=user):
        await ctx.message.author.send("```" + str(user) + ", You gave yourself the " + role + " role.```")
    else:
        await ctx.message.author.send("```" + str(user) + ", something went wrong. Please make sure the role "
                                                          "exists, is spelled correctly, you do not have the "
                                                          "role, and you have the permission to add it. If you"
                                                          " still cannot add the role, contact @Dual#3727 or"
                                                          " another Admin for assistance.```")


@client.command(pass_context=True)
async def removerole(ctx, role):
    await ctx.message.delete()
    user = ctx.message.author
    if await client.remove_role(role=role, user=user):
        await ctx.message.author.send("```" + str(user) + ", You removed the " + role + " role from yourself.```")
    else:
        await ctx.message.author.send("```" + str(user) + ", something went wrong. Please make sure the role exists,"
                                                          " is spelled correctly, you have the role, and you have "
                                                          "the permission to remove it. If you still cannot remove"
                                                          " the role, contact @Dual#3727 or another Admin for "
                                                          "assistance.```")


@addrole.error
async def addrole_error(ctx, error):
    #await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.author.send(embed=Info.get_addrole_help())


@removerole.error
async def removerole_error(ctx, error):
    #await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.author.send(embed=Info.get_removerole_help())


# =======================STATS==================================================
@client.command(pass_context=True)
@commands.has_role("Admin")
async def set_send_link(ctx, arg):
    await ctx.message.delete()
    if client.set_send_link(arg):
        await ctx.message.author.send("Set the get_stats_link variable to: " + arg)
    else:
        await ctx.message.author.send(embed=Info.get_set_stats_link_help())


@client.command(pass_context=True)
async def setfnid(ctx, arg):
    await ctx.message.delete()
    client.set_user_profile_id(str(ctx.message.author), arg, r'fn.dictionary')
    await ctx.message.author.send("```Fortnite ID set to: " + str(arg) + "```")


@setfnid.error
async def setfnid_error(ctx, error):
    #await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.author.send(embed=Info.get_set_id_help())


@client.command(pass_context=True)
async def setsteamid(ctx, arg):
    await ctx.message.delete()
    client.set_user_profile_id(str(ctx.message.author), arg, r'steam.dictionary')
    await ctx.message.author.send("```Steam ID set to: " + str(arg) + "```")


@setsteamid.error
async def setsteamid_error(ctx, error):
    #await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.author.send(embed=Info.get_set_id_help())


@client.command(pass_context=True)
async def fnstats(ctx):
    await ctx.message.delete()
    player = ctx.message.author
    data = client.get_fortnite_stats(user=(player.name + "#" + player.discriminator))
    await player.send(data)


@client.command(pass_context=True)
async def rlstats(ctx):
    await ctx.message.delete()
    player = ctx.message.author
    data = client.get_rocket_league_stats(user=(player.name + "#" + player.discriminator))
    await player.send(data)


@client.command(pass_context=True)
async def champ(ctx, champion):
    await ctx.message.delete()
    await ctx.message.author.send(client.get_champ_build(champion))


@champ.error
async def champ_error(ctx, error):
    #await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.author.send(embed=Info.get_champ_help())


# ======================QUEUES===================================================
@client.command(pass_context=True)
async def createq(ctx, arg, arg1):
    await ctx.message.delete()
    channel = ctx.message.channel
    if channel.name == "queues":
        if str(arg).isdigit() and str(arg1).isdigit():
            await client.start_queue(arg, arg1, channel)
        else:
            await ctx.message.author.send("You must use integer values when creating a new queue. For more info use "
                                          "'/help queue'")
    else:
        await ctx.message.author.send("You must use the channel specified for queues when creating a new queue. "
                                      "For more info use '/help queue'")


@createq.error
async def createq_error(ctx, error):
    # await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.author.send(embed=Info.get_queue_help())


@client.command(pass_context=True)
async def endq(ctx):
    await ctx.message.delete()
    channel = ctx.message.channel
    if channel.name == "queues":
        await client.end_queue()
    else:
        await ctx.message.author.send("You must use the channel specified for queues when ending a queue. "
                                      "For more info use '/help queue'")


@client.command(pass_context=True)
async def joinq(ctx):
    await ctx.message.delete()
    player = ctx.message.author
    channel = ctx.message.channel
    if channel.name == "queues":
        if not await client.add_player(player.mention):
            await player.send("```You can't join a queue if you are already in it!```")
    else:
        await ctx.message.author.send("You must use the channel specified for queues when joining a queue. "
                                      "For more info use '/help queue'")


@client.command(pass_context=True)
async def leaveq(ctx):
    await ctx.message.delete()
    player = ctx.message.author
    channel = ctx.message.channel
    if channel.name == "queues":
        if not await client.remove_player(player.mention):
            await player.send("```You can't leave a queue if you are not in it!```")
    else:
        await ctx.message.author.send("You must use the channel specified for queues when leaving a queue. "
                                      "For more info use '/help queue'")


@client.command(pass_context=True)
async def getq(ctx):
    await ctx.message.delete()
    channel = ctx.message.channel
    if channel.name == "queues":
        await channel.send(embed=await client.get_teams())
    else:
        await ctx.message.author.send("You must use the channel specified for queues when getting the teams from a "
                                      "queue. For more info use '/help queue'")


# ======================================HELP==============================================
@client.command(pass_context=True)
async def help(ctx, arg='default'):
    await ctx.message.delete()
    await ctx.message.author.send(embed=client.get_help(arg))


# =======================TEST ONLY====================================
# Works for now

@client.command(pass_context=True)
async def server_stats(ctx):
    await ctx.message.delete()
    players = ctx.message.guild.members
    player = ctx.message.author

    # Sets the date range in which to gather all the data
    date_range = pd.date_range(start='2018-10-10', end='2019-09-20', freq='1D')

    # Gets when the players joined the discord server
    Metrics.create_date_heatmap(Metrics.server_joined_data(date_range, players), date_range, 'Blues', 10)
    await player.send(file=discord.File('heatmap.png'))

    # Gets when we have tweeted as the program
    Metrics.create_date_heatmap(Metrics.tweeted_date_data(date_range, tw), date_range, 'Greens', 5)
    await player.send(file=discord.File('heatmap.png'))

    # Returns a pdf of more specific numbers for when people join the server
    Metrics.server_roles(ctx.message.guild.members)
    await player.send(file=discord.File('stats.pdf'))


@client.command(pass_context=True)
async def server_activity(ctx):
    await ctx.message.delete()
    channels = ctx.message.guild.channels

    series = await Metrics.get_user_msg_count(channels)
    series = series.sort_values(ascending=False)
    print(series.to_string())
    print(len(series))


# =====================================Leaderboards===========================================

@client.command(pass_context=True)
async def adt_lol(ctx, arg):
    await ctx.message.delete()
    Leaderboard.LoLBoard.add_team(arg)


@client.command(pass_context=True)
async def rmt_lol(ctx, arg):
    await ctx.message.delete()
    Leaderboard.LoLBoard.remove_team(arg)


@client.command(pass_context=True)
async def gp_lol(ctx, arg, points):
    await ctx.message.delete()
    Leaderboard.LoLBoard.give_points(arg, points)


@client.command(pass_context=True)
async def rmp_lol(ctx, arg, points):
    await ctx.message.delete()
    Leaderboard.LoLBoard.remove_points(arg, points)


@client.command(pass_context=True)
async def lb_lol(ctx):
    await ctx.message.delete()
    await ctx.message.author.send(embed=Leaderboard.LoLBoard.get_leaderboard())

# =====================================Kill Bot from Server===================================

@client.command(pass_context=True)
@commands.has_role("Moderator") 
async def kill(ctx):
    await ctx.message.delete()
    await client.logout()

# =====================================RUNS THE BOT===========================================

token = os.environ["DISCORD_TOKEN"]
client.run(token)

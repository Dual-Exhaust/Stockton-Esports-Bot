import discord

# This class contains static methods that return discord.Embed objects
# The discord.Embed objects contain the help menu texts and other sorts of info
class Info:
    def __init__(self):
        pass

    @staticmethod
    def get_addrole_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Add Role Help")
        embed.add_field(name="Description", value="Use this to add a role to yourself."
                                                  "\nOnly roles that you are allowed to change are acceptable to use.")
        embed.add_field(name="Usage", value="/addrole <role>")
        return embed

    @staticmethod
    def get_removerole_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Remove Role Help")
        embed.add_field(name="Description", value="Use this to remove a role from yourself.\nOnly roles that you are "
                                                  "allowed to change are acceptable to use.")
        embed.add_field(name="Usage", value="/removerole <role>")
        return embed

    @staticmethod
    def get_set_id_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Set ID Help")
        embed.add_field(name="Description", value="Use this to set an ID for your statistics.")
        embed.add_field(name="Usage for Epic(Fortnite)", value="/setfnid <ID>")
        embed.add_field(name="Usage for Steam(Rocket League)", value="/setsteamid <ID>")
        return embed

    @staticmethod
    def get_queue_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Queue Help")
        embed.add_field(name="Description", value="Queues is a tool that allows you to randomize any number of teams "
                                                  "with any number of people.")
        embed.add_field(name="createq Usage", value="/createq <team size> <number of teams> \nStarts a new queue, "
                                                    "only one can be active at a time.")
        embed.add_field(name="endq Usage", value="/endq \nEnds and deletes the queue.")
        embed.add_field(name="joinq Usage", value="/joinq \nLets you join the queue.")
        embed.add_field(name="leaveq Usage", value="/leaveq \nLets you leave the queue.")
        embed.add_field(name="getq Usage", value="/getq \nSends you another message of your randomized teams.")
        return embed

    @staticmethod
    def get_champ_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Champion Build Help")
        embed.add_field(name="Description", value="This lets you pull champ info from champion.gg for finished champ"
                                                  " builds, max skill order and even starters.")
        embed.add_field(name="champ Usage", value="/champ <Champion Name>")
        return embed

    @staticmethod
    def get_rlstats_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Rocket League Stats Help")
        embed.add_field(name="Description", value="This lets you view your Rocket League Stats.")
        embed.add_field(name="rlstats Usage", value="/rlstats")
        return embed

    @staticmethod
    def get_fnstats_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Fortnite Stats Help")
        embed.add_field(name="Description", value="This lets you view your Fortnite Stats.")
        embed.add_field(name="fnstats Usage", value="/fnstats")
        return embed

    @staticmethod
    def get_set_stats_link_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Set Stats Link Help")
        embed.add_field(name="Description", value="This value dictates whether or not an additional link is sent with "
                                                  "a stat getter.\nThe link simply points to the page where the stats "
                                                  "were taken from.")
        embed.add_field(name="set_send_link Usage", value="/set_send_link <True/False>")
        return embed

    @staticmethod
    def get_help():
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Help Menu")
        embed.add_field(name="Description", value="This is the general help menu for the server commands.")
        embed.add_field(name="Additional Help", value="For additional information on each command's function and usage"
                                                      " use: \n/help <command>")
        embed.add_field(name="Stats", value="\t-setsteamid\n\t-setfnid\n\t-rlstats\n\t-fnstats\n\t-champ")
        embed.add_field(name="Queues", value="\t-createq\n\t-endq\n\t-joinq\n\t-leaveq\n\t-getq")
        embed.add_field(name="Roles", value="\t-addrole\n\t-removerole")

        embed.add_field(name="Reminder",
                        value="The Stockton Esports server and its respective bot are a work in progress. If you run "
                              "into any issues, or have any comments or concerns feel free to '@Admin' or "
                              "'@Moderator' for assistance.")
        return embed

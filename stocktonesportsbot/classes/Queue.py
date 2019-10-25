import discord
import random


class Queue:
    def __init__(self, team_size, number_of_teams):
        self.team_size = int(team_size)
        self.number_of_teams = int(number_of_teams)
        self.player_limit = int(team_size) * int(number_of_teams)
        self.player_queue = []
        self.queue_message_id = ''
        self.total_players = 0
        self.queue_full = False
        self.start_queue()

    def get_queue_message(self):
        return self.queue_message_id

    # Creates the embed to send as a message for the queue
    def get_queue_message_embed(self):
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Team Picker")
        embed.add_field(name="Queue Info", value=self.get_queue_info())
        embed.add_field(name="Players", value=self.player_queue)
        return embed

    # Sets the message id for later use (changing queue statuses/ending queue
    def set_queue_message_id(self, message_id):
        self.queue_message_id = message_id

    def start_queue(self):
        return self.get_queue_message_embed()

    def end_queue(self):
        pass

    def add_player(self, player):
        if not self.queue_full:
            self.player_queue.append(player)
            self.total_players += 1
        if self.player_limit == self.total_players:
            self.queue_full = True

    def remove_player(self, player):
        if self.total_players > 0:
            self.player_queue.remove(player)
            self.total_players -= 1

    # Sets the teams and returns them in an embed
    def get_teams_embed(self):
        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        embed.set_author(name="Team Picker")
        for x in range(self.number_of_teams):
            temp = []
            for y in range(self.team_size):
                player = random.choice(self.player_queue)
                temp.append(player)
                self.player_queue.remove(player)
            embed.add_field(name="Team " + str(x + 1), value=temp)
        return embed

    def get_queue_info(self):
        return "**Player Max:** " + str(self.player_limit) + " **Number of Teams:** " + str(self.number_of_teams) + \
               " **Team Size:** " + str(self.team_size) + " **Players in Queue:** " + str(self.total_players) + \
               " **Queue Full:** " + str(self.queue_full)

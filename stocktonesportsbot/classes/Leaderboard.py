import discord
from stocktonesportsbot.classes.Stats import Dictionary
import pickle

# use a dictionary + pickle to store the data


class LoLBoard:

    @staticmethod
    def add_team(team_name):
        Dictionary.add_item(team_name, 0, r'LoL_Leaderboard')

    @staticmethod
    def remove_team(team_name):
        Dictionary.remove_item(team_name, r'LoL_Leaderboard')

    @staticmethod
    def give_points(index, amount):
        with open(r'LoL_Leaderboard', 'rb') as config_dictionary_file:
            db = pickle.load(config_dictionary_file)

        # Gets the original value (String) and adds the new value to it
        temp = int(db[index]) + int(amount)

        # changes or concatonates the value we want to add to the dictionary
        db[index] = str(temp)

        # opens the file again and writes the updated dictionary object to it
        with open(r'LoL_Leaderboard', 'wb') as config_dictionary_file:
            db = pickle.dump(db, config_dictionary_file)
        return db

    @staticmethod
    def remove_points(index, amount):
        with open(r'LoL_Leaderboard', 'rb') as config_dictionary_file:
            db = pickle.load(config_dictionary_file)

        # Gets the original value (String) and substracts the value from it
        temp = int(db[index]) - int(amount)

        # changes or concatonates the value we want to add to the dictionary
        db[index] = str(temp)

        # opens the file again and writes the updated dictionary object to it
        with open(r'LoL_Leaderboard', 'wb') as config_dictionary_file:
            db = pickle.dump(db, config_dictionary_file)
        return db

    @staticmethod
    def get_leaderboard():
        with open(r'LoL_Leaderboard', 'rb') as config_dictionary_file:
            db = pickle.load(config_dictionary_file)

        embed = discord.Embed(colour=discord.Colour.from_rgb(121, 219, 233))
        # embed.set_author(name="League Leaderboard")
        # Creates a list of the keys in the dict, we need to reference this because dicts can't sort really so we
        # sort the values and then need to find the keys associated with them. As we add each team to the discord embed
        # object we remove it from the list so that even if multiple teams have the same score they don't get added
        # multiple times, the "if score == each" line was doing just that without the "and team in keys"
        keys = []
        # We have to make a list and put each key directly into it because for whatever reason dict.keys()
        # returns a view not a real list we can manipulate
        for each in db.keys():
            keys.append(each)
        # sorted sorts the values, reverse makes it so they sort in descending order
        for each in sorted(db.values(), reverse=True):
            # .items() returns a tuple of the key and value; team and score respectively
            # This actually gets the sorted value and finds the key associated with it, then adds it to the embed
            for team, score in db.items():
                if score == each and team in keys:
                    keys.remove(team)
                    embed.add_field(name=team, value=score)
        # for team in db:
            # embed.add_field(name=team, value=db[team])
        return embed

import pickle
import re
import requests
from bs4 import BeautifulSoup


class Stats:
    def __init__(self):
        pass

    @staticmethod
    def get_user_data(user):
        pass

    @staticmethod
    def get_user_data_link(user):
        pass


class Fortnite(Stats):

    @staticmethod
    def get_user_data(user):
        # Opens the pickled python dictionary and loads it as an object
        with open(r'fn.dictionary', 'rb') as config_dictionary_file:
            db = pickle.load(config_dictionary_file)
        # Creates the url to parse the stats from
        url = "https://www.fortbuff.com/players/" + str(db[user]) + "?mode=all&platform=all"
        result = requests.get(url)
        soup = BeautifulSoup(result.content, "html.parser")
        # Actually gets the data from the site
        data = soup.select(
            "div.PlayerPresenter > div.MainContent > main.PlayerSummary > aside > section > "
            "article > table > tbody > tr > td")
        return data

    @staticmethod
    def get_user_data_link(user):
        with open(r'fn.dictionary', 'rb') as config_dictionary_file:
            db = pickle.load(config_dictionary_file)
        return "https://www.fortbuff.com/players/" + str(db[user]) + "?mode=all&platform=all"


class RocketLeague(Stats):

    @staticmethod
    def get_user_data(user):
        with open(r'steam.dictionary', 'rb') as config_dictionary_file:
            steam_db = pickle.load(config_dictionary_file)
        url = "https://rocketleague.tracker.network/profile/steam/" + str(steam_db[user])
        result = requests.get(url)
        soup = BeautifulSoup(result.content, "html.parser")
        data = soup.select(
            "div.trn-profile > div.profile-main > div.aside > div.card-table-container > div#season-11 > "
            "table.card-table > tbody > tr > td")
        return data

    @staticmethod
    def get_user_data_link(user):
        with open(r'steam.dictionary', 'rb') as config_dictionary_file:
            steam_db = pickle.load(config_dictionary_file)
        return "https://rocketleague.tracker.network/profile/steam/" + str(steam_db[user])


class Dictionary:
    # This class literally only changes the python dictionary and overwrites the file

    def __init__(self):
        pass

    @staticmethod
    # This works for now but it may be easier to check if the file exists using os.path.isfile rather than a try catch statement, not sure what is best
    def add_item(user, arg, dictionary):
        # try to open the dictionary file to add the item too
        try:
            with open(dictionary, 'r+b') as config_dictionary_file:
                db = pickle.load(config_dictionary_file)
        # if the file does not exist then we create a default dictionary, create the file (xb), and write the dict to it
        except FileNotFoundError:
            db = {'Default User': 'Default ID'}
            with open(dictionary, 'xb') as config_dictionary_file:
                db = pickle.dump(db, config_dictionary_file)
        # by this point there is definitely a file and we can manipulate it to add the item
        finally:
            with open(dictionary, 'r+b') as config_dictionary_file:
                db = pickle.load(config_dictionary_file)
            # changes or concatonates the value we want to add to the dictionary
            db[user] = str(arg)
            with open(dictionary, 'wb') as config_dictionary_file:
            # writes the updated dictionary object to the file
                db = pickle.dump(db, config_dictionary_file)
        return db

class LoLInfo:
    def __init__(self, arg):
        champ = str(arg).upper()
        self.url = "https://champion.gg/champion/" + champ
        result = requests.get(self.url)
        self.soup = BeautifulSoup(result.content, "html.parser")
        # Starts the output to have the champ name at the top, the ``` starts the markdown box in discord
        self.output = "```_" + champ + "_\n"
        self.set_champ_build()
        self.set_champ_runes()
        self.set_champ_skills()
        # finishes the markdown box in discord
        self.output += "```"

    def get_data_link(self):
        return self.url

    # ==========================ITEMS===========================
    # Check the html of the site if this breaks in the future, what we are using now are the
    # 'div.build-wrapper > a' elements
    def set_champ_build(self):
        count = 0
        data = self.soup.findAll('div', attrs={'class': 'build-wrapper'})
        # cycles through each div we find(there are four, each on has info we want)
        # the if count == statements represent what each div that we pull holds and adds the appropriate
        # title line to the output
        for div in data:
            if count == 0:
                self.output += "Most Frequent Completed Build:\n"
            if count == 1:
                self.output += "Highest Win Percent Completed Build:\n"
            if count == 2:
                self.output += "Most Frequent Starters:\n"
            if count == 3:
                self.output += "Highest Win Percent Starters:\n"
            # This finds each individual link in the div that we just snagged and manipulates it for the info we want
            links = div.findAll('a')
            # this strips the item off of the end of the url that the we pull from the site (site uses
            # img's with href links)
            for a in links:
                a = a['href']
                if a.startswith("http://leagueoflegends.wikia.com/wiki/"):
                    link = re.sub('http://leagueoflegends.wikia.com/wiki/', '', a)
                    self.output += ("\t\t" + link + "\n")
            count += 1
        self.output += "\n"

    # =========================RUNES=========================
    def set_champ_runes(self):

        data = self.soup.findAll('div', attrs={'class': 'Description__Block-bJdjrS hGZpqL'})

        count = 0
        for div in data:
            if count == 0:
                self.output += "Most Frequent Runes:\n"
            # if the item is a rune itself we want to tab it to make it more aesthetically pleasing
            if (count == 1) or (count == 2) or (count == 3) or (count == 4) or (count == 6) or (count == 7) or (
                    count == 9) or (count == 10) or (count == 11) or (count == 12) or (count == 14) or (count == 15):
                self.output += "\t"
            if count == 8:
                self.output += "Highest Win Percent Runes:\n"
            # removes the whitespace and stuff afraid to change bc it formats okay already
            text = re.sub("\n.*$", "", div.text)
            text = text.replace("\n", "")
            self.output += ("\t\t" + text + "\n")
            count += 1
        self.output += "\n"

    # ==========================MAX SKILL ORDER======================================
    def set_champ_skills(self):
        order = []
        data = self.soup.findAll('div', attrs={'class': 'skill-selections'})
        for x in data:
            temp = ""
            dat = x.findAll('div')
            for y in dat:
                if y.text.strip() != "":
                    text = y.text.replace("\n", "")
                    temp += text
                else:
                    temp += "-"
            order.append(temp)

        count = 0
        for s in order:
            if count == 0:
                self.output += "Most Frequent Max Skill Order:\n"
            if count == 5:
                self.output += "Highest Win Percent Max Skill Order:\n"
            # We also get an element that holds the numbers at the top of the chart so this takes care of
            # the unwanted numbers that get returned
            if not s.isdigit():
                self.output += s + "\n"
            count += 1

    def get_info(self):
        return self.output


# Stockton Esports Bot

## Install and Run
Create a directory that you want to run the bot in. It can create files for storage as commands are called.
You need to have a .env file inside this directory that contains the discord api key. This is the same file that should hold your twitter api key and twitter api secret as well.

Install the package using pip. This requires using python3.7.x.

> pip install stocktonesportsbot

Now use the launch command inside your new directory. The bot will start up.

> launch.sh

If you  were using AWS or another hosting service and you have already installed the package on the server instance:

> nohup launch.sh > nohup.out &

This will run the bot in the background, disconnected from the shell you are using. That means you can close the shell and the bot will continue to run. 

## Commands

### Help

[main.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/main.py#L227)
[StocktonClient.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/StocktonClient.py#L169)
[Info.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/master/Classes/Info.py)

#### help
Use the help command by itself to get general knowledge of the other commands in the server.
> Usage: /help

You can also enter the name of another command to get a more in depth description for the usage of that specific command.
> Usage: /help <command>

Output from the help command is sent directly to the user in a direct message.

### Role Moderation

[main.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/main.py#L34)
[StocktonClient.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/StocktonClient.py#L153)
[Roles.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/master/Classes/Roles.py)

#### accept
Accept is only for when a new user joins the server; it is so they verify that they have read the rules and then it gives them the "auth-ed" role in the server. This grants them access to the rest of the server.
> Usage: /accept

This can also be used to gain the auth-ed role at any time, should an accident happen and it gets removed from a user manually.

#### addrole
Specifically for adding roles to a user, by the user themselves. They should be able to add any role for specific games that exist in the server. They *should not* be able to add roles such as "Game-manager" or "Moderator". Role names entered as a parameter can now be case insensative.
> Usage: addrole <role name>

#### removerole
Removes a role from a user as specified. Similar to addrole, this command can only manipulate game specific roles, *not* roles such as "auth-ed" or "Moderator". Role names entered as a parameter can now be case insensative.
> Usage: /removerole <role name>

### Game Statistics

[main.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/main.py#L88)
[StocktonClient.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/StocktonClient.py#L105)
[Stats.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/master/Classes/Stats.py)

#### Notes 
All statistic commands can possibly become broken due to a change in the website that we parse the data from. The sites are 3rd party sites and may not always have the most up to date statistics.

The python dictionaries that hold the user ID's use their discord name and the discriminator as an index for the account ID that will be used for the stats.

Ex:
> Discord#1234 : <Steam or Epic ID>

In the future it would be good to allow the get stat functions to use an ID as a parameter as well, rather than solely relying on the fact that a user has to save the ID first before calling the stat command.

#### setfnid
Allows a user to set and save their Epic Games username in order to get their Fortnite stats later, without entering it again. The username is stored in a __python dictionary__ and saved to a file using __pickle__. This ID can be found if you search for your stats on [Fortbuff](https://www.fortbuff.com/) and look in the url. It should look something like this:
> https://www.fortbuff.com/players/<**EPIC ID**>?mode=all&platform=all

All this does is simply store that ID in a file for later use, it will not automatically send you your stats after you set your ID.
> Usage: /setfnid <Epic Games ID>

#### setsteamid
Allows a user to set and save their Steam username in order to get their Rocket League stats later, without entering it again. The username is stored in a __python dictionary__ and saved to a file using __pickle__. This ID can be found in two main places. You can search for your stats on [Tracker Network](https://rocketleague.tracker.network/) and look in the url, or go to your [Steam](https://steamcommunity.com/) profile page (browser or desktop client) and look there.

*For Tracker Network*
> https://rocketleague.tracker.network/profile/steam/<**STEAM ID**>

*For Steam*
> https://steamcommunity.com/id/<**STEAM ID**>

This ID can be either the name that you set when you created your Steam account *OR* a string of numbers. The Tracker Network will accept either when the url is built by the bot.

> Usage: /setsteamid <Steam ID>

#### fnstats
When called, this returns a list of the user's Fortnite stats. It uses the saved Epic Games ID set by **setfnid**. The method gets the ID from a pickled python dictionary and then uses that value to build the url on [Fortbuff](https://www.fortbuff.com/) that contains their respective stat page.

> Usage: /fnstats

#### rlstats

When called, this returns a list of the user's Rocket League stats. It uses the saved Steam ID set by **setsteamid**. The method gets the ID from a pickled python dictionary and then uses that value to build the url on [Rocket League Tracker Network](https://rocketleague.tracker.network/) that contains their respective stat page.

> Usage: /rlstats

#### champ

This is a command specifically for League of Legends. When passed a champions name, such as Riven or Thresh, it will return general stats for that champion from [champion.gg](https://champion.gg). This includes most frequent and highest win percent starters, runes, finished builds, and max skill order. The idea here is that Discord has a game overlay that can be pulled up in full screen games rather than alt-tabbing to a browser window.

> Usage: /champ <Champion Name>

### Queues

[main.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/main.py#L156)
[StocktonClient.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/StocktonClient.py#L73)
[Queue.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/master/Classes/Queue.py)

#### Notes

Queues can only be used in a channel named "queues". Only one queue can be active at a time, in the future maybe have a list of queue IDs to support multiple queues at once. This can be done by passing another parameter ID when calling the command and storing the queue by the created ID rather than the embed message ID. Then you could join a queue by /joinq <queue> instead.

#### createq

This physically creates the queue by taking in the size of each team, and how many teams to create. Both parameters must be passed, *and* be integer values. It returns by creating an embedded message in the "queues" channel. This message will be further updated as people join and leave the queue. It will be deleted if endq is used.

> Usage: /createq <team size> <number of teams>

#### endq

Simply ends the current queue by deleting the embedded message and setting StocktonClient.queue to null.

> Usage: /endq

#### joinq

This lets a user join the current queue. It adds them to the list of users, and then updates the embedded queue message to display them in the queue.

> Usage: /joinq

#### leaveq

Allows a user that previously joined the queue to leave it. It removes them from the list of users and updates the embedded queue message.

> Usage: /leaveq

#### getq

This randomizes teams from the players in the current queue and sends a list of each team in the "queues" channel.

> Usage: /getq


### Metrics

[main.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/4fd7f268cb257dc17165ff82362cfe36c8ee91ed/main.py#L241)
[Metrics.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/master/Classes/Metrics.py)

#### server_stats

This sends calendar heat maps to the user. The blue heat map represents when users join the discord server. The green heat map represents when the @StocktonEsports twitter account tweets. The heat maps are created using [this answer](https://stackoverflow.com/questions/32485907/matplotlib-and-numpy-create-a-calendar-heatmap/51977000#51977000) on stack overflow. The discord data is collected by parsing through the members in the server and viewing their **joined date**. The twitter data is collected using **tweepy** which is a python wrapper for the Twitter API. 

> Usage: /server_stats

#### server_activity

All this does is parse through each text channel in the server and keep a tally of how many times each user sends a message. It prints the list out to console and it's kind of trivial.

> Usage: /server_activity

### Admin Controls

#### set\_send_link

To see the code for this setting see the Game Statistics section

This sets a setting to send the stats link along with the stats when they get sent to a user. It is only for statistics related to games themselves. This is so that they could easily view the page the stats came from as well as get a more in depth view.

> Usage: /set\_send_link <boolean>
  
  #### kill
  [main.py](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/8c569c602fb79a567ab3e068ad96befa01b4bfe1/main.py#L309)
  
  This closes the bots connection with Discord. Essentially just turns it off.
  
  > Usage: /kill

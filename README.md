
# stocktonbot

## Installed libraries

Includes all of the libraries I have installed currently because I'm lazy and didn't feel like taking out the default ones

Use "pip freeze" when in terminal to get this list, or use "pip list" to get a formatted list of the packages and versions

aiohttp==3.5.4
async-timeout==3.0.1
attrs==19.1.0
beautifulsoup4==4.8.0
certifi==2019.6.16
chardet==3.0.4
cycler==0.10.0
discord.py==1.2.3
idna==2.8
kiwisolver==1.1.0
matplotlib==3.1.1
multidict==4.5.2
numpy==1.17.1
oauthlib==3.1.0
pandas==0.25.1
pyparsing==2.4.2
PySocks==1.7.0
python-dateutil==2.8.0
pytz==2019.2
requests==2.22.0
requests-oauthlib==1.2.0
six==1.12.0
soupsieve==1.9.3
tweepy==3.8.0
urllib3==1.25.3
websockets==6.0
yarl==1.3.0

## Commands

### Help

#### help
Use the help command by itself to get general knowledge of the other commands in the server.
> Usage: /help

You can also enter the name of another command to get a more in depth description for the usage of that specific command.
> Usage: /help <command>

Output from the help command is sent directly to the user in a direct message.

### Role Moderation

#### accept
Accept is only for when a new user joins the server; it is so they verify that they have read the rules and then it gives them the "auth-ed" role in the server. This grants them access to the rest of the server.
> Usage: /accept

This can also be used to gain the auth-ed role at any time, should an accident happen and it gets removed from a user manually.

#### addrole
Specifically for adding roles to a user, by the user themselves. They should be able to add any role for specific games that exist in the server. They *should not* be able to add roles such as "Game-manager" or "Moderator". At the moment role names entered as a parameter have to be case sensitive to the roles that exist in the server.
> Usage: addrole <role name>

#### removerole
Removes a role from a user as specified. Similar to addrole, this command can only manipulate game specific roles, *not* roles such as "auth-ed" or "Moderator". Role names passed as a parameter must also be case sensitive to the existing role in the server.
> Usage: /removerole <role name>

### Game Statistics

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

#### server_stats

This sends calendar heat maps to the user. The blue heat map represents when users join the discord server. The green heat map represents when the @StocktonEsports twitter account tweets. The heat maps are created using [this answer](https://stackoverflow.com/questions/32485907/matplotlib-and-numpy-create-a-calendar-heatmap/51977000#51977000) on stack overflow. The discord data is collected by parsing through the members in the server and viewing their **joined date**. The twitter data is collected using **tweepy** which is a python wrapper for the Twitter API. 

> Usage: /server_stats

#### server_activity

All this does is parse through each text channel in the server and keep a tally of how many times each user sends a message. It prints the list out to console and it's kind of trivial.

> Usage: /server_activity

### Settings

#### set\_send_link

This sets a setting to send the stats link along with the stats when they get sent to a user. It is only for statistics related to games themselves. This is so that they could easily view the page the stats came from as well as get a more in depth view.

> Usage: /set\_send_link <boolean>

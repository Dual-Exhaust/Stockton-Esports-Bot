# Initial Setup
_**General notes:**_
~~In order to use pickle with the dictionaries that hold user ID's (for the stats methods), you have to keep in mind that when you are using pickle you are not allowed to unpickle files that are empty, it throws an EOFError: ran out of input. This makes sense enough, you just need to somehow make the file not empty.
To create a new data file I just manually created a dictionary object and pickled it to the file first, then took out that code so we only had the file holding the pickled dictionary object. The up to date code un-pickles the dictionary object **first** so it can manipulate it, but since the error was getting thrown when the file was empty I _*needed*_ to add a "default" value in the pickled dictionary. What should be changed is that there should be a try/catch around the code and on fail check the type of error, if it is EOFError, then call a few lines that add an item to a dict and then save it to the file **before** you try to manipulate the dict. So essentially:~~

> ~~try (un-pickle dict) catch on EOFError (manually add default item to a dict and pickle it to the file), _**then**_ (un-pickle dict as norrmal and do what you need to do)~~

~~You only need one item in a single dict that is pickled to a file to be able to un-pickle it.~~
The code should now automatically create the files necessary and add a default listing in the dictionaries when set ID commands are called. I believe that if you call a stat getter before an id setter (before the dictionary file is created) it will break as I have not yet had a chance to rework the stat getters themselves.

The reason this snippet is in setup is because the files that hold the dictionaries of user IDs are not included in the repo for user privacy purposes. You need to make sure these files are present, and functional otherwise the bot commands using them will error.

If multiple instances of code are running and you call a command that exists in both instances of code where the code deletes the command message (as it should), then the instance of code that recieves the request first will delete the message and the other instances will throw a 404 not found error as they tried to delete a message that already had been deleted. The only reason I put this here is that sometimes I work from Windows and sometimes I work from Linux, and I don't always stop execution of the code which actually caused this issue to arise. Just something to remember while you program because there could be a lot of things that go wrong due to running multiple instances of code.

I absolutely recommend using Linux, but it is just my personal preference.

## Windows
I personally prefer to use PyCharm as my IDE for python related projects in Windows. You can download the free community version [here](https://www.jetbrains.com/pycharm/download/#section=windows).

You also may need [Git](https://git-scm.com/) installed depending on how you wish to set up your files, and I highly recommend it.

Once you have installed PyCharm you may have to do some initial setup but then a pop up will be displayed to create your own project. 

### Git
Click on "Check out from Version Control" and select "git" from the drop down menu. Another pop up will appear where you can specify a URL and a directory to store the local files. Note that you can also log directly into Github from this menu; for private repo URLs you need to verify you have access to them. 

Paste [this URL](https://github.com/Dual-Exhaust/Stockton-Esports-Bot) into the prompt and click on test. It will say "Connection Successful" or give you an error for why you couldn't connect. 

If it says git.exe not found in the error then you probably haven't yet installed git for windows and if you have, then try restarting PyCharm as it checks for Git's file path on startup.

Once you have gotten the "Connection Successful" message, go ahead and click "Clone" and PyCharm will handle creating the project for you.

### Zip File

From the [Github repo main page](https://github.com/Dual-Exhaust/Stockton-Esports-Bot) click the green button on the right side that says "Clone or Download". From there click the "Download Zip" option.

In your downloads folder you should now see a zip file that is named "StocktonBot.zip". To unzip the folder, right click it and select "extract all", or use an archive tool of your preference such as 7zip. This will unzip the folders.

If you double click on the new folder titled "StocktonBot" you will see that there is another folder inside of it also called "StocktonBot", this is the folder that we will want to move into our PyCharm project directory. 

The default directory that PyCharm uses is "C:\Users\\**USER**\PycharmProjects". We simply want to open two instances of File Explorer, and then drag the folder from Downloads into the PyCharm project directory. 

From there all you need to do launch PyCharm, and then open the project folder you just dropped into the project directory by clicking on the folder and hitting "open".

*Note*: Project folders will have a small black box on their image. Your directory should look something like this :

> C:\Users\\**USER**\PycharmProjects\StocktonBot\ProjectFiles

Sometimes the pop up to open a project does not automatically open the project directory so you will need to find it and then open your project from there.

### Project Dependencies

PyCharm _**will not**_ automatically set up the project's dependencies. 

It will notice the requirements.txt file and will try to display a warning for you to "Install Requirements" at the top of the window. You can just click the button up there. If you do not get the notification, you can go to the bottom of the screen and click on the "terminal" tab. Once you are using the terminal type the following command:

> pip install -r requirements.txt

Pip will then install the dependencies specified in the file.

I still have not yet found a way to get a .env file to work inside of PyCharm, I had hardcoded the token into the code (which is really bad practice) so I could make sure this tutorial worked and then took it out before I committed files.

## Linux
**NOTE:** For some reason the pandas install from the requirements does not work when running main.py after finishing this tutorial, not sure why, but remming out the pandas bits in main.py allows the program to compile/run successfully. This disables the commands in the TEST portion of the code as well as some imports. 

This is a WIP as I have not yet had a chance to fully set it up on Linux yet. I have also not really reviewed this part of the setup tutorial so its a bit informal. This assumes you have prior experience in Linux.

### Windows Subsystem for Linux 
If you are using Windows but want to use Linux, [this article](https://docs.microsoft.com/en-us/windows/wsl/install-win10) will show you how to run a Linux subsystem on Windows.

I personally use **Ubuntu 18.04 LTS** but you are welcome to use whichever distribution you like if you prefer another. The rest of this tutorial will assume you are using Ubuntu 18.04 LTS.

### Python3.7 Install
Next thing is you need to have **Python 3.7.3** installed, which [this tutorial](https://websiteforstudents.com/installing-the-latest-python-3-7-on-ubuntu-16-04-18-04/) for installing Python 3.7.x seemed to work fine. I did **not** use the PPA section because I do not want Python to update automatically. **BEFORE** you follow that tutorial please make sure to call these two bash commands:

> sudo apt-get install libbz2-dev
> sudo apt-get install liblzma-dev

Those libraries are necessary when using some imported packages with python, and they are not included when building python with the tutorial.

Then you just need to make sure that you have pip and virtualenv installed before you actually start cloning.

To install pip:

> sudo apt install python-pip

To install virtualenv for python:

> python3.7 -m pip install --user virtualenv

### Git Clone and Virtual Environment Setup
You can now clone the github repository and activate your virtual environment.

> git clone https://github.com/Dual-Exhaust/Stockton-Esports-Bot

This will make a directory called "Stockton-Esports-Bot" with all of the project files inside of it. 

Move into that directory and now we can create our virtual environment. 

> python3.7 -m venv env

This creates the virtual environment and all the files it needs to run. To activate the virtual environment:

> source env/bin/activate

You should see **(env)** before user@machine:/file/path

Anything that you install with pip now will be installed to the virtual environment and NOT your real environment, so we can now use:

> pip install -r requirements.txt

Your dependencies have been installed. When you are all done editing and testing your code, just remember to deactivate your virtual environment. Just type "deactivate" to do so.

### .env Setup
At the bottom of main.py you will notice a line that sets a variable named 'token'. This variable is our Discord API key. The variable is stored in a .env file that is not included in the repo. You will need to obtain your own key in order to connect to your own Discord bot, and then create a .env file that holds the key.

[This tutorial](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) goes over how to create a Discord bot and connect it to your testing server.

Create an .env file in the project directory and add the following line to it:
> DISCORD_TOKEN='INSERT YOUR TOKEN HERE'

Now we need to load the .env file so your code can access it. Enter this line into the console:
> set -a; source ./.env; set +a;

Type "echo $DISCORD_TOKEN" to make sure it worked. You should see your token printed to the console.

You should now be all set to start programming!

# Contributions
Any and all contributions are welcome as long as they follow the [code of conduct](https://github.com/Dual-Exhaust/Stockton-Esports-Bot/blob/master/CODE_OF_CONDUCT.md). Please submit a pull request to merge your contributions with the project.

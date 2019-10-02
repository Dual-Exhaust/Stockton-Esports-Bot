# Initial Setup

## Windows
I personally prefer to use PyCharm as my IDE for python related projects. You can download the free community version [here](https://www.jetbrains.com/pycharm/download/#section=windows).

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


## Linux

This is a WIP as I have not yet had a chance to fully set it up on Linux yet. I have also not really reviewed this part of the setup tutorial so its a bit informal. This sort of assumes you have prior experience in Linux.

To begin with, if you use Linux already good for you but I'm going to tell you how to set up Windows Subsystem for Linux (WSL for short).

I lied, I won't teach you but [this article](https://docs.microsoft.com/en-us/windows/wsl/install-win10) will.

I personally use Ubuntu 18.04 LTS but you are welcome to use whichever distribution you like if you prefer another. 

Next thing is you need to have **Python 3.7.3** installed, which [this tutorial](https://websiteforstudents.com/installing-the-latest-python-3-7-on-ubuntu-16-04-18-04/) for installing Python 3.7.x seemed to work. Keep in mind that is specifically for Ubuntu.

Then you just need to make sure that you have pip installed as well as virtualenv and you should be all set to actually start cloning.

Ubuntu uses apt, so to install pip:

> sudo apt install python-pip

Then to install virtualenv for python:

> python3.7 -m pip install --user virtualenv

From there you are all set to clone the git repo and activate your venv. I would make a test directory to clone the repo files to at first.

From inside that directory:

>git clone https://github.com/Dual-Exhaust/Stockton-Esports-Bot

This will make a directory called "Stockton-Esports-Bot" with all the files inside of it. 

Move into that directory and now we can create our venv. 

> python3 -m venv env

This creates the venv and all the files it needs to run. All we did was create it, and it is not active yet. To activate it:

>source env/bin/activate

You should see **(env)** before user@machine:/file/path

Anything that you install with pip now will be installed to the venv and NOT your real environment, so we can now use:

> pip install -r requirements.txt

Your dependencies have been installed. When you are all done editing your code just remember to deactivate your venv and use your regular environment again. Just type "deactivate" to do so.

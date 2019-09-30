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

This is a WIP as I have not yet had a chance to fully set it up on Linux yet.

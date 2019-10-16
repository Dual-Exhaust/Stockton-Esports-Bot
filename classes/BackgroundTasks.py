import discord
import asyncio
from itertools import cycle

status = ["bot stuff", "type /help", "annoying the devs", "storing data", "ruining everything"]


class BackgroundTasks:

    @staticmethod
    async def change_status(stockton_client):
        await stockton_client.wait_until_ready()
        mgs = cycle(status)
        # this is where your background process actually gets run
        while not stockton_client.is_closed():
            stat = next(mgs)
            await stockton_client.change_presence(activity=discord.Game(name=stat))
            await asyncio.sleep(30)  # task runs every 30 seconds

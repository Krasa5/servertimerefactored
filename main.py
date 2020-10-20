import discord
from discord.ext import commands, tasks
from datetime import datetime, time, timedelta
import datetime as dt
from itertools import cycle
import asyncio
import pickle
import os


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="s!", intents=intents)
channel_id = 693467686146932832
version = 0.21

all_cogs = []


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(f"Version = {str(version)}")
    for filename in os.listdir("./cogs/"):
        if filename.endswith(".py"):
            bot.load_extension(f"cogs.{filename[:-3]}")
            all_cogs.append(filename[:-3])
            print(f"Cog: {filename[:-3]} is loaded successfully.")
    with open("./cogs/cogs.txt", "w") as fp:
        fp.write(str(all_cogs))
    print("-------------------------------------------")


with open("./botkeyrefactored.txt", "r") as fp:
    clientkey = fp.read()
    bot.run(clientkey)

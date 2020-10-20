import discord
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import asyncio
import ast


class BackgroundTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.changeStatus.start()

    @tasks.loop(seconds=60)
    async def changeStatus(self):
        status = next(self.bot.statuses)
        await self.bot.change_presence(activity=discord.Game(status))

    @changeStatus.before_loop
    async def wait_for_bot(self):
        await self.bot.wait_until_ready()
        self.bot.statuses = cycle(["s!amongus", "Reworking the bot.", "s!help"])


def setup(bot):
    bot.add_cog(BackgroundTasks(bot))

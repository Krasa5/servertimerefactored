import discord
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle
import asyncio
import ast

with open("./cogs/cogs.txt", "r") as fp:
    all_cogs = ast.literal_eval(fp.read())


class AdminCommands(commands.Cog):
    global all_cogs

    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        privilege = get(ctx.guild.roles, name="bot_tester")
        return privilege in ctx.author.roles

    # @commands.Cog.listener()
    # async def on_ready(self):

    # Start of Cogs
    @commands.command()
    async def cogs(self, ctx):
        cogs = []
        for one_cog in all_cogs:
            cogs.append(one_cog)
        cogs = ", \n".join(cogs)
        await ctx.send(f"Running cogs: ```{cogs}```")

    @commands.command()
    async def load(self, ctx, cog):
        self.bot.load_extension(f"cogs.{cog}")

    @commands.command()
    async def unload(self, ctx, cog):
        self.bot.unload_extension(f"cogs.{cog}")

    @commands.command()
    async def reload(self, ctx, cog=None):
        if not cog:
            for one_cog in all_cogs:
                self.bot.reload_extension(f"cogs.{one_cog}")
                print(f"Reloaded cog: {one_cog}")
            await ctx.send("Reloaded all Cogs.")
        else:
            self.bot.reload_extension(f"cogs.{cog}")
            await ctx.send(f"Reloaded cog: {cog}")

    # End of Cogs

    @commands.command()
    async def ping(self, ctx):
        latency = self.bot.latency * 1000
        await ctx.send(f"My ping is {round(latency,1)} ms!")

    @commands.command()
    async def purge(self, ctx, amount: int):
        amount = amount + 1
        if amount >= 10:
            msg = await ctx.send("Are you sure?")
            await msg.add_reaction("\U0001F44D")

            def check(reaction, user):
                return (
                    user == ctx.author and str(reaction.emoji) == "\U0001F44D"
                )  # thumbsup emoji

            await self.bot.wait_for("reaction_add", check=check)
            await ctx.channel.purge(limit=amount)
        else:
            await ctx.channel.purge(limit=amount)


def setup(bot):
    bot.add_cog(AdminCommands(bot))

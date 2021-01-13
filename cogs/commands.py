import discord
from discord.ext import commands, tasks
import asyncio


class UserCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def guild_check():  # method has no argument
        def predicate(ctx):
            return ctx.author.guild.id == 362555652230479872

        return commands.check(predicate)

    @commands.command()
    @guild_check()
    async def suhu(self, ctx):
        msg = await ctx.send("Are you 18+?")
        await msg.add_reaction("\U0001F44D")

        def check(reaction, user):
            return (
                user == ctx.author and str(reaction.emoji) == "\U0001F44D"
            )  # thumbsup emoji

        await self.bot.wait_for("reaction_add", check=check)
        role = ctx.author.guild.get_role(422723686936870912)
        # add_roles accepts a role object not an ID
        await ctx.author.add_roles(role)
        await msg.delete()


def setup(bot):
    bot.add_cog(UserCommands(bot))
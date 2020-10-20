import asyncio
import datetime as dt
import os
from datetime import datetime, time, timedelta
from itertools import cycle

import discord
from mvc.amongus.controller import AmongUsGame
from discord.ext import commands, tasks
from mvc.hangman.controller import HangmanGame

hangman_games = {}


class Game(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hm(self, ctx, guess: str):
        player_id = ctx.author.id
        hangman_instance = HangmanGame()
        game_over, won = hangman_instance.run(player_id, guess)

        if game_over:
            game_over_message = "You LOST!"
            if won:
                game_over_message = "You WON!"

            game_over_message = f"{game_over_message} The word was '{hangman_instance.get_secret_word()}'."
            await hangman_instance.reset(player_id)
            await ctx.send(game_over_message)
        else:
            await ctx.send(f"Progress: {hangman_instance.get_progress_string()}")
            await ctx.send(f"Guess so far: {hangman_instance.get_guess_string()}")

    @commands.command()
    async def amongus(self, ctx, gameID="No code provided."):
        if ctx.author.voice and ctx.author.voice.channel:
            guild_id = ctx.guild.id
            amongus_instance = AmongUsGame(self.bot, ctx, gameID)
            message = await amongus_instance.run(guild_id)
            if message == True:
                await ctx.send("Your server is already running a game.")
        else:
            await ctx.send("Please join a voice channel to start playing.")
            return


def setup(bot):
    bot.add_cog(Game(bot))

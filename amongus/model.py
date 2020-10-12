import discord
from discord.ext import commands


class AmongUs:
    def __init__(self, bot, ctx, gameID):
        self.bot = bot
        self.ctx = ctx
        self.gameID = gameID

    async def start(self, ctx, members_list):
        await self.ctx.author.voice.channel.set_permissions(self.ctx.guild.default_role, use_voice_activation=True)

        amongstart = discord.Embed(
            title = 'Among Us Bot',
            description =  'Discord Bot helper for Among Us!',
            colour = discord.Colour.blue())
        amongstart.set_image(url='https://i.ibb.co/jwMHxQT/start.jpg')
        amongstart.add_field(name='Game ID: ', value=self.gameID, inline=False)
        amongstart.add_field(name='Players: ', value=', \n'.join(members_list), inline= False)
        amongstart.add_field(name='Instructions ', value='All players in the voice channel can react to emoji to start the game.', inline= False)
        amongstart.set_footer(text=(f'Game started by: {ctx.author}'))
        msg = await ctx.send(embed=amongstart)
        await msg.add_reaction('\U00002705')
        await msg.add_reaction('\U0000274C')

        def check(reaction, user):
            return (user in self.ctx.author.voice.channel.members and (str(reaction.emoji) == '\U00002705' or str(reaction.emoji) == '\U0000274C'))
                
        result = await self.bot.wait_for('reaction_add', check=check)
        await msg.delete()
        return result

    async def playing(self, ctx):
        await self.ctx.author.voice.channel.set_permissions(ctx.guild.default_role, use_voice_activation=False)
        playing_embed = discord.Embed(
            title = 'Shhhhhh! Game is underway.',
            description= 'Press the unmute button to start discussions.', 
            colour = discord.Colour.red()
        )
        playing_embed.add_field(name='Game ID: ', value=self.gameID, inline=False)
        playing_embed.set_image(url='https://i.ibb.co/sJvKyFv/unmute.jpg')
        playing_embed.set_footer(text=(f'All players in voice channel can react to emoji to go to discussions round.'))
        playing = await ctx.send(embed=playing_embed)

        await playing.add_reaction('\U0001F508')
        await playing.add_reaction('\U0001F503')
        await playing.add_reaction('\U0000274C')

        def check(reaction, user):
            return (user in self.ctx.author.voice.channel.members and (str(reaction.emoji) == '\U0001F508' or str(reaction.emoji) == '\U0001F503' or str(reaction.emoji) == '\U0000274C'))
        result = await self.bot.wait_for('reaction_add', check=check)
        await playing.delete()
        return result

    async def discussions(self, ctx):
        await self.ctx.author.voice.channel.set_permissions(ctx.guild.default_role, use_voice_activation=True)
        discussions_embed = discord.Embed(
            title = 'Voting round. Discuss!',
            description =  'Press the mute button when voting round ends.',
            colour = discord.Colour.green()
        )
        discussions_embed.add_field(name='Game ID: ', value=self.gameID, inline=False)
        discussions_embed.set_image(url='https://i.ibb.co/RHS0jg3/mute.jpg')
        discussions_embed.set_footer(text=(f'All players in voice channel can react to emoji to go to playing round.'))
        discussions = await ctx.send(embed=discussions_embed)
        await discussions.add_reaction('\U0001F507')
        await discussions.add_reaction('\U0001F503')
        await discussions.add_reaction('\U0000274C')

        def check(reaction,user):
            return (user in self.ctx.author.voice.channel.members and (str(reaction.emoji) == '\U0001F507' or str(reaction.emoji) == '\U0001F503' or str(reaction.emoji) == '\U0000274C'))

        result = await self.bot.wait_for('reaction_add', check=check)
        await discussions.delete()
        return result

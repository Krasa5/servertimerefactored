from .model import AmongUs

games = {}

class AmongUsGame:
    current_game = None

    def __init__(self, bot, ctx, gameID):
        self.bot = bot
        self.ctx = ctx
        self.gameID = gameID

    async def get_members(self):
        members_list = [member.name for member in self.ctx.author.voice.channel.members]
        return members_list
    
    async def run(self, guild_id):
        check = await self.check_game(guild_id)
        if check == False:
            return True
        while True:
            status = await self.play()
            while True:
                end = await self.check_status(status)
                if end == 1: #ends game if true
                    await self.reset(guild_id)
                    return
                elif end == 2:
                    break

                status = await self.playing_round()
                end = await self.check_status(status)
                if end == 1: #ends game if true
                    await self.reset(guild_id)
                    return
                elif end == 2:
                    break

                status = await self.discussions_round()

    async def play(self):
        members_list = await self.get_members()
        status = await self.current_game.start(self.ctx, members_list)
        return status

    async def playing_round(self):
        status = await self.current_game.playing(self.ctx)
        return status
            
    async def discussions_round(self):
        status = await self.current_game.discussions(self.ctx)
        return status

    async def check_status(self, status):
        if status[0].emoji == '\U0000274C':
            return 1
        elif status[0].emoji == '\U0001F503':
            return 2
        else:
            False
    
    async def check_game(self, guild_id):
        if guild_id in games.keys():
            # self.current_game = games[guild_id]
            return False
            # if self.current_game is None:
            #     await self.create_game(guild_id)
        else:
            await self.create_game(guild_id)

    async def create_game(self, guild_id):
        self.current_game = AmongUs(self.bot, self.ctx, self.gameID)
        await self.save(guild_id)

    async def save(self, guild_id):
        games[guild_id] = self.current_game
        print(games)

    async def reset(self, guild_id):
        games.pop(guild_id)
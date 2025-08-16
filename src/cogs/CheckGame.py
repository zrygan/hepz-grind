import discord
from discord.ext import commands

class CheckGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

async def setup(bot):
    await bot.add_cog(CheckGame(bot))
import discord
from discord.ext import commands

"""
    File for checking the activity of a user
    Source: https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html
"""
class CheckGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if before.activities == after.activities:
            return

        if not after.guild:
            return

        for activity in after.activities:
            if isinstance(activity, discord.Game):
                hep_role = discord.utils.get(after.guild.roles, name="hep")
                if hep_role and hep_role in after.roles:
                    channel = discord.utils.get(
                        after.guild.channels, 
                        name="hepz-valorant-grind"
                    )
                    
                    if channel:
                        await channel.send(
                            f"{after.mention} is about to grind on **{activity.name}** 🎮"
                        )
                break  # stop after the first game activity

async def setup(bot):
    await bot.add_cog(CheckGame(bot))

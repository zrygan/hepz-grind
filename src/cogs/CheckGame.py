import discord
from discord.ext import commands

class CheckGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):

        if before.activities != after.activities: # check if user changed activity

            for activity in after.activities: # check all user activities

                if isinstance(activity, discord.Game): # check if activity is a game
                    hep_role = "hep" # hep role
                    role = discord.utils.get(after.guild.roles, name=hep_role) # get hep role

                    if role in after.roles: # if user has hep role
                        channel = discord.utils.get(after.guild.channels, name="hepz-valorant-grind") # get the grinding channel

                        if channel:
                            await channel.send(f"{after.mention} is about to grind on {activity.name}")

async def setup(bot):
    await bot.add_cog(CheckGame(bot))
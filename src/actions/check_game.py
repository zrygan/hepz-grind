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
            print(activity.type, activity.name)
            if str(activity.type) == "ActivityType.playing":
                name = getattr(activity, "name", None)

                channel = discord.utils.get(
                    after.guild.channels, name="hepz-valorant-grind"
                )

                hep_role = "hep"  # hep role
                role = discord.utils.get(
                    after.guild.roles, name=hep_role
                )  # get hep role

                if role in after.roles:
                    # Hep started playing <gamename>.
                    message = f"{after.mention} started grinding **{name}**!"

                    if channel:
                        await channel.send(message)

                    break


async def setup(bot):
    await bot.add_cog(CheckGame(bot))

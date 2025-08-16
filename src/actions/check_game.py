import discord
from datetime import datetime
from discord.ext import commands

"""
    File for checking the activity of a user
    Source: https://discordpy.readthedocs.io/en/stable/ext/commands/extensions.html
"""


tracker = {}

class CheckGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_presence_update(self, before, after):
        if before.activities == after.activities:
            return

        if not after.guild:
            return

        # Detect stopped activities: present in before but not in after
        for activity in before.activities:
            print("Stopped: ", activity.name, activity.type)

            # if somebody changed their activity (before != after)
            # (i.e., the person stopped playing)
            if activity not in after.activities:
                # name of activity
                name = getattr(activity, "name", None)

                # the key of the activity in the hashmap (it should exist in it)
                key = (name, getattr(activity, "type", None))
                time = tracker.get(key)

                # handle printing the time
                if time:
                    delta = datetime.now() - time
                    # FIXME. fix delta to be formatted:
                    # Hep played <gamename> for <xxx> Hours, <xxx> Mins, <xxx> Seconds
                    message = f"{after.mention} grinded **{name}** for {delta}"
                    
                    # delete entry in the hashmap
                    del tracker[key]

                    channel = discord.utils.get(
                        after.guild.channels, name="hepz-valorant-grind"
                    )

                    if channel:
                        await channel.send(message)

        # Detect started activities: present in after but not in before
        for activity in after.activities:
            print("Started: ", activity.name, activity.type)

            if activity in before.activities:
                continue

            # check for playing activity
            try:
                is_playing = activity.type == discord.ActivityType.playing
            except Exception:
                is_playing = str(getattr(activity, "type", None)) == "ActivityType.playing"

            if not is_playing:
                continue
            
            # name of activity
            name = getattr(activity, "name", None)

            # get name and activity type as a 2-tuple
            # this is the key to the hashmap (`tracker`)
            key = (name, getattr(activity, "type", None))

            # get channel
            channel = discord.utils.get(
                after.guild.channels, name="hepz-valorant-grind"
            )

            # get role
            role = discord.utils.get(after.guild.roles, name="hep")

            if role in after.roles:
                message = f"{after.mention} started grinding **{name}**!"

                # add them to the tracker
                tracker[key] = datetime.now()

                if channel:
                    await channel.send(message)


async def setup(bot):
    await bot.add_cog(CheckGame(bot))

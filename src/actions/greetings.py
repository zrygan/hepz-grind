import discord
from discord.ext import commands


class Greetings(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # use the guild's configured system channel (not a nested `system` attribute)
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member.mention}.")

    @commands.command()
    async def hello(self, ctx, *, member=None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send(f"Hello {member.name}~")
        else:
            await ctx.send(f"Hello {member.name}... This feels familiar.")
        self._last_member = member


async def setup(bot):
    await bot.add_cog(Greetings(bot))

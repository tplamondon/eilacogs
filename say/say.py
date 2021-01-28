from redbot.core import commands


class Say(commands.Cog):
    """Makes the bot say something"""

    @commands.command()
    async def say(self, ctx, *message):
        """Make the bot say something"""
        str = " ".join(message)
        await ctx.message.delete()
        await ctx.send(str)

from redbot.core import commands
from discord.ext.commands import has_permissions

class Say(commands.Cog):
    """Makes the bot say something"""

    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, *message):
        """Make the bot say something"""
        str = " ".join(message)
        await ctx.message.delete()
        await ctx.send(str)

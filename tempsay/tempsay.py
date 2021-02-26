from redbot.core import commands
from discord.ext.commands import has_permissions

class TempSay(commands.Cog):
    """Makes the bot say something"""

    @commands.command()
    @has_permissions(administrator=True)
    async def tempsay(self, ctx, delayTime: float, *message):
        """Make the bot say something and delete after a set time"""
        str = " ".join(message)
        if str == "":
            str = "Nothing Said"
        await ctx.message.delete()
        msg = await ctx.send(str)
        await msg.delete(delay=delayTime)

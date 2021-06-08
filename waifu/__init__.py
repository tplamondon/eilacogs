"""Wafu cog.  Send waifu.pics to a channel."""

from redbot.core.bot import Red
from .waifu import Waifu

def setup(bot: Red):
    """Add the cog to the bot."""
    bot.add_cog(Waifu(bot))

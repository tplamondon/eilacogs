"""Wafu cog.  Send waifu.pics to a channel."""
import asyncio
import discord
import requests
from redbot.core import checks, Config, commands
from redbot.core.bot import Red

class Waifu(commands.cog):
    """Display waifu.pic pictures"""

    def __init__(self, bot: Red):
        self.bot = bot

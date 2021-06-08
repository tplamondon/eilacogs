"""Wafu cog.  Send waifu.pics to a channel."""
import asyncio
import discord
import requests
from redbot.core import checks, Config, commands
from redbot.core.bot import Red
from .catgirl import Catgirl #For access to the getImageURL function

#Global variables
URL = "https://api.waifu.pics/sfw/"

class Waifu(commands.cog):
    """Display waifu.pic pictures"""

    def __init__(self, bot: Red):
        self.bot = bot

    def waifuCmd(self, ctx):
        await ctx.channel.trigger_typing()

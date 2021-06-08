"""Wafu cog.  Send waifu.pics to a channel."""
import asyncio
import discord
import requests
from redbot.core import checks, Config, commands
from redbot.core.bot import Red

#Global variables
URL = "https://api.waifu.pics/sfw/"

class Waifu(commands.cog):
    """Display waifu.pic pictures"""

    def __init__(self, bot: Red):
        self.bot = bot

    def waifuCmd(self, ctx, imageType):
        """Display a waifu.pic picture"""
        await ctx.channel.trigger_typing()

    # [p]waifu
    @commands.command(name="waifu")
    async def _waifu(self, ctx):
        """Display a random waifu"""
        await self.waifuCmd(ctx, "waifu")

    # [p]neko
    @commands.command(name="neko")
    async def _neko(self, ctx):
        """Display a random neko"""
        await self.waifuCmd(ctx, "neko")

    # [p]shinobu
    @commands.command(name="shinobu")
    async def _shinobu(self, ctx):
        """Display a random shinobu"""
        await self.waifuCmd(ctx, "shinobu")


    def getImage(image, title):
        """
        Take a passed url from Waifu.pics, and construct a discord.Embed object

        Parameters:
        -----------
        image : a URL
        title: a string

        Returns:
        -----------
        embed : discord.embed
            a fully constructed discord.Embed object, ready to be sent as a message.
        """
        embed = discord.Embed()
        embed.colour = discord.Colour.red()
        embed.title = title
        embed.url = image
        embed.set_image(url=image)
        return embed

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

    # [p]megumin
    @commands.command(name="megumin")
    async def _megumin(self, ctx):
        """Display a random megumin"""
        await self.waifuCmd(ctx, "megumin")

    # [p]bully
    @commands.command(name="bully")
    async def _bully(self, ctx):
        """Display a random bully"""
        await self.waifuCmd(ctx, "bully")

    # [p]cuddle
    @commands.command(name="cuddle")
    async def _cuddle(self, ctx):
        """Display a random cuddle"""
        await self.waifuCmd(ctx, "cuddle")


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

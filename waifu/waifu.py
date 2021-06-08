"""Wafu cog.  Send waifu.pics to a channel."""
import asyncio
import discord
import requests
from redbot.core import checks, Config, commands
from redbot.core.bot import Red

#Global variables
URL = "https://api.waifu.pics/sfw/"
IMAGE_CATEGORIES = [ "waifu", "neko", "shinobu", "megumin", "bully", "cuddle", "cry",
"hug", "awoo", "kiss", "lick", "pat", "smug", "bonk", "yeet", "blush", "smile", "wave",
"highfive", "handhold", "nom", "bite", "glomp", "slap", "kill", "happy", "wink", "poke",
"dance", "cringe" ]

class Waifu(commands.Cog):
    """Display waifu.pic pictures"""

    def __init__(self, bot: Red):
        self.bot = bot

    async def waifuCmd(self, ctx, imageType):
        """Display a waifu.pic picture"""
        await ctx.channel.trigger_typing()
        requestURL = URL + imageType
        r = requests.get(url=requestURL)
        data = r.json()
        embed = getImage(data["url"], imageType)

        try:
            await ctx.send(embed=embed)
        except discord.errors.Forbidden:
            # No permission to send, ignore.
            pass

    # [p]waifu
    @commands.command(name="waifu")
    async def _waifu(self, ctx, imageType: str = None):
        """Display a random waifu"""
        if not imageType:
            #Display about this module if no command passed
            waifuAbout(ctx)
            return
        elif imageType.lower() not in IMAGE_CATEGORIES:
            imageType = "waifu"

        await self.waifuCmd(ctx, imageType)

    async def waifuAbout(self, ctx):
        """Displays information about the waifu module"""
        customAuthor = "@西木野 真姫#4354"
        embed = discord.Embed()
        embed.title = "About this module"
        embed.add_field(name="Name", value="Waifu Module")
        embed.add_field(name="Author", value=customAuthor)
        embed.add_field(name="Initial Version Date", value="2021-06-08")
        embed.add_field(
            name="Description",
            value="A module to display images from waifu.pics."
            "Valid commands are as follows: waifu, neko, shinobu, megumin, bully"
            "cuddle, cry, hug, awoo, kiss, lick, pat, smug, bonk, yeet, blush, smile"
            "wave, highfive, handhold, nom, bite, glomp, slap, kill, happy, wink, poke"
            "dance, cringe",
        )
        embed.set_footer(text="cogs/waifu")
        await ctx.send(embed=embed)


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

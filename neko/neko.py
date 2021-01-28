from redbot.core import commands
import requests
import json

class Neko(commands.Cog):
    """Posts a random catgirl. Requires requests to be installed"""
    """pip install requests"""

    @commands.command()
    async def neko(self, ctx):
        """Posts a random catgirl"""
        response = requests.get("https://nekos.moe/api/v1/random/image?nsfw=false")
        JSON = response.json()
        imageID = JSON["images"][0]["id"]
        await ctx.send("https://nekos.moe/image/"+imageID)

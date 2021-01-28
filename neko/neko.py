from redbot.core import commands
import requests
import json

class Neko(commands.Cog):
    """Looks up source of anime and pictures, may get NSFW results. Requires requests to be installed"""
    """pip install requests"""

    @commands.command()
    async def neko(self, ctx):
        response = requests.get("https://nekos.moe/api/v1/random/image?nsfw=false")
        JSON = response.json()
        imageID = JSON["images"][0]["id"]
        await ctx.send("https://nekos.moe/image/"+imageID)

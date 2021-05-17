from redbot.core import commands, Config
import discord
import requests
import json


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):-1]
    return text  # or whatever


class FF14(commands.Cog):

    def __init__(self):
        self.config = Config.get_conf(self, identifier=141414141414)

        default_member = {
            "characterURL": "",
            "characterID": 0
        }
        self.config.register_member(**default_member)


    @commands.group(name="ff14", invoke_without_command=False)
    async def ff14Command(self, ctx):
        """Shouldn't run"""

    @ff14Command.command(name="set")
    async def ff14Set(self, ctx, url):
        """Set the URL for a person's character

        Parameters:
        -----------
        url: a url pointing to the ff14 lodestone character
        """
        if(url.startswith("https://na.finalfantasyxiv.com/lodestone/character/") == True):
            await self.config.member(ctx.author).characterURL.set(url)
            id = remove_prefix(url, "https://na.finalfantasyxiv.com/lodestone/character/")
            await self.config.member(ctx.author).characterID.set(id)
            msg = f"Set {ctx.author} FF14 character to {url} with id {id}"
            await ctx.send(msg)
        else:
            await ctx.send("Not a character URL")

    @ff14Command.command(name="get")
    async def ff14Get(self, ctx, user: discord.Member):
        """Set the URL for a person's character

        Parameters:
        -----------
        url: a url pointing to the ff14 lodestone character
        """
        url = await self.config.member(ctx.author).characterURL()
        id = await self.config.member(ctx.author).characterID()
        if(url==""):
            await ctx.send("No character associated with this user")
        else:
            #get json response
            response = requests.get(f"https://xivapi.com/character/{id}")
            JSON = response.json()
            portrait = JSON["Character"]["Portrait"]
            job = JSON["Character"]["ActiveClassJob"]["UnlockedState"]["Name"]
            name = JSON["Character"]["Name"]
            server = JSON["Character"]["Server"]

            #build embed
            await ctx.trigger_typing()
            embed = discord.Embed()
            embed.colour = discord.Colour.blue()
            embed.title = name
            embed.url = url
            embed.add_field(name="Job", value=job, inline=False)
            embed.add_field(name="Server", value=server, inline=False)
            embed.set_image(url=portrait)

            await ctx.send(embed=embed)

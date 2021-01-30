from urllib import parse
import discord
from redbot.core import commands


def sauceLink(url: str):
    return "https://saucenao.com/search.php?url={}".format(parse.quote_plus(url))
def iqdbLink(url: str):
    return "https://iqdb.org/?url={}".format(parse.quote_plus(url))
def yandexLink(url: str):
    return "https://yandex.com/images/search?url={}&rpt=imageview".format(parse.quote_plus(url))

class Sauce(commands.Cog):
    """
    Uses IQDB to search for source of a image
    Code used from https://github.com/PoldekPL/SauceBot/blob/master/bot.py and converted to a redbot cog. This code follows the LICENCE file of MIT License
    """

    @commands.command()
    async def sauce(self, ctx, url):
        embed = discord.Embed(title="Sauce Links")
        embed.add_field(name="\u200b", value="**[IQDB]({})\n**".format(iqdbLink(url)), inline=False)
        embed.add_field(name="\u200b", value="**[SauceNAO]({})\n**".format(sauceLink(url)), inline=False)
        embed.add_field(name="\u200b", value="**[Yandex]({})\n**".format(yandexLink(url)), inline=False)
        await ctx.send(embed=embed)

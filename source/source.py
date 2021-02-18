from redbot.core import commands
import tracemoepy
from tracemoepy.errors import EmptyImage, EntityTooLarge, ServerError, TooManyRequests


async def assignDefaultStringValue(stringVar, val):
    """
    Assigns default value to string if string is null
    """
    if stringVar == None:
        stringVar = val
    return

async def postSourceFunction(ctx, imageURL):
    """helper method"""
    try:
        tracemoe = tracemoepy.tracemoe.TraceMoe()
        result = tracemoe.search(imageURL.strip("<>"), is_url=True)
        titleEnglish = result.docs[0].title_english
        anilistID = f"{result.docs[0].anilist_id}"
        episode = f"{result.docs[0].episode}"
        similarity = float(result.docs[0].similarity)

        assignDefaultStringValue(titleEnglish, "No Title Found")
        assignDefaultStringValue(anilistID, "No anilistID Found")
        assignDefaultStringValue(episode, "No Episode Found")

        URL = "https://anilist.co/anime/" + anilistID

        if similarity < 0.9:
            await ctx.send(
                "Anime: "
                + titleEnglish
                + "\nEpisode: "
                + episode
                + "\nSimilarity: "
                + ("%.3f" % ((similarity) * 100))
                + "\nWARNING: Similarity less than 90%, result may not be accurate"
                + "\n"
                + URL
            )
        else:
            await ctx.send(
                "Anime: "
                + titleEnglish
                + "\nSimilarity: "
                + ("%.3f" % ((similarity) * 100))
                + "%"
                + "\nEpisode: "
                + episode
                + "\n"
                + URL
            )
    except TooManyRequests:
        await ctx.send("Please try again later")
    except EntityTooLarge:
        await ctx.send("Too big of file image")
    except ServerError:
        await ctx.send(
            "Server error. Ensure image is provided as URL and points directly to png or jpg image"
        )
    except EmptyImage:
        await ctx.send(
            "Empty image provided. Ensure image is provided as URL and points directly to png or jpg image"
        )


class Source(commands.Cog):
    @commands.group(name="source", invoke_without_command=True)
    async def sourceCommand(self, ctx):
        """Looks for source of a screenshot from anime, using trace.moe

        Parameters:
        -----------
        make sure to attach a png or jpg image, or type 'source url URL_HERE'
        """
        await ctx.trigger_typing()
        if not ctx.message.attachments:
            await ctx.send_help(command="source")
            return
        else:
            imageURL = ctx.message.attachments[0].url
            await postSourceFunction(ctx, imageURL)
            return

    @sourceCommand.command(name="url")
    async def urlSource(self, ctx, imageURL):
        """Looks for source of a screenshot from anime, using trace.moe

        Parameters:
        -----------
        imageURL: a url pointing to a image from an anime episode. Can be surrounded with <> to suppress embeds in Discord
        """
        await postSourceFunction(ctx, imageURL)

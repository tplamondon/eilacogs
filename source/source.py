from redbot.core import commands
import tracemoepy

class Source(commands.Cog):
    """Looks up source of anime and pictures, may get NSFW results. Requires tracemoepy to be installed"""

    @commands.command()
    async def source(self, ctx, imageURL):
        """Looks for source of image"""
        tracemoe = tracemoepy.tracemoe.TraceMoe()
        try:
            result = tracemoe.search(imageURL, is_url = True)
            titleEnglish = f'{result.docs[0].title_english}'
            anilistID = f'{result.docs[0].anilist_id}'
            await ctx.send("Anime: " + titleEnglish + "\nAnilistID: "+anilistID)
        except TooManyRequests:
            await ctx.send("Too many requests sent")
        except EntityTooLarge:
            await ctx.send("Too big of file image")
        except ServerError:
            await ctx.send("Server error")
        except InvalidToken:
            await ctx.send("Invalid token")
        except EmptyImage:
            await ctx.send("Empty image provided")
        except InvalidPath:
            await ctx.send("Invalid path, bot had an error with .save method")
        # Your code will go here

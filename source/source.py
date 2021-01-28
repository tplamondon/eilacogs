from redbot.core import commands
import tracemoepy
import math

class Source(commands.Cog):
    """Looks up source of anime and pictures, may get NSFW results. Requires tracemoepy to be installed"""
    """ run 'pip install tracemoepy' on your redbot virtual environment to install"""

    @commands.command()
    async def source(self, ctx, imageURL):
        """
        Looks for source of image

        Parameters:
        -----------
        imageURL: a url pointing to a image from an anime episode. Can be surrounded with < or > to supressed embeds in discord
        """
        tracemoe = tracemoepy.tracemoe.TraceMoe()
        try:
            await ctx.trigger_typing()
            result = tracemoe.search(imageURL.strip("<>"), is_url = True)
            titleEnglish = f'{result.docs[0].title_english}'
            anilistID = f'{result.docs[0].anilist_id}'
            episode = f'{result.docs[0].episode}'
            similarity = float(f'{result.docs[0].similarity}')
            url = "https://anilist.co/anime/"+anilistID
            if(similarity < 0.8):
                await ctx.send("Anime: " + titleEnglish + "\nEpisode: " + episode +"\nWARNING: Similarity less than 80%, result may not be accurate"+ "\n"+url)
            else:
                await ctx.send("Anime: " + titleEnglish + "\nSimilarity: " + ('%.3f'%((similarity)*100)) +"%" + "\nEpisode: " + episode + "\n"+url)
        except TooManyRequests:
            await ctx.send("Too many requests sent")
        except EntityTooLarge:
            await ctx.send("Too big of file image")
        except ServerError:
            await ctx.send("Server error")
        #except InvalidToken:
        #    await ctx.send("Invalid token")
        except EmptyImage:
            await ctx.send("Empty image provided")
        #except InvalidPath:
        #    await ctx.send("Invalid path, bot had an error with .save method")

import discord
from discord.ext import commands


class invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # '!invite' command:
    async def invite(self, ctx):
        embed = discord.Embed(
            title="BOT INVITE LINK",
            description="You can invite me to your server by [Clicking Here](https://discord.com/api/oauth2/authorize?client_id=1072079088111583335&permissions=8&scope=bot)",
            color=discord.Color.blue())

        await ctx.send(embed=embed)


# Setup/Register the cog:
async def setup(bot):
    await bot.add_cog(invite(bot))

import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # '!help' command:
    async def help(self, ctx):
        embed = discord.Embed(
            description='Welcome to the help section. Here is the List of commands I can do: ',
            title='Bot Commands',
            color=discord.Color.blue()
        )

        embed.add_field(name='\U000027A1 hi, Hi, hello, Hello',
                        value='For Greetings', inline=False)
        embed.add_field(name='\U000027A1 bye, Bye',
                        value='For Goodbyes', inline=False)
        embed.add_field(name='\U000027A1 How are you?',
                        value='For Asking how I am', inline=False)
        embed.add_field(name='\U000027A1 What\'s your name?',
                        value='For Asking my name', inline=False)
        embed.add_field(name='\U000027A1 cool',
                        value='For reaction', inline=False)
        embed.add_field(name='\U000027A1 !joke',
                        value='For Random Dad Joke...haha', inline=False)
        embed.add_field(name='\U000027A1 !invite',
                        value='For Invite Link', inline=False)

        await ctx.send(embed=embed)


# Setup/Register the cog:
async def setup(bot):
    await bot.add_cog(help(bot))

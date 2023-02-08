import discord
from discord.ext import commands


class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild_name = member.guild.name
        print("Server Name: ", guild_name)

        channel = discord.utils.get(
            member.guild.channels,
            name="general"
        )
        channel_id = channel.id
        print("Channel Id: ", channel)

        await channel.send(f"Hey {member.mention}! \n\n\U0001F389\U0001F389WELCOME TO THE SERVER\U0001F389\U0001F389\n\n")
        await member.send(f"Welcome to the {guild_name} Discord Server \nUse ***'!help'*** in <#{channel_id}> to see the list of commands I can do!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(
            member.guild.channels,
            name="general"
        )
        await channel.send(f"{member.mention} has left the server.")


async def setup(bot):
    await bot.add_cog(members(bot))

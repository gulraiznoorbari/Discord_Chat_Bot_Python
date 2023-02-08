import discord
from discord.ext import commands


class members(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = await self.bot.get_guild(1065617002393247808)
        general_channel = await self.bot.fetch_channel(1065617003949338676)
        await general_channel.send(f"Hey {member.mention}! \n\n\U0001F389\U0001F389WELCOME TO THE SERVER\U0001F389\U0001F389\n\nThis is <#{general_channel}> channel.")
        await member.send(f"Welcome to the {guild.name} Discord Server \n Use ```!help``` to see the list of commands I can do!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await member.send(f"{member.mention} has left the server.")


async def setup(bot):
    await bot.add_cog(members(bot))

import discord
import random
from discord.ext import commands


class greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Prevents the bot from responding to itself:
        if message.author == self.bot.user:
            return

        if message.channel.name == "general":

            greetings = ["hello", "hi", "Hello", "Hi"]
            for greeting in greetings:
                if message.content == greeting:
                    await message.channel.send(f"Hey {message.author.mention}! Welcome to the server!\nUse ***'!help'*** to see the list of commands I can do!")

            if (message.content == "bye" or message.content == "Bye"):
                await message.channel.send(f"Bye {message.author.name}! See you later!")

            if message.content == "How are you?":
                await message.channel.send("I'm fine, thanks for asking! \nWhat about you?")

            if message.content == "What's your name?":
                await message.channel.send("My name is Billy and I talk trash!")

            dad_jokes = [
                "Why do fathers take an extra pair of socks when they go golfing? In case they get a hole in one!",
                "Dear Math, grow up and solve your own problems.",
                "What has more letters than the alphabet? The post office!",
                "Why are elevator jokes so classic and good? They work on so many levels!",
                "What do you call a fake noodle? An impasta!",
                "What do you call a belt made out of watches? A waist of time!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "Why don't skeletons ever go trick or treating? Because they have no body to go with!",
                "What's brown and sticky? A stick!"]
            joke = random.choice(dad_jokes)
            if message.content == "!joke":
                await message.channel.send(joke)

            # If the message is "cool", add a reaction to the message:
            if message.content == "cool":
                await message.add_reaction("\U0001F60E")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        await before.channel.send(
            f'{before.author.mention} edited their message.\n'
            f'**Before:** {before.content}\n'
            f'**After:** {after.content}\n'
            f'**Are your fingers broken???**'
        )


async def setup(bot):
    await bot.add_cog(greetings(bot))

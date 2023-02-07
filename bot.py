import os
import asyncio
import dotenv
import discord
from discord.ext import commands

# Load the .env file:
dotenv.load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

# Intents allow you to specify which events you want to receive:
intents = discord.Intents.all()
intents.members = True


# intents = discord.Intents.default()
# intents.message_content = True

# Create a bot with the specified prefix and intents:
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
)

bot.remove_command('help')

# @bot.event
# # When the bot is ready, print a message to the console:
# async def on_ready():
#     print(f'We have logged in as {bot.user}')

#     await bot.change_presence(activity=discord.Game(name="with your feelings!"))

#     print("Bot Activated!")


async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')


async def main():
    await load()
    await bot.start(bot_token)


asyncio.run(main())

# extensions = [
#     'cogs.greetings',
#     'cogs.members',
#     'cogs.help',
#     'cogs.invite',
# ]

# if __name__ == '__main__':
#     for extension in extensions:
#         bot.load_extension(extension)

# bot.run(bot_token)

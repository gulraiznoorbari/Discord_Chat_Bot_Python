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

# Create a bot with the specified prefix and intents:
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    case_insensitive=True,
    help_command=None,
)


@bot.event
# When the bot is ready, print a message to the console:
async def on_ready():
    print(f'We have logged in as {bot.user}')
    # Change the bot's presence:
    await bot.change_presence(activity=discord.Game(name="with your feelings!"))
    print("Bot Activated!")


async def load():
    # Load all cogs in the cogs folder:
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

# Run the bot:


async def main():
    # Load all cogs:
    await load()
    # Start the bot:
    await bot.start(bot_token)

# Run the main function:
asyncio.run(main())

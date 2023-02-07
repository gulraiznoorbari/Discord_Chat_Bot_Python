import os
import discord
from discord.ext import commands
import dotenv

# Load the .env file:
dotenv.load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

# Intents allow you to specify which events you want to receive:
intents = discord.Intents.all()

# Create a bot with the specified prefix and intents:
bot = commands.Bot(
    command_prefix='!',
    intents=intents,
    help_command=None,
    case_insensitive=True,
)


@bot.event
# When the bot is ready, print a message to the console:
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print("Bot Activated!")


@bot.command()
# '!channel' command:
async def channel(ctx):
    general_channel = '1065617003949338676'
    await ctx.send(f"Hey {ctx.message.author.mention}! \n\n\U0001F389\U0001F389WELCOME TO THE SERVER\U0001F389\U0001F389\n\nThis is <#{general_channel}> channel.")


@bot.command()
# '!help' command:
async def help(ctx):
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
    embed.add_field(name='\U000027A1 !joke',
                    value='For Random Dad Joke...haha', inline=False)

    await ctx.send(embed=embed)

bot.run(bot_token)

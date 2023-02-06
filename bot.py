import os
import random
import dotenv
import discord

dotenv.load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

# Intents allow you to specify which events you want to receive:
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
# When the bot is ready, print a message to the console:
async def on_ready():
    print(f'We have logged in as {client.user}')
    print("Bot Activated!")


@client.event
async def on_message(message):
    # Prevents the bot from responding to itself:
    if message.author == client.user:
        return

    if message.channel.name == "general":

        greetings = ["hello", "hi", "Hello", "Hi"]
        for greeting in greetings:
            if message.content == greeting:
                await message.channel.send(f"Hey {message.author.name}! Welcome to the server!")

        if (message.content == "bye" or message.content == "Bye"):
            await message.channel.send(f"Bye {message.author.name}! See you later!")

        if message.content == "How are you?":
            await message.channel.send("I'm fine, thanks for asking!")

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

        if message.content == "!help":
            # await message.reply(f'Visit #{client.get_channel(1072173149426303069)} for the list of commands I can do!', mention_author=True)

            await message.reply(
                f'List of commands I can do:\n'
                f'\U000027A1 hi, Hi, hello, Hello (for greetings)\n'
                f'\U000027A1 bye, Bye (for goodbyes)\n'
                f'\U000027A1 How are you?\n'
                f"\U000027A1 What's your name?\n"
                f'\U000027A1 !joke (for random dad joke...haha)\n'
                f'These commands will only work in #general channel.',
            )


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author.name} edited their message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
        f'Your Fingers are broken!'
    )


@client.event
async def on_member_join(message, member):
    message.channel.send(f"{member} has joined the server!")


@client.event
async def on_member_remove(message, member):
    message.channel.send(f"{member} has left the server.")

client.run(bot_token)

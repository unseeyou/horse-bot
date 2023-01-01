import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
horse = 'https://media.istockphoto.com/photos/questioning-horse-picture-id637702884?k=20&m=637702884&s=612x612&w=0&h=3ZA35KBH3rce8waza4rkLkNp6aS73delq3OuSZLlNic='
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix='h ', intents=intents, case_insensitive=True)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print(f"{horse} lol")


@bot.listen()
async def on_message(message):
    if message.author.bot:
        pass
    elif 'horse' in message.content.lower():
        await message.channel.send('https://tenor.com/view/you-have-alerted-the-horse-horse-gt-when-the-gif-24722142')
    else:
        pass


@bot.tree.command(description='you what now?', name='huh')
async def huh(interaction: discord.Interaction):
    await interaction.response.send_message(horse)


async def main():
    async with bot:
        await bot.start(TOKEN)


asyncio.run(main())

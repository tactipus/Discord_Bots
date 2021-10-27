import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import subprocess

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# client = discord.Client()
#
# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break
#
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )

intents = discord.Intents().all()
client = commands.Bot(command_prefix = ".", intents=intents)


@client.event
async def on_ready():
   print("Bot is ready.")


@client.event
async def on_member_join(member):
    button = "OK"

    applescript = """
    display dialog "{} has either been removed or has joined." ¬
    with title "Discord Alert" ¬
    with icon caution ¬
    buttons "{}"
    """.format(member, button)

    subprocess.call("osascript -e '{}'".format(applescript), shell=True)

    print(f"{member} has joined the server.")


@client.event
async def on_member_remove(member):
    button = "OK"

    applescript = """
    display dialog "{} has either been removed or has joined." ¬
    with title "Discord Alert" ¬
    with icon caution ¬
    buttons "{}"
    """.format(member, button)

    subprocess.call("osascript -e '{}'".format(applescript), shell=True)
    print(f"{member} has left the server.")


#@client.command()
#async def ping(ctx):


client.run(TOKEN)
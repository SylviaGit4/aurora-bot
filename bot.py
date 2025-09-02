import discord
from discord.ext import commands
import json

with open('config.json', 'r') as cfg:
    data = json.load(cfg)

BOT_TOKEN = data["token"]
CHANNEL_ID = 1412224167537016922

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

#Shows the bot is up and running.
@bot.event
async def on_ready():
    print("Bot running.")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Bot running.")

#Shows list of commands.
@bot.command()
async def commands(ctx):
    await ctx.send("# Commands List \n!commands - Shows list of commands. \n!test_up - Test to see if bot is correctly recieving commands. \n")

#Checks to see if the bot is correctly recieving commands.
@bot.command()
async def test_up(ctx):
    await ctx.send("Bot currently up.")

bot.run(BOT_TOKEN)
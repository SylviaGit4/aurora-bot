import discord
from discord.ext import commands

BOT_TOKEN = "MTQxMTc4OTMxNDQyOTU1MDY3Ng.GX_YCv.rLzvA_qoj2Lcb5JL1DxQYOEKirrO4Go2pQ7HWc"
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
    await ctx.send("# Commands List \n!commands - Shows list of commands. \n!test_up - Test to see if bot is correctly recieving commands. \n!sum - Adds numbers and shows result.")

#Checks to see if the bot is correctly recieving commands.
@bot.command()
async def test_up(ctx):
    await ctx.send("Bot currently up.")

#Shows the sum of numbers in a message.
@bot.command()
async def sum(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    await ctx.send(f"Result: {result}")


bot.run(BOT_TOKEN)
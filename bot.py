import discord
from discord.ext import commands

BOT_TOKEN = "MTQxMTc4OTMxNDQyOTU1MDY3Ng.GX_YCv.rLzvA_qoj2Lcb5JL1DxQYOEKirrO4Go2pQ7HWc"
CHANNEL_ID = 1412224167537016922

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot running.")

bot.run(BOT_TOKEN)
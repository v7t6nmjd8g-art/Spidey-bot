import os
import discord
from discord.ext import commands
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.default()
intents.message_content = true
bot = commands.Bot(command_prefix="!" , intents=intents)
@bot.event 
async def on_ready ():
  print(f"🕷️ Spidey bot est connecté en tant que {bot.user}"
@bot.command()
async def ping(ctx):
  await ctx.send ("🏓 pong ! spidey bot fonctionne.")

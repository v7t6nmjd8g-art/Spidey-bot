import os
import discord
from discord.ext import commands
import feedparser
TOKEN = os.getenv("DISCORD_TOKEN")
RSS_URL = "https://rss.app/feeds/WtYR8fnVhYK9yQRI.xml"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!" , intents=intents)
@bot.event 
async def on_ready ():
  print(f"🕷️ Spidey bot est connecté en tant que {bot.user}")
@bot.command()
async def ping(ctx):
  await ctx.send ("🏓 pong ! spidey bot fonctionne.")
bot.run(TOKEN) 

import os
import discord
from discord.ext import commands, tasks
import feedparser
TOKEN = os.getenv("DISCORD_TOKEN")
RSS_URL = "https://rss.app/feeds/WtYR8fnVhYK9yQRI.xml"
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!" , intents=intents)
@bot.event 
async def on_ready ():
  print(f"🕷️ Spidey bot est connecté en tant que {bot.user}")
  @tasks.loop(minutes=5)
async def check_leaks():
    feed = feedparser.parse(RSS_URL)

    if feed.entries:
        channel = discord.utils.get(bot.get_all_channels(), name="codm-leaks")

        if channel:
            latest = feed.entries[0]
            await channel.send(
                f"🚨 Nouveau leak CODM !\n{latest.title}\n{latest.link}"
            )

@bot.event
async def on_ready():
    print(f"🕷️ Spidey bot est connecté en tant que {bot.user}")
    check_leaks.start()
@bot.command()
async def ping(ctx):
  await ctx.send ("🏓 pong ! spidey bot fonctionne.")
bot.run(TOKEN) 

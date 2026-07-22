import os
import discord
from discord.ext import commands, tasks
import feedparser

TOKEN = os.getenv("DISCORD_TOKEN")
RSS_URL = "https://rss.app/feeds/WtYR8fnVhYK9yQRI.xml"

last_leak = None

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@tasks.loop(minutes=5)
async def check_leaks():
    global last_leak

    feed = feedparser.parse(RSS_URL)

    if feed.entries:
        latest = feed.entries[0]

        # Empêche d'envoyer le même leak plusieurs fois
        if latest.link == last_leak:
            return

        channel = discord.utils.get(bot.get_all_channels(), name="⌁・leaks")

        if channel:
            await channel.send(
                f"🚨 Nouveau leak CODM !\n{latest.title}\n{latest.link}"
            )

            last_leak = latest.link


@bot.event
async def on_ready():
    print(f"🕷️ Spidey bot est connecté en tant que {bot.user}")
    print("TEST NOUVELLE VERSION")
    check_leaks.start()


@bot.command()
async def ping(ctx):
    await ctx.send("🏓 pong ! spidey bot fonctionne.")


@bot.command()
async def testleak(ctx):
    await ctx.send("🚨 Test leak CODM : Spidey Bot fonctionne !")


bot.run(TOKEN)

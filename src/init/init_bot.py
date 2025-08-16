import discord, logging, os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!h ", intents=intents)


@bot.event
async def on_ready():
    # load cogs when the bot is ready
    await bot.load_extension("src.actions.check_game")
    await bot.load_extension("src.actions.greetings")


@bot.command()
async def hello(ctx):
    await ctx.send("I am Hepz-Bot, the android sent by CyberLife")

@bot.command()
async def bye(ctx):
    await ctx.send("Bye! I am Hepz-Bot, the android sent by CyberLife")

def bot_init():
    if token is not None:
        print("Bot is ready")
        bot.run(token, log_handler=handler, log_level=logging.DEBUG)
    else:
        exit(1)

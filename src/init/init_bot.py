import discord, logging, os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print(f'I am Hepz-Bot, the android sent by CyberLife')

    await bot.load_extension('src.cogs.CheckGame') # loads CheckGame cog

def bot_init():
    if token is not None:
        bot.run(token, log_handler=handler, log_level=logging.DEBUG)
    else:
        exit(1)
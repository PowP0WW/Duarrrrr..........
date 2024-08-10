import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def roll(ctx, num_sides: int = 6):
    """Rolls a die with a specified number of sides (default is 6)."""
    roll_result = random.randint(1, num_sides)
    await ctx.send(f'🎲 You rolled a {roll_result} on a {num_sides}-sided die!')

bot.run("token")

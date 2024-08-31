import discord
from discord.ext import commands
import random
import requests

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
    """Rolls a dice with a specified number of sides (default is 6)."""
    roll_result = random.randint(1, num_sides)
    await ctx.send(f'🎲 You rolled a {roll_result} on a {num_sides}-sided dice!')

@bot.command()
async def meme1(ctx):
    with open('images/meme1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def meme2(ctx):
    with open('images/meme2.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def meme3(ctx):
    with open('images/download.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

jingliu_memes = ['images/legendary_meme.jpg', 'images/rare_meme.jpg']

@bot.command()
async def jingliumeme(ctx):
    selected_meme = random.choice(jingliu_memes)
    with open(selected_meme, 'rb') as f:
        picture = discord.File(f)
    embed = discord.Embed(title="Here's a Jingliu meme for you!")
    await ctx.send(embed=embed, file=picture)

memes = {
    'common': ['images/meme1.jpg', 'images/meme2.jpg'],
    'rare': ['images/rare_meme.jpg'],
    'legendary': ['images/legendary_meme.jpg']
}

@bot.command()
async def meme(ctx):
    rarity = random.choices(['common', 'rare', 'legendary'], [0.8, 0.15, 0.05])[0]
    meme_path = random.choice(memes[rarity])
    with open(meme_path, 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")

import discord
from settings import TOKEN
from bot_code import *
from discord.ext import commands


# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default() 
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")

@bot.command()
async def generate_pass(ctx, passlength = 10):
    await ctx.send(password_gen(passlength))

@bot.command()
async def emoji_random(ctx):
    await ctx.send(random_emoji())

@bot.command()
async def dice_roll(ctx):
    await ctx.send(roll_dice())

@bot.command()
async def coin_flip(ctx):
    await ctx.send(flip_coin())

bot.run(TOKEN)

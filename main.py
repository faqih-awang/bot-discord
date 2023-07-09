import discord
# from settings import whatsurproblem
from bot_code import *

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default() 
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Kita telah masuk sebagai {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('halo'):
        await message.channel.send("Hi!")
    elif message.content.startswith('emoji'):
        await message.channel.send(random_emoji())
    elif message.content.startswith('flip'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('roll'):
        await message.channel.send(roll_dice())
    elif message.content.startswith('bye'):
        await message.channel.send(":wave:")
    elif message.content.startswith('generate'):
        await message.channel.send(password_gen(10))
    else:
        await message.channel.send(message.content)


client.run("MTEyNDk2MjU1ODMxNTYwMjAwMg.GUOrlA.qdqxVnnpBwC6kQ2UyET-yIk-1KMHTqEs5z6wzw")
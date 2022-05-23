import os

import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

bot = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    test_quotes = [
        'WAGMI',
        'GMI FR',
    ]

    lee = "Lee Bell indeed"
    
    if message.content == 'am I gmi?':
        response = random.choice(test_quotes)
        await message.channel.send(response)
    
    if message.content == 'lee bell' :
        response = lee
        await message.channel.send(response)
# @client.event
# async def on_message(message,member : discord.Member):
#     if message.author == client.user:
#         return

#     test_quotes_2 = [
#         'WAGMI',
#         'GMI FR',
#     ]

#     if message.content == 'Is '+ member +'gmi?':
#         response = random.choice(test_quotes_2)
#         await message.channel.send(response)
    
@bot.command()
async def gmi(message, member: discord.Member):
    gmi_quotes = [
        'GMI FR FR'
    ]
    response = random.choice(member + gmi_quotes)
    await message.channel.send(response)
   
   
client.run(TOKEN)
bot.run(TOKEN)



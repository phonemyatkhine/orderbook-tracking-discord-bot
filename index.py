import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from database import databaseConnection

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
   
connection = databaseConnection()
conn = connection.connect()
cursor = connection.getCursor(conn)
# sql = '''   CREATE TABLE EMPLOYEE(
#                     FIRST_NAME CHAR(20) NOT NULL,
#                     LAST_NAME CHAR(20),
#                     AGE INT, 
#                     SEX CHAR(1),
#                     INCOME FLOAT) ''' 

sql = ''' DROP TABLE EMPLOYEE '''
connection.executeSql(cursor,sql)

@bot.command()
async def test(ctx):
    print(ctx)
    await ctx.channel.send("test")

@bot.command()
async def testicle(ctx):
    await ctx.channel.send("big balls")

@bot.command()
async def gmi(ctx,  member: discord.Member):
    await ctx.channel.send(member.name + " gmi fr")
    
@bot.command()
async def new_collection(ctx,arg):
    print(arg)
    await ctx.channel.send("Making order book for new collection "+arg)

bot.run(TOKEN)



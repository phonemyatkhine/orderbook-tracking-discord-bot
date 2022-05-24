import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from database import databaseConnection

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

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
    connection = databaseConnection()
    connection.connect()
    connection.getCursor()
    split = arg.split("@")
    # "insert into contacts (name, phone, email) values (?, ?, ?)",
    #         (name, phone, email)
    new_collection_sql = "INSERT INTO COLLECTIONS (NAME, TWITTER_LINK) VALUES ("+split[0]+","+split[1]+")"
    print(new_collection_sql)
    try :
        connection.executeSql(new_collection_sql)
        connection.commit()    
        connection.close()
        await ctx.channel.send("New collection " +split[0]+" created ")
    except :
        await ctx.channel.send("Collection creation failed")

@bot.command()
async def show_collections(ctx):
    connection = databaseConnection()
    connection.connect()
    connection.getCursor()
    show_collection_sql = "SELECT * FROM COLLECTIONS"
    try :
        collections = connection.fetchAll(show_collection_sql)
        connection.commit()
        connection.cursor()
        await ctx.channel.send("Collections "+collections)
    except :
        await ctx.channel.send("Collection fetched failed")
        
@bot.command()
async def make_tables(ctx):
    connection = databaseConnection()
    connection.connect()
    connection.getCursor()
    collections_sql = ''' CREATE TABLE COLLECTIONS(
                            COLLECTION_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            NAME VARCHAR(255) NOT NULL,
                            TWITTER_LINK VARCHAR(255),
                            DISCORD_LINK VARCHAR(255), 
                            IMAGE_LINK VARCHAR(255) 
                            ) '''
    buy_orders_sql = ''' CREATE TABLE BUY_ORDERS(
                            BUY_ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            COLLECTION_ID INT NOT NULL,
                            DISCORD_ID VARCHAR(255) NOT NULL,
                            PRICE FLOAT NOT NULL ,
                            CONSTRAINT fk_collections
                                FOREIGN KEY (collection_id)
                                REFERENCES collections(id) 
                        )'''
    
    sell_orders_sql = ''' CREATE TABLE SELL_ORDERS(
                            SELL_ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            COLLECTION_ID INT NOT NULL,
                            DISCORD_ID VARCHAR(255) NOT NULL,
                            PRICE FLOAT NOT NULL ,
                            CONSTRAINT fk_collections
                                FOREIGN KEY (collection_id)
                                REFERENCES collections(id) 
                        )'''
    
    try :
        connection.executeSql(collections_sql)
        connection.executeSql(buy_orders_sql)
        connection.executeSql(sell_orders_sql)
        connection.commit()
        connection.close()
        await ctx.channel.send("Tables created successfully")
    except :
        await ctx.channel.send("Tables creation error")
        
bot.run(TOKEN)
                      


    
                    

import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from bot_commands.collections import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
bot.add_cog(Collections(bot))

# @bot.command()
# async def test(ctx):
#     print(ctx)
#     await ctx.channel.send("test")

# @bot.command()
# async def testicle(ctx):
#     await ctx.channel.send("big balls")

# @bot.command()
# async def gmi(ctx,  member: discord.Member):
#     await ctx.channel.send(member.name + " gmi fr")

@bot.command(name="make_tables")
@commands.has_role("Devs")
async def make_tables(ctx):
    conn = load_db()
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
                            VERIFIED BOOLEAN,
                            CONSTRAINT fk_collections
                                FOREIGN KEY (collection_id)
                                REFERENCES collections(id) 
                        )'''
    
    sell_orders_sql = ''' CREATE TABLE SELL_ORDERS(
                            SELL_ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            COLLECTION_ID INT NOT NULL,
                            DISCORD_ID VARCHAR(255) NOT NULL,
                            PRICE FLOAT NOT NULL ,
                            VERIFIED BOOLEAN,
                            CONSTRAINT fk_collections
                                FOREIGN KEY (collection_id)
                                REFERENCES collections(id)
                        )'''
    
    try :
        conn.executeSql(collections_sql)
        conn.executeSql(buy_orders_sql)
        conn.executeSql(sell_orders_sql)
        close_db(conn)
        await ctx.channel.send("Tables created successfully")
    except :
        await ctx.channel.send("Tables creation error")
@make_tables.error
async def make_tables_error(ctx, error):
    if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
        await ctx.channel.send("You do not have required permissions to use this command.")

@bot.command(name="make_buy_order")
async def make_buy_order(ctx,arg):
    split = arg.split("$")
    print(split)

bot.run(TOKEN)
                      


    
                    

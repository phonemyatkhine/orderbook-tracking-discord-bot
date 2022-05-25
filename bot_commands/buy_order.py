from dis import disco
from discord.ext import commands
from database.connect import load_db
from database.connect import close_db

class BuyOrder(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="buy_order")
    async def buy_order(self, ctx, arg):
        split = arg.split("$")
        name = split[0]
        price = split[1]
        discord_id = str(ctx.author)
        conn = load_db()
        get_collection_id_sql = "SELECT COLLECTION_ID FROM COLLECTIONS WHERE NAME = '" + name + "' "
        print(get_collection_id_sql)
        collection_id = conn.fetchOne(get_collection_id_sql)
        collection_id = str(collection_id[0])
        buy_order_sql = "INSERT INTO BUY_ORDERS (COLLECTION_ID, DISCORD_ID, PRICE) VALUES ('"+collection_id+"','"+discord_id+"','"+price+"')"
        print(buy_order_sql)
        try:
            conn.executeSql(buy_order_sql)
            close_db(conn)
            await ctx.channel.send("Buy order successfully created.")
        except:
            await ctx.channel.send("Buy order creation failed.")
          
    @commands.command()
    async def show_buy_orders(self, ctx):
        conn = load_db()
        show_buy_orders_sql = "SELECT bo.*,c.NAME FROM BUY_ORDERS bo JOIN COLLECTIONS c ON c.COLLECTION_ID = bo.COLLECTION_ID"
        try :
            collections = conn.fetchAll(show_buy_orders_sql)
            close_db(conn)
            response = ""
            print(collections)
            for collection in collections :
                # print(collection)
                response = response + "Buy Order id : "+ str(collection[0]) + ". Collection Name : " + str(collection[4]) +". Price :"+ str(collection[3]) + " SOL\n"
            await ctx.channel.send("Buy Orders\n" + response)
        except :
            await ctx.channel.send("Buy orders fetching failed")


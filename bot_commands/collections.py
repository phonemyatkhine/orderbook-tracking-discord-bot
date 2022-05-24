from discord.ext import commands
from database.connect import load_db
from database.connect import close_db

class Collections(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="new_collection")
    @commands.has_role("Devs")
    async def new_collection(self, ctx, arg):
        conn = load_db()
        split = arg.split("@")
        new_collection_sql = "INSERT INTO COLLECTIONS (NAME, TWITTER_LINK) VALUES (' "+split[0]+" ', ' "+split[1]+"' )"
        try :
            conn.executeSql(new_collection_sql)
            close_db(conn)
            await ctx.channel.send("New collection " +split[0]+" created ")
        except :
            await ctx.channel.send("Collection creation failed")       
    @new_collection.error
    async def new_collection_error(self, ctx, error):
        if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
            await ctx.channel.send("You do not have required permissions to use this command.")
        
    @commands.command()
    async def show_collections(self, ctx):
        conn = load_db()
        show_collection_sql = "SELECT * FROM COLLECTIONS"
        try :
            collections = conn.fetchAll(show_collection_sql)
            close_db(conn)
            response = ""
            print(collections)
            for collection in collections :
                # print(collection)
                response = response + "Collection id : "+ str(collection[0]) + ". Name : " + str(collection[1]) +". Twitter link : https://twitter.com/"+ str(collection[2]) + "\n"
            print(response)
            await ctx.channel.send("Collections\n" + response)
        except :
            await ctx.channel.send("Collection fetched failed")

    @commands.command(name="delete_collection")
    @commands.has_role("Devs")
    async def delete_collection(self, ctx, arg):
        delete_sql = "DELETE FROM COLLECTIONS WHERE COLLECTION_ID = " + str(arg)
        conn = load_db()
        try:
            conn.executeSql(delete_sql)
            close_db(conn)
            await ctx.channel.send("Deleted Collection")
        except:
            await ctx.channel.send("Collection deletion error")
    @delete_collection.error
    async def delete_collection_error(self, ctx, error):
        if isinstance(error, (commands.MissingRole, commands.MissingAnyRole)):
            await ctx.channel.send("You do not have required permissions to use this command.")
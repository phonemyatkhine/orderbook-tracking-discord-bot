import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from bot_commands.export import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

bot.add_cog(Collections(bot))
bot.add_cog(Admin(bot))
bot.add_cog(BuyOrder(bot))
bot.add_cog(SellOrder(bot))


bot.run(TOKEN)
                      


    
                    

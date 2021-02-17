from redbot.core.bot import Red
from .schedule import Schedule

___red_end_user_data_statement__ = "This cog does not persistently store data about users."

def setup(bot: Red):
    cog = Schedule(bot)
    bot.add_cog(cog)
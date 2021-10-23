import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.bot(command_prefix='-', intents =
discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run
("Njk0ODUzMzUzNjQ1MTQ2MjEz.XoRqnQ.e4D85JGZu84fw8geG0sWiw_hQOA")
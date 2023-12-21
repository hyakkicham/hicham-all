import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event 
async def on_ready():
    for guild in bot.guilds:
        for member in guild.members:
            try:
                await member.edit(nick="J'ai Chialler pour elle")
            except:
                pass

bot.run('')
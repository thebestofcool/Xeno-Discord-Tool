import discord
from discord.ext import commands

# Define the bot with a command prefix
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run('YOUR_TOKEN_HERE')

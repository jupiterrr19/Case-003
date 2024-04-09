import discord
from discord.ext import commands
intents = Intents.default()
intents.members = True
client = discord.Client(intents=intents)

TOKEN = 'YOUR_TOKEN_HERE'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello!')

bot.run(TOKEN)

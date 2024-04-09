from main import TOKEN
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user in message.mentions:
        embed = discord.Embed(
            title="You pinged the bot!",
            description="Thanks for reaching out!",
            color=ff0000
        )
        await message.channel.send(embed=embed)

client.run(TOKEN)
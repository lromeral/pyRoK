import discord
import datetime
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


bot = commands.Bot(command_prefix="!", intents=intents)
token='MTE2MjM1NjU2OTkwODk2OTU0Mw.GmJchk.7MtLn2KzaM8so7OE08Gnp5tEpNzSxc8exeJJeM'

@bot.command(name="help2")
async def help (ctx):
    embed = discord.Embed(title="RoK Scanning Bot",timestamp=datetime.datetime.utcnow())
    embed.set_author (name="klyde")
    embed.set_footer (text="Requested by {}".format(ctx.author.name))
    ctx.send(embed)




async def enviar_mensaje_canal (mensaje:str):
    #channel Rok Server
    #channel_id = 1155487109960978452
    #channel pruebas
    channel_id =1162358226575179866
    channel = client.get_channel(channel_id)
    await channel.send(mensaje)

asyncio.run(client.run(token))
enviar_mensaje_canal("test de mensaje")


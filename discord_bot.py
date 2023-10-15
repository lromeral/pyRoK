import discord
import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
token='MTE2MjM1NjU2OTkwODk2OTU0Mw.GmJchk.7MtLn2KzaM8so7OE08Gnp5tEpNzSxc8exeJJeM'

@bot.command(name="test", description="Testing command")
async def test(ctx, arg):
    response ="Hola"
    await ctx.send(arg)

@bot.command(name="help")
async def help (ctx):
    embed = discord.Embed(title="RoK Scanning Bot",timestamp=datetime.datetime.utcnow())
    embed.set_author (name="klyde")
    embed.set_footer (text="Requested by {}".format(ctx.author.name))
    ctx.send(embed)

bot.run(token)
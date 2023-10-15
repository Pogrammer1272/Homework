import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
@bot.command()
async def ecology(ctx):
    await ctx.send(f'first: waterpollution second: earthpollution third: airpollution')
@bot.command()
async def airpollution(ctx):
    await ctx.send(f'you should duy a conditioner')
@bot.command()
async def earthpollution(ctx):
    await ctx.send(f'you should clean earth from litter')
@bot.command()
async def waterpollution(ctx):
    await ctx.send(f'you should clean water from plastik bottles,plastic bags etc ')
@bot.command()
async def help(ctx):
    await ctx.send(f'Il show you all commands, dont forget about command prefix $. 1st hello 2nd ecology 3rd airpollution 4th earthpollution 5th waterpollution 6th add 7th heh ')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("")

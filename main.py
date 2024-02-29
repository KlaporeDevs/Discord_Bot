import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
@bot.command()
async def greet(ctx, member: discord.Member):
    greetings = f'Hi {member.mention}'
    await ctx.send(greetings)
@bot.command()
async def hello(ctx):
    member = ctx.author
    greetings = f"Hello {member.mention}"
    await ctx.send(greetings)
@bot.command()
async def Hello(ctx):
    member = ctx.author
    greeting = f"Hello {member.mention}"
    await ctx.send(greeting)
bot.run('Discord Token')
import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix='.')
block_words = ["dylan", "catz", "minor"]

@client.event
async def on_ready():
    print(f"Successfully logged in as {client.user}")


@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)} ms ping time")


@client.command(aliases=["8ball", "eightball"])
async def Eightball(ctx, *, question):
    responses = ['Signs point to yes.',
                 'Fuck no',
                 'Yes.',
                 'Yes definitely.',
                 'Yes.',
                 'Most likely.',
                 'Very doubtful.',
                 'Without a doubt.',
                 'Most likely.',
                 "Don't count on it.",
                 'No',
                 "Its not looking so good"]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command(aliases=["yon"])
async def yesorno(ctx, *, question):
    responses = ['Yes.',
                 'Fuck no.',
                 'FUCK YEAH.',
                 'Hell no.',
                 'No.']
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


@client.command(aliases=["Hello", "hi", "Hi"])
async def hello(ctx):
    await ctx.send('Hi')


@commands.has_permissions(administrator=True)
@client.command(aliases=['purge'])
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)


@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, Member: discord.Member, *, reason=None):
    await Member.kick(reason=reason)


@commands.has_permissions(kick_members=True)
@client.command()
async def ban(ctx, Member: discord.Member, *, reason=None):
    await Member.ban(reason=reason)


@client.command(aliases=["userinfo"], help="Yummy data.")
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title=f"{user}'s info", description=f"Here's {user}'s info", color=0x00ff00)
    embed.add_field(name="Username:", value=user.name, inline=True)
    embed.add_field(name="ID:", value=user.id, inline=True)
    embed.add_field(name="Status:", value=user.status, inline=True)
    embed.add_field(name="Highest Role:", value=user.top_role, inline=True)
    embed.add_field(name="Joined:", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)



client.run('')

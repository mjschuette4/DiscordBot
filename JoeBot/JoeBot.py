import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('With Anime Tiddies'))
    print('Bot is ready')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def ding(ctx):
    await ctx.send('Dong!')

@client.command()
async def a(ctx):
    await ctx.send('Shut up Alyssa')

@client.command()
async def z(ctx):
    await ctx.send('Shut up Zach')

@client.command()
async def dm2(ctx, member: discord.Member, number, *, content):
    channel = await member.create_dm()
    x = 0 
    y = int(number)
    await ctx.channel.purge(limit=1)
    if y <= 50:
        for x in range(y):
            await channel.send(content)
            x + 1
    else:
        await ctx.send('You sadistic fuck')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(aliases=['peepee'])
async def _peepee(ctx):
    lengths = [
        "MANGINA", "MANGINA", "MANGINA", "MANGINA", "MANGINA", 
        "1.1 in","1.2 in","1.3 in","1.4 in","1.5 in","1.6 in","1.7 in","1.8 in","1.9 in", "2.0 in",
        "2.1 in","2.2 in","2.3 in","2.4 in","2.5 in","2.6 in","2.7 in","2.8 in","2.9 in", "3.0 in",
        "3.1 in","3.2 in","3.3 in","3.4 in","3.5 in","3.6 in","3.7 in","3.8 in","3.9 in", "4.0 in",
        "3.1 in","3.2 in","3.3 in","3.4 in","3.5 in","3.6 in","3.7 in","3.8 in","3.9 in", "4.0 in",
        "3.1 in","3.2 in","3.3 in","3.4 in","3.5 in","3.6 in","3.7 in","3.8 in","3.9 in", "4.0 in",
        "4.1 in","4.2 in","4.3 in","4.4 in","4.5 in","4.6 in","4.7 in","4.8 in","4.9 in", "5.0 in",
        "4.1 in","4.2 in","4.3 in","4.4 in","4.5 in","4.6 in","4.7 in","4.8 in","4.9 in", "5.0 in",
        "4.1 in","4.2 in","4.3 in","4.4 in","4.5 in","4.6 in","4.7 in","4.8 in","4.9 in", "5.0 in",
        "4.1 in","4.2 in","4.3 in","4.4 in","4.5 in","4.6 in","4.7 in","4.8 in","4.9 in", "5.0 in",
        "4.1 in","4.2 in","4.3 in","4.4 in","4.5 in","4.6 in","4.7 in","4.8 in","4.9 in", "5.0 in",
        "5.1 in","5.2 in","5.3 in","5.4 in","5.5 in","5.6 in","5.7 in","5.8 in","5.9 in", "6.0 in",
        "5.1 in","5.2 in","5.3 in","5.4 in","5.5 in","5.6 in","5.7 in","5.8 in","5.9 in", "6.0 in",
        "5.1 in","5.2 in","5.3 in","5.4 in","5.5 in","5.6 in","5.7 in","5.8 in","5.9 in", "6.0 in",
        "5.1 in","5.2 in","5.3 in","5.4 in","5.5 in","5.6 in","5.7 in","5.8 in","5.9 in", "6.0 in",
        "5.1 in","5.2 in","5.3 in","5.4 in","5.5 in","5.6 in","5.7 in","5.8 in","5.9 in", "6.0 in",
        "5.1 in","5.2 in","5.3 in","5.4 in","5.5 in","5.6 in","5.7 in","5.8 in","5.9 in", "6.0 in",
        "5.1 in","5.2 in","5.3 in","5.4 in","5.5 in","5.6 in","5.7 in","5.8 in","5.9 in", "6.0 in",
        "5.1 in","5.2 in","5.3 in","5.4 in","5.5 in","5.6 in","5.7 in","5.8 in","5.9 in", "6.0 in",
        "6.1 in","6.2 in","6.3 in","6.4 in","6.5 in","6.6 in","6.7 in","6.8 in","6.9 in", "7.0 in",
        "7.1 in","7.2 in","7.3 in","7.4 in","7.5 in","7.6 in","7.7 in","7.8 in","7.9 in", "8.0 in",
        "8.1 in","8.2 in","8.3 in","8.4 in","8.5 in","8.6 in","8.7 in","8.8 in","8.9 in", "9.0 in",
        "9.1 in","9.2 in","9.3 in","9.4 in","9.5 in","9.6 in","9.7 in","9.8 in","9.9 in", "10.0 in",
        "10.1 in","10.2 in","10.3 in","10.4 in","10.5 in","10.6 in","10.7 in","10.8 in","10.9 in", "11.0 in",
        "11.1 in","11.2 in","11.3 in","11.4 in","11.5 in","11.6 in","11.7 in","11.8 in","11.9 in", "12.0 in",
        "12.1 in","12.2 in","12.3 in","12.4 in","12.5 in","12.6 in","12.7 in","12.8 in","12.9 in", "13.0 in",
        "MONSTER COCK", "MONSTER COCK", "MONSTER COCK"]
    size = random.choice(lengths)   
    print(size) 
    await ctx.send(f' 🍆 : {size}')
    

@client.command()
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount+1)

client.run('Nzc4NDYyMTE0MzE3ODYwOTE2.X7SVVw.-_VBOj_LRKWLpj3hVmiaEgouN8I')

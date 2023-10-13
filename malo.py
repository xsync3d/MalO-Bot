import requests
import json

import discord
from discord.ext import commands

DISCORD_API_TOKEN = ''
MALCORE_API_HEADERS = {"apiKey": ""} 
MALCORE_API = "https://api.malcore.io/api/"

TXT_FILE = "tempout.json"

def pop_out_file(data):
    with open(TXT_FILE, 'w') as f:
        f.write(data)

def post(headers=MALCORE_API_HEADERS, data=None, files=None, endpoint=None): 
    r = requests.post(MALCORE_API + endpoint, data=data, headers=headers, files=files)
    return json.dumps(r.json(), indent=4)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!!', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(pass_context=True)
async def sce(ctx, arg):
    await ctx.send(f"Emulating...")
    pop_out_file(post(data={"shellcode": arg}, endpoint="shellcode"))
    await ctx.send(f"Here's your shellcode ({arg}) emulation!")
    await ctx.send(file=discord.File(TXT_FILE, TXT_FILE))

@bot.command()
async def urlchk(ctx, arg):
    await ctx.send(f"Checking sussy url...")
    data=post(data={"url": arg}, endpoint="urlcheck")
    await ctx.send(f"```json\n{data}```")

bot.run(DISCORD_API_TOKEN)

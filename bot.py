import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import asyncio
import json

def get_server_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefix = json.load(f)
        
    return prefix[str(message.guild.id)]    

client = commands.Bot(command_prefix=get_server_prefix, intents=discord.Intents.all())

bot_status = cycle(["Minecraft com meus amigos! :)", "redelunar.com :D", "com 1400 jogadores.", "sem parar no Lunar"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print("Bot is running...")
    change_status.start()
    
@client.event
async def on_guild_join(guild):
    with open("./prefix.json", "r") as f:
        prefix = json.load(f)
        
    prefix[str(guild.id)] = "!"   
    
    with open("./prefix.json", "w") as f:
        json.dump(prefix, f, indent=4)
        
@client.event
async def on_guild_remove(guild):
    with open("./prefix.json", "r") as f:
        prefix = json.load(f)
        
    prefix.pop[str(guild.id)] 
    
    with open("prefix.json", "w") as f:
        json.dump(prefix, f, indent=4)               
  
async def load():
    for filename in os.listdir("./cogs"):    
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:    
        await load()
        await client.start("Ur bot token here")  
                         
asyncio.run(main())            

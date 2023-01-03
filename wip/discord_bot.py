# THIS file is a WIP it doesn't work yet !!!

import os, discord

TOKEN = os.getenv('DISCORD_TOKEN')
# intents = discord.Intents.default()
# # intents.message_content = True
# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#    await client.get_channel("1059602942061199533").send("bot is online")

# client.run(TOKEN)

from discord.ext import commands
client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
    print(f"Log : {client.user}")
    ch = await client.fetch_channel("1059602942061199533")
    await ch.send(content="Hello world")


client.run(TOKEN)

import discord
from discord.ext import commands
import os
import requests


client = commands.Bot(command_prefix = '!')


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!summon enter friends name here'):
    await message.channel.send("https://tenor.com/view/kakashi-hatake-summoning-jutsu-naruto-gif-12217932")
    for i in range(3):
      await message.channel.send("<@enter Discord id here>")



client.run(os.getenv('TOKEN'))

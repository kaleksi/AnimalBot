import discord
import requests
from stayinalive import stayinalive

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith("!fox"):
    response = requests.get("https://randomfox.ca/floof")
    fox = response.json()
    await message.channel.send(fox['image'])
    return

  if message.content.startswith("!cat"):
    response = requests.get("http://aws.random.cat/meow")
    cat = response.json()
    await message.channel.send(cat["file"])
    return

  if message.content.startswith("!dog" or "!doggo"):
    response = requests.get("https://random.dog/woof.json")
    dog = response.json()
    await message.channel.send(dog["url"])
    return

  if message.content.startswith("!jeff"):
    await message.channel.send("if Jeff Benzos put all his money up his ass he would need a really big as s")
    return

stayinalive()
client.run("ODY5NDY1ODYzMjM1OTY5MDg0.YP-nLw.Z9oY8AGL775k-DCgRTad956IAxg")

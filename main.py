#Created 7/27/2021 "727 day!"
#Last modified 7/28/2021

#This bot is intended for use in a personal discord server with my friends
#As such, it is a complete mess of stupid features and horrible code :^)

import discord
import requests
from stayinalive import stayinalive

client = discord.Client()

#log in
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

  if message.content.startswith("!smug"):
    response = requests.get("https://api.waifu.pics/sfw/smug")
    smug = response.json()
    await message.channel.send(smug["url"])
    return

  if message.content.startswith("!bonk"):
    response = requests.get("https://api.waifu.pics/sfw/bonk")
    smug = response.json()
    await message.channel.send(smug["url"])
    return

  if message.content.startswith("!cringe"):
    response = requests.get("https://api.waifu.pics/sfw/cringe")
    smug = response.json()
    await message.channel.send(smug["url"])
    return

  if message.content.startswith("!bully"):
    response = requests.get("https://api.waifu.pics/sfw/bully")
    smug = response.json()
    await message.channel.send(smug["url"])
    return


  #LISTS BOT COMMANDS
  if message.content.startswith("!animalbot"):
    await message.channel.send("Currently available commands are: !fox, !cat, !dog, !jeff, !smug, !bonk, !cringe, !bully, !animalbot")
    return

stayinalive()

#Shouldn't put this here but env wasn't working YOLO
client.run("ODY5NDY1ODYzMjM1OTY5MDg0.YP-nLw.uEKqrhXEBkOjGzrw7gKy37bwkTU")


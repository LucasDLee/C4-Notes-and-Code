import discord  # Discord has a specific set of Python that lets you work with its Discord bots
import os  # os = operating system

# First, we need to connect to Discord's platform
intents = discord.Intents.default()
# intents.message_content = True

client = discord.Client(intents=intents)


@client.event
# A client.event is any task someone does on Discord
async def on_ready():
	print("Bot has logged in")


@client.event
async def on_message(message):
	# if message.content.startswith('$hello'):
	# 	await message.channel.send('Hello!')
	if message.author == client.user:
		await message.channel.send('Hello!')
	else:
		await message.channel.send("default")				

client.run('MTAyMjI3MjU0NTUwMTc1NzU1MA.GLf3qG.ZzCeBiYGbqBf9HJrtH9AdxT03WQu-NvON2hiOY')

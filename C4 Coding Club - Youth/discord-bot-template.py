import discord  # Discord has a specific set of Python that lets you work with its Discord bots
# import os  # os = operating system

# First, we need to connect to Discord's platform
intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
# A client.event is any task someone does on Discord
async def on_ready():
	print("Bot has logged in")

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('Hello'):
		await message.channel.send('Hello!')
		return

client.run('MTAyMjI3MjU0NTUwMTc1NzU1MA.GccI8z.crhPd3pVpMa0cavlOKfvWCiKn4BetkUtjx74SI')
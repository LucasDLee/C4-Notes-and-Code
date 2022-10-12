import discord  # Discord has a specific set of Python that lets you work with its Discord bots

# Refer to https://discordpy.readthedocs.io/en/latest/api.html for all of the Discord code we will be working with

# Step 1: Connect to Discord's platform/service #
intents = discord.Intents.default() # Discord Intents are like privileges we give to our bot

client = discord.Client(intents=intents)

# Step 2: Enable our bot to do stuff #

@client.event
# A client.event is any task our bot does on Discord
# Can also be @discord.Client(intents=intents).event
async def on_ready():
	# on_ready() is used when our code successfully connects to our bot
	print("Bot has logged in")


# Step 3: Sending messages #
@client.event
async def on_message(message):
	# on_message() is a built in Discord function for our bot to manage messages

	# If we send nothing, the bot stops this message function
	if message.author == client.user:
		return

	# For example, if we send 'Hello', our bot will respond with 'Hello!'
	if message.content.startswith('Hello'):
		await message.channel.send('Hello!')
		return # Use return to stop our code

	# Step 4: Sending pictures #
	# From a website known as Picsum.photos (https://picsum.photos/), we can get random images of certain sizes
	# However, if we do the same thing as we did for our 'Hello' message, we get the same picture over and over
	if message.content.startswith('Image'):
		seedNumber = random.randint(0,1000)
		await message.channel.send('https://picsum.photos/seed/' + str(seedNumber) + '/200/300')
		return


client.run('MTAyMjI3MjU0NTUwMTc1NzU1MA.Gcm19w.YG8mX1Wkif6jGjCXRNrnViEyjHWvrJ6MQdwOH0')
# This is where we will connect our bot to our Python code
# Our "security token" is a specific set of numbers, letters, and symbols. 
# Anyone with our security token can implement changes to our bot so its best to keep it hidden
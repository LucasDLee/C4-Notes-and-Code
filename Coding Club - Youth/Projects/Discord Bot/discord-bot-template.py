# Refer to https://discordpy.readthedocs.io/en/latest/api.html for all of the Discord code we will be working with

import discord  # Discord has a specific set of Python that lets you work with its Discord bots
import random
from datetime import datetime
import math

# Step 1: Connect to Discord's platform/service #
myIntents = discord.Intents.default() # Discord Intents are like privileges we give to our bot

client = discord.Client(intents=myIntents)
# A discord.Client asks for access to Discord

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
	# on_message() is a built in Discord function for our bot to manage direct messages

	# If we send nothing, the bot stops this message function
	if message.author == client.user:
		return

	# For example, if we send '!hello', our bot will respond with 'Hello!'
	if message.content.startswith('!hello'):
		await message.channel.send('Hello!')
		return # Use return to stop our code

	if message.content.startswith('!goodbye'):
		await message.channel.send('Goodbye')
		return

	if message.content.startswith('!time'):
		currentTime = datetime.now()
		await message.channel.send(currentTime)
		return

	# Step 4: Sending pictures #
	# From a website known as Picsum.photos (https://picsum.photos/), we can get random images of certain sizes
	# However, if we do the same thing as we did for our 'Hello' message, we get the same picture over and over
	if message.content.startswith('.image'):
		seedNumber = random.randint(0,1000)
		await message.channel.send('https://picsum.photos/seed/' + str(seedNumber) + '/200/300')
		return

	# Step 5: Adding Reactions
	if message.content.startswith('!heart'):
		emoji = '\U0001f49d' # The emoji's value is attached to the "Unicode number" which is a way to format all emojis and characters from the internet
		await message.add_reaction(emoji)
		return

	# Step 6: Doing Calculations
	if message.content.startswith('!calculate'):
		calculation = message.content.split(" ")
		result = -1
		calculation[2] = int(calculation[2])
		calculation[3] = int(calculation[3])
		# Currently, calculation[] at positions 2 and 3 are strings (words) so we need to change them into numbers
		
		if(calculation[1].lower() == 'pythagorean'):
			result = pythagorean(calculation[2], calculation[3])
		elif(calculation[1].lower() == 'add'):
			result = add(calculation[2], calculation[3])
			
		await message.channel.send(result)

def pythagorean(x, y):
	return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

### ACTIVITY: ###

# 1) Make a function called "add(x, y)". This function will return the sum of x + y
# 2) In step 6, make an elif (else-if) statement that checks if you type !calculate add x y and sees if "add" is at position 1 of the array. If so, then set result to equal your sum
# 3) Test it out in Discord!

def add(x, y):
	return x + y

# Step 7: Greeting New Members in a Discord Server
@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send("Hello " + member.name + ". Welcome to my Discord server!")
	return

client.run('MTAyMjI3MjU0NTUwMTc1NzU1MA.GQGrjy.pzdnj7xmmImzWNZLsLwrH0tZh-RwF1dHMlFHhk')
# This is where we will connect our bot to our Python code
# Our "security token" is a specific set of numbers, letters, and symbols. 
# Anyone with our security token can implement changes to our bot so its best to keep it hidden
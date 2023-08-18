# Refer to https://discordpy.readthedocs.io/en/latest/api.html for all of the Discord code we will be working with

import discord  # Discord has a specific set of Python that lets you work with its Discord bots
import random
from datetime import datetime
import math

# Step 1: Connect to Discord's platform/service #
myIntents = discord.Intents.default() # Discord Intents are like privileges we give to our bot
myIntents.members = True

client = discord.Client(intents=myIntents)
# A discord.Client asks for access to Discord

# Step 2: Enable our bot to do stuff #

@client.event
# A client.event is any task our bot does on Discord
# Can also be @discord.Client(intents=intents).event
async def on_ready():
	# on_ready() is used when our code successfully connects to our bot
	print("Bot has logged in")

# STEP 3 FUNCTIONS #
def pythagorean(x, y):
	return math.sqrt(math.pow(x, 2) + math.pow(y, 2))

### ACTIVITY: ###

# 1) Make a function called "add(x, y)". This function will return the sum of x + y
# 2) Go back to step 6. In step 6, make an elif (else-if) statement that checks if you type `!calculate add x y`` to see the sum of your numbers. For example, `!calculate add 6 7` will give you 13.
# 3) Test it out on Discord!

def add(x, y):
	return x + y

# END OF STEP 3 FUNCTIONS

# Step 3: Sending messages #
@client.event
async def on_message(message):
	# on_message() is a built in Discord function for our bot to manage direct messages

	# If we send nothing, the bot stops this message function
	if message.author == client.user:
		return
	
	# For example, if we send '!hello', our bot will respond with 'Hello!'
	if '!hello' in message.content.lower():
		await message.channel.send('Hello!')
	elif '!goodbye' in message.content.lower():
		await message.channel.send('Goodbye')
	elif '!date' in message.content.lower():
		currentTime = datetime.now()
		await message.channel.send(currentTime)
	
	# Step 4: Adding Reactions
	elif '!heart' in message.content.lower():
		emoji = '\U0001f49d' # The emoji's value is attached to the "Unicode number" which is a way to format all emojis and characters from the internet
		await message.add_reaction(emoji)
		return

	# Step 5: Doing Calculations
	elif '!calculate' in message.content.lower():
		calculation = message.content.split(" ")

		if message.content.startswith("<@%s>" % client.user.id):	
			calculation = calculation[1:] # Removes the @bot part in a Discord server's channel's message
		
		result = -1
		calculation[2] = int(calculation[2])
		calculation[3] = int(calculation[3])
		# Currently, calculation[] at positions 2 and 3 are strings (words) so we need to change them into numbers
		
		if(calculation[1].lower() == 'pythagorean'):
			result = pythagorean(calculation[2], calculation[3])
		elif(calculation[1].lower() == 'add'):
			result = add(calculation[2], calculation[3])
			
		await message.channel.send(result)

	### ACTIVITY ###
	
	# You will be making another command for your Discord bot.
	# This command will be called "!count-vowels" and will count all of the vowels (a,e,i,o,u) in a sentence
	
	# Some notes:
	# 	1) Inside of your if (or else-if) statement with your command, use `sentence = message.content.split(maxsplit=1)[1]` to ignore !count-vowels when counting the total number of vowels
	# 	2) Make a variable called `vowel_count` set to 0
	# 	3) Use a loop (for- or while-loop, it doesn't matter) to go through each letter in the variable called `sentence`
	# 		3.1) Inside of your loop, you can use variable.lower() to get the lowercase version of whatever letter you want
	# 		3.2) If you find a vowel, increase vowel_count by 1
	# 	4) Don't worry about using the commmand in your Discord server. Just make sure it works in your direct messages
	
	elif '!count-vowels' in message.content.lower():
		sentence = message.content.split(maxsplit=1)[1]  # Get the sentence after the command
		vowels = "aeiou"
		vowel_count = 0
		for x in sentence:
			if x.lower() in vowels:
				vowel_count += 1
			
		final_message = f"There are {vowel_count} vowels in the sentence *{sentence}*"
		await message.channel.send(final_message)

# Step 6: Greeting New Members in a Discord Server
@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f"Hello {member.name}. Welcome to my Discord server!")
	return

# Step 7: Responding in your Discord server
@client.event
async def set_response_channel(ctx):
    channel_id = ctx.channel.id
    await ctx.send(f"Response channel set to {ctx.channel.mention} (ID: {channel_id}).")


client.run('')
# This is where we will connect our bot to our Python code
# Our "security token" is a specific set of numbers, letters, and symbols (FOUND IN THE "Bot" SECTION)
# Anyone with our security token can implement changes to our bot so it's best to keep it hidden
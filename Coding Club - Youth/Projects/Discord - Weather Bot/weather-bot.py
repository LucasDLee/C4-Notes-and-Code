# Finding Latitude and Longitude: https://www.findlatitudeandlongitude.com/
# Weather API from Canada's Meteorological Center: https://open-meteo.com/en/docs/gem-api

import discord
import requests

weather_data = ""

# Functions you will use in your activity #

# DO NOT EDIT ANY OF THE FUNCTIONS HERE

# get_coordinates(): Gets the coordinates from your Discord user and saves temporarily saves it into the bot
# Returns nothing
def get_coordinates(lat, lon):
	global weather_data
	API_URL = "https://api.open-meteo.com/v1/gem?latitude=" + str(lat) + "&longitude=" + str(lon) + "&daily=weathercode,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,precipitation_sum,rain_sum,showers_sum,snowfall_sum,precipitation_hours,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant,shortwave_radiation_sum,et0_fao_evapotranspiration&timezone=GMT"
	weather_data = requests.get(API_URL).json()

# get_sunrise_and_sunset(): Uses the data from weather_data that was found using get_coordinates(), and finds the sunrise and sunset times for a certain location in GMT time
# Returns a formatted Discord message
def get_sunrise_and_sunset():
	sunrise = weather_data["daily"]["sunrise"]
	sunset = weather_data["daily"]["sunset"]
	combined_data = zip(sunrise, sunset) # Combines the lists together

	# Iterate through the combined data and process each date and time
	formatted_message = ""
	for sunrise_time, sunset_time in combined_data:
		sunrise_date, sunrise_time = sunrise_time.split("T")
		_, sunset_time = sunset_time.split("T")

		formatted_message += f"Date: {sunrise_date}\n"
		formatted_message += f"Sunrise Time: {sunrise_time}\n"
		formatted_message += f"Sunset Time: {sunset_time}\n"
		formatted_message += "-" * 25 + "\n"

	return formatted_message

# get_temp(): Uses the data from weather_data, and gets the minimmum and maximum temperature for each day
# Returns a formatted Discord message
def get_temp():
	# TODO: Complete step 4 in this function

	time = weather_data["daily"]["time"]
	temperature_2m_max = weather_data["daily"]["temperature_2m_max"]
	temperature_2m_min = weather_data["daily"]["temperature_2m_min"]

	combined_data = zip(time, temperature_2m_max, temperature_2m_min)
	formatted_message = ""
	for row in combined_data:
		date, max_temp, min_temp = row
		formatted_message += f"Date: {date}\nMax Temperature: {max_temp}°C\nMin Temperature: {min_temp}°C\n"
		formatted_message += "-" * 20 + "\n"

	return formatted_message

# Discord Bot #
myIntents = discord.Intents.default()
client = discord.Client(intents=myIntents)

@client.event
async def on_ready():
	print("Bot has logged in")

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	
  # TODO: Complete the activity in this function

	# Step 2: Get weather coordinates #
	if '!weather' in message.content.lower():
		get_coords = message.content.split(" ")
		
		if message.content.startswith("<@%s>" % client.user.id):	
			get_coords = get_coords[1:] # Removes the @bot part in a Discord server's channel's message

		get_coordinates(get_coords[1], get_coords[2])
		msg = f"Your coordinates were {get_coords[1]} for latitude and {get_coords[2]} for longitude."
		await message.channel.send(msg)
	
	# Step 3: Get sunrise and sunset data #
	if '!sun' in message.content.lower():
		if weather_data == "":
			await message.channel.send("Sorry, you need to set a location first.")
		else:
			await message.channel.send(get_sunrise_and_sunset())

	# Step 4: Get min and max temperature #
	if '!temperature' in message.content.lower():
		if weather_data == "":
			await message.channel.send("Sorry, you need to set a location first.")
		else:
			await message.channel.send(get_temp())
	

client.run('')
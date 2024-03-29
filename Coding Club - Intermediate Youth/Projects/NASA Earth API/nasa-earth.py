# Finding Latitude and Longitude: https://www.findlatitudeandlongitude.com/
# NASA APIs: https://api.nasa.gov/

# Step 1
import tkinter as tk
from PIL import Image, ImageTk
import io
import requests
import re

def run_nasa_earth_api():
    # Step 2
    print("Welcome to NASA's Earth API.\n \nThis API gets you an image based on your provided latitude and longitude.\n")
    lat = float(input("What latitude do you want to look at? "))
    while(lat > 90 or lat < -90):
        print("Sorry, your latitude is not accepted.")
        lat = float(input("What latitude do you want to look at? "))

    lon = float(input("What longitude do you want to look at? "))
    while(lon > 180 or lon < -180):
        print("Sorry, your longitude is not accepted.")
        lon = float(input("What longitude do you want to look at? "))
    
    print("\nYour latitude was " + str(lat) + " and your longitude was " + str(lon) + ". Now, we need the dimension of the width and height your image in degrees.\n")
    dim = float(input("What is your image's dimension? "))

    # Step 3
    print("\nNow, we need a date for your image. Please provide in YYYY-MM-DD format.\n")
    user_date = str(input("What is the date for your image? "))
    check_date = valid_date(user_date)
    while(not check_date):
        print("Your date was not valid")
        user_date = str(input("What is the date for your image? "))
        check_date = valid_date(user_date)
        
    print("\nYour date was " + user_date)

    # Step 4
    print("\nFinally, we need an API key.\n")
    api_key = str(input("What is your API key? "))
    url = "https://api.nasa.gov/planetary/earth/imagery?lon=" + str(lon) + "&lat=" + str(lat) + "&date=" + user_date + "&dim=" + str(dim) + "&api_key=" + api_key

    # Step 5
    window = tk.Tk()
    window.geometry("500x450")  # set your GUI size (width x height)

    # Download the image to your workplace
    response = requests.get(url)
    img_data = response.content

    # Open your image from the data
    load_img = Image.open(io.BytesIO(img_data))

    # Add your uploaded image to Tkinter
    resize_image = load_img.resize((500, 450))
    gui_image = ImageTk.PhotoImage(resize_image)

    # Create a label with the image to put it into your GUI
    add_image = tk.Label(window, image=gui_image)
    add_image.pack()

    window.mainloop()  # display everything in your GUI

# You may use this function to check if the date a user inputted matches our format or not
def valid_date(date):
    is_valid = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(is_valid.match(date))

run_nasa_earth_api()
# Finding Latitude and Longitude: https://www.findlatitudeandlongitude.com/
# NASA APIs: https://api.nasa.gov/

# Step 1
import re
from matplotlib import pyplot
from skimage import io

def run_nasa_earth_api():
    # Step 2
    print("Welcome to NASA's Earth API.\n \nThis API gets you an image based on your provided latitude and longitude.\n")
    lat = float(input("What latitude do you want to look at? "))
    lon = float(input("What longitude do you want to look at? "))
    print("\nYour latitude was " + str(lat) + " and your longitude was " + str(lon) + ". Now, we need the dimension of the width and height your image in degrees.\n")
    dim = float(input("What is your image's dimension? "))
    print("\nNow, we need a date for your image. Please provide in YYYY-MM-DD format.\n")

    # Step 3
    user_date = str(input("What is the date for your image? "))
    check_date = valid_date(user_date)
    while(not check_date):
        print("Your date was not valid")
        user_date = str(input("What is the date for your image? "))
        check_date = valid_date(user_date)
        print(check_date)
    print("\nYour date was " + user_date)

    # Step 4
    print("\nFinally, we need an API key.\n")
    api_key = str(input("What is your API key? "))
    url = "https://api.nasa.gov/planetary/earth/imagery?lon=" + str(lon) + "&lat=" + str(lat) + "&date=" + user_date + "&dim=" + str(dim) + "&api_key=" + api_key

    # Step 5
    url_img = io.imread(url) # loads the image from the URL
    pyplot.imshow(url_img) # prepares the image
    pyplot.axis("off")
    pyplot.show() # display image in output

# You may use this function to check if the date a user inputted matches our format or not
def valid_date(date):
    is_valid = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(is_valid.match(date))

run_nasa_earth_api()
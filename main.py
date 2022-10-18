import requests

API_KEY = "599ce62bd1b34caebe1c75a328d04b4e"

# This function is to get latitude and longitude data for the location that you want to get the forecast for.
# It starts by asking the user if they are looking for a location in the US or not based off of a yes or no question
# converts the user response into a boolean, asks for the city they are looking for, then checks to see if the location
# in question is in the US or not. If it is, then we ask for the state information and send an HTTP request to
# the open weather api including city, state, and the US country code.
# If the location is not in the US, then we ask for the country code and then make a call to the open weather api including
# the city and country code. If any of the user inputs are invalid, return a False boolean to error out of the script
# Once either of the requests is made to the API, we parse out the JSON information and create a new dictionary to return
# and pass to the next function


def get_lat_and_lon():
    print()
    print("What location are you looking to get the weather for?")
    print()
    print("In the US? (y or n)")
    inUsInputResponse = input()

    inUs = None

    if inUsInputResponse == "y":
        inUs = True
    elif inUsInputResponse == "n":
        inUs = False
    else:
        return False

    print()
    print("City Name?")
    city = input()

    stateCode = None
    countryCode = None

    if inUs == True:
        print()
        print("State Code? (ND)")
        stateCode = input()

        if len(stateCode) != 2:
            return False
        else:
            countryCode = "US"

            response = requests.get(
                f"http://api.openweathermap.org/geo/1.0/direct?q={city},{stateCode},{countryCode}&limit={1}&appid={API_KEY}"
            )

            location_dict = response.json()[0]

            lat_lon_dict = {
                "lat": location_dict.get("lat"),
                "lon": location_dict.get("lon"),
                "city": city,
            }
    else:
        print()
        print("Country Code? (FR)")
        countryCode = input()

        if len(countryCode) != 2:
            return False
        else:
            response = requests.get(
                f"http://api.openweathermap.org/geo/1.0/direct?q={city},{countryCode}&limit={1}&appid={API_KEY}"
            )
            location_dict = response.json()[0]

            lat_lon_dict = {
                "lat": location_dict.get("lat"),
                "lon": location_dict.get("lon"),
                "city": city,
            }

    return lat_lon_dict


# This function will take the the lat and lon dict created in the get_lat_lon_data function and send it to the open weather API
# to get the current forecast data for the requested location. When the data returns, create a new dict and fill the responses
# with the parsed JSON from the API response, and return the new dict


def get_current_weather_data(lat_lon_dict):
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?lat={lat_lon_dict.get("lat")}&lon={lat_lon_dict.get("lon")}&units=imperial&appid={API_KEY}'
    ).json()

    current_weather_data = {
        "temp": response.get("main").get("temp"),
        "feels_like": response.get("main").get("feels_like"),
        "temp_min": response.get("main").get("temp_min"),
        "temp_max": response.get("main").get("temp_max"),
        "humidity": response.get("main").get("humidity"),
        "wind_speed": response.get("wind").get("speed"),
        "desc": response.get("weather")[0].get("description"),
        "city": lat_lon_dict.get("city"),
    }

    return current_weather_data


# This function will take a passed in dict full of weather data and print output to the console


def print_forecast(current_weather_data):
    print()
    print(
        "In "
        + current_weather_data.get("city")
        + ", it is: "
        + current_weather_data.get("desc")
    )
    print()
    print("The current forecast for " + current_weather_data.get("city") + " is:")
    print()
    print("Temperature: " + str(current_weather_data.get("temp")) + " degrees")
    print(
        "Minimum Temperature: " + str(current_weather_data.get("temp_min")) + " degrees"
    )
    print(
        "Maximum Temperature: " + str(current_weather_data.get("temp_max")) + " degrees"
    )
    print("Feels Like: " + str(current_weather_data.get("feels_like")) + " degrees")
    print("Humidity: " + str(current_weather_data.get("humidity")) + "%")
    print("Wind Speed: " + str(current_weather_data.get("wind_speed")) + " MPH")
    print()


# This is our main function, it calls all of the other functions in our script


def main():
    lat_and_lon = get_lat_and_lon()
    if lat_and_lon == False:
        print()
        print("Invalid data, please try again")
        print()
    else:
        current_weather_data = get_current_weather_data(lat_and_lon)
        print_forecast(current_weather_data)


main()

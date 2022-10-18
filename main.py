import requests

API_KEY = "599ce62bd1b34caebe1c75a328d04b4e"


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


def main():
    lat_and_lon = get_lat_and_lon()
    current_weather_data = get_current_weather_data(lat_and_lon)
    print_forecast(current_weather_data)


main()

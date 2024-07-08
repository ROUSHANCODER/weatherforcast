import requests
# we use requests module
def get_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city}&aqi=no"
    
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Will raise an error 
        data = response.json()
        # website use in this weather forcast  is https://www.weatherapi.com
        location = data["location"]
        current = data["current"]
        weather_info = {
            "Location": location["name"],
            "Region": location["region"],
            "Country": location["country"],
            "Temperature (C)": current["temp_c"],
            "Condition": current["condition"]["text"],
            "Humidity": current["humidity"],
            "Wind (kph)": current["wind_kph"]
        }
        
        return weather_info
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")

if __name__ == "__main__":
    api_key = "your api key after sign in website"  # Replace with your WeatherAPI key
    city = input("Enter city name: ")
    weather_info = get_weather(city, api_key)
    
    if weather_info:
        print(f"Weather in {weather_info['Location']}, {weather_info['Region']}, {weather_info['Country']}:")
        print(f"Temperature: {weather_info['Temperature (C)']}°C")
        print(f"Condition: {weather_info['Condition']}")
        print(f"Humidity: {weather_info['Humidity']}%")
        print(f"Wind: {weather_info['Wind (kph)']} kph")
    else:
        print(f"City {city} not found.")


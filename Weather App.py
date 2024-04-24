import requests
import json

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def get_forecast(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def print_weather(weather):
    if 'name' in weather:
        print(f"Current weather in {weather['name']}:")
        print(f"{weather['weather'][0]['description']}")
        print(f"Temperature: {weather['main']['temp']}°C")
    else:
        print("Could not get weather data.")


def print_forecast(forecast):
    print(f"\nForecast for the next few days in {forecast['city']['name']}:")
    for entry in forecast['list']:
        print(f"{entry['dt_txt']}: {entry['weather'][0]['description']}, Temperature: {entry['main']['temp']}°C")

def main():
    city = 'London'  # replace with your city
    api_key = '49f6205cd65942ec2585b4f598667c6d'  # your OpenWeatherMap API key
    weather = get_weather(city, api_key)
    forecast = get_forecast(city, api_key)
    print_weather(weather)
    print_forecast(forecast)

if __name__ == "__main__":
    main()
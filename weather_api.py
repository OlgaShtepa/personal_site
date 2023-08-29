import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Replace 'YOUR_API_KEY' with your actual API key from the weather API provider
API_KEY = os.getenv('WEATHER_API_KEY')
API_URL = 'https://api.weatherapi.com/v1/'

def get_weather_data(city):
    if not API_KEY:
        raise ValueError("Weather API key not found. Make sure to set the WEATHER_API_KEY environment variable.")

    params = {'key': API_KEY, 'q': city}
    response = requests.get(API_URL + 'current.json', params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None
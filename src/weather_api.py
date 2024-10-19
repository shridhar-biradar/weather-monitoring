# src/weather_api.py

import requests
import config_loader  # Updated import

def fetch_weather_data(city):
    config = config_loader.load_config()  # Load configuration
    API_KEY = config['api_key']  # Fetch API key from config
    
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Get temperature in Celsius
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {city}: {response.status_code}")
        return None

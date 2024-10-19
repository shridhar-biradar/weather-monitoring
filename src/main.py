# src/main.py

import time
from weather_api import fetch_weather_data
from data_processing import process_weather_data, calculate_daily_aggregates
from alert_system import check_alerts
import config_loader  # Updated import

def run_weather_monitoring():
    config = config_loader.load_config()  # Load config using config_loader
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
    interval = 300  # 5 minutes in seconds

    while True:
        for city in cities:
            weather_data = fetch_weather_data(city)
            if weather_data:
                # Process and store weather data
                process_weather_data(weather_data, city)
                # Check for alerts
                check_alerts(weather_data, city)

                # Calculate and print daily aggregates (you can adjust how you want to display this)
                date = time.strftime('%Y-%m-%d')  # Get current date
                aggregates = calculate_daily_aggregates(city, date)
                print(f"Daily aggregates for {city} on {date}: {aggregates}")
        
        time.sleep(interval)

if __name__ == "__main__":
    run_weather_monitoring()

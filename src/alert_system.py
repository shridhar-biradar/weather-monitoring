# src/alert_system.py

import config_loader  # Updated import

def check_alerts(weather_data, city):
    config = config_loader.load_config()  # Load configuration
    temp = weather_data['main']['temp']
    
    # Access threshold values from config
    thresholds = config['thresholds']

    if temp > thresholds['temperature']:
        trigger_alert(city, temp)

def trigger_alert(city, temp):
    # This will print the alert message to the console
    print(f"Alert! Temperature in {city} is {temp}°C")







# src/data_processing.py

import sqlite3
from datetime import datetime

def process_weather_data(weather_data, city):
    conn = sqlite3.connect('data/weather_data.db')
    cursor = conn.cursor()

    temp = weather_data['main']['temp']
    weather_condition = weather_data['weather'][0]['main']
    timestamp = weather_data['dt']
    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')

    cursor.execute("""
        INSERT INTO weather_summary (city, date, temp, weather_condition)
        VALUES (?, ?, ?, ?)
    """, (city, date, temp, weather_condition))

    conn.commit()
    conn.close()

def calculate_daily_aggregates(city, date):
    conn = sqlite3.connect('data/weather_data.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(temp), MAX(temp), MIN(temp), weather_condition
        FROM weather_summary
        WHERE city = ? AND date = ?
    """, (city, date))

    aggregates = cursor.fetchone()
    conn.close()

    # Determine dominant weather condition (this logic can be expanded as needed)
    if aggregates:
        avg_temp, max_temp, min_temp, dominant_condition = aggregates
        return {
            'avg_temp': avg_temp,
            'max_temp': max_temp,
            'min_temp': min_temp,
            'dominant_condition': dominant_condition
        }
    return None

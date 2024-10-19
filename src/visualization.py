# src/visualization.py

import matplotlib.pyplot as plt
import sqlite3

def plot_daily_weather(city):
    conn = sqlite3.connect('data/weather_data.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT date, AVG(temp), MAX(temp), MIN(temp)
        FROM weather_summary
        WHERE city = ?
        GROUP BY date
    """, (city,))

    results = cursor.fetchall()
    conn.close()

    dates = [result[0] for result in results]
    avg_temps = [result[1] for result in results]
    max_temps = [result[2] for result in results]
    min_temps = [result[3] for result in results]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label='Avg Temp', marker='o')
    plt.plot(dates, max_temps, label='Max Temp', marker='o')
    plt.plot(dates, min_temps, label='Min Temp', marker='o')
    plt.title(f'Daily Weather Summary for {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

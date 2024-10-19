# tests/test_weather.py

import unittest
from src.weather_api import fetch_weather_data
from src.data_processing import calculate_daily_aggregates

class TestWeatherMonitoring(unittest.TestCase):
    
    def test_weather_data_retrieval(self):
        city = 'Delhi'
        data = fetch_weather_data(city)
        self.assertIsNotNone(data)
        self.assertIn('main', data)
    
    def test_daily_aggregates(self):
        city = 'Delhi'
        date = '2024-10-19'  # Adjust this date as needed for testing
        aggregates = calculate_daily_aggregates(city, date)
        self.assertIsNotNone(aggregates)

if __name__ == '__main__':
    unittest.main()

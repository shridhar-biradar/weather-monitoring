**Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates**

# Project Overview
This project is a real-time weather monitoring system that retrieves weather data from the OpenWeatherMap API for six major metros in India (Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad). It processes the weather data to calculate daily aggregates like average temperature, maximum and minimum temperatures, and dominant weather conditions. It also supports configurable alert thresholds for extreme weather conditions, such as high temperatures.

# Features
* Real-time retrieval of weather data at a configurable interval (every 5 minutes).
* Conversion of temperature from Kelvin to Celsius.
* Calculation of daily weather aggregates, including:
   * Average temperature
   * Maximum temperature
   * Minimum temperature
   * Dominant weather condition
* Configurable alert system based on user-defined thresholds (e.g., temperature exceeding a certain limit).
* Data persistence using SQLite to store daily weather summaries for further analysis.

# Project Structure
weather-monitoring/
│
├── src/
│   ├── main.py                 # Main script to run the application
│   ├── weather_api.py           # Module for interacting with the OpenWeatherMap API
│   ├── data_processing.py       # Module for processing and aggregating weather data
│   ├── alert_system.py          # Module for handling alerting mechanisms
│   ├── config_loader.py         # Module for loading configuration settings
│   ├── init_db.py               # Script to initialize the SQLite database
│   └── visualization.py         # Optional module for visualizations (Not used in this version)
│
├── config/
│   └── config.json              # Configuration file for API keys and other settings
│
├── data/
│   └── weather_data.db          # SQLite database to store weather data
│
├── tests/                       # Directory for testing (if applicable)
│   └── test_weather.py          # Test cases for weather data retrieval and processing
│
├── README.md                    # Documentation for the project (this file)
├── requirements.txt             # List of dependencies and libraries to install
└── .gitignore                   # Git ignore file

# Setup Instructions

1. Clone the Repository
   * git clone https://github.com/shridhar-biradar/weather-monitoring.git
   * D:\weather-monitoring

2. Install Python Dependencies
   * pip install -r requirements.txt 
   * The requirements.txt file include libraries like:
      * requests
      * sqlite3
      * matplotlib

3. OpenWeatherMap API Key
{
    "api_key": "1a31b13168487fb15df72cd671bfb634",
    "thresholds": {
        "temperature": 35
    }
}
* temperature: Temperature for triggering alerts.

4. Initialize the Database
* Before running the application, initialize the SQLite database where daily weather summaries will be stored.
* python src/init_db.py
* This will create the weather_data.db file in the data folder with the necessary table (weather_summary) to store daily weather aggregates.

5. Run the Application
* Once the database is initialized, you can start the weather monitoring system by running the following command:
* python src/main.py
* The system will continuously retrieve weather data at the configured interval and print the real-time updates and daily weather summaries on the console.

6. Configure Alert Thresholds
* You can configure the temperature alert threshold in the config/config.json file. The system will monitor the temperature and trigger an alert if it exceeds the defined threshold for two consecutive updates.

# How it Works
* The application retrieves weather data for the specified cities from the OpenWeatherMap API.
* It processes the data to convert the temperature from Kelvin to Celsius and stores it in memory.
* Daily aggregates (average temperature, max/min temperature, dominant weather condition) are calculated at the end of each day and stored in an SQLite database.
* An alert system continuously checks for temperature threshold violations and displays alerts in the console when conditions are met.

# Design Choices
* SQLite: Chosen for data persistence as it is lightweight and easy to set up for a project of this scale.
* OpenWeatherMap API: Provides comprehensive weather data and is easy to use with a free API key.
* Python: The application is written in Python for simplicity and ease of managing HTTP requests, data processing, and alerts.

# Dependencies
The following Python libraries are required for the project:
* requests: To make API calls to OpenWeatherMap.
* sqlite3: For database storage and management of weather data.
* matplotlib: For visualization features.
* These can be installed using the requirements.txt file as shown in the setup instructions.

# Example Usage
* Here’s an example of the real-time weather updates and daily summary aggregates printed in the console:
* Daily aggregates for Delhi on 2024-10-19: {'avg_temp': 32.51153846153847, 'max_temp': 33.05, 'min_temp': 30.05, 'dominant_condition': 'Haze'}
* Daily aggregates for Mumbai on 2024-10-19: {'avg_temp': 29.836153846153852, 'max_temp': 29.99, 'min_temp': 28.99, 'dominant_condition': 'Haze'}
* Daily aggregates for Chennai on 2024-10-19: {'avg_temp': 29.323076923076922, 'max_temp': 29.58, 'min_temp': 28.76, 'dominant_condition': 'Mist'}
* Daily aggregates for Bangalore on 2024-10-19: {'avg_temp': 23.035384615384608, 'max_temp': 23.91, 'min_temp': 21.95, 'dominant_condition': 'Thunderstorm'}
* Daily aggregates for Kolkata on 2024-10-19: {'avg_temp': 27.893076923076926, 'max_temp': 27.97, 'min_temp': 26.97, 'dominant_condition': 'Haze'}
* Daily aggregates for Hyderabad on 2024-10-19: {'avg_temp': 28.84538461538462, 'max_temp': 30.23, 'min_temp': 26.23, 'dominant_condition': 'Clouds'}

# Future Enhancements
* Web Interface: Implementing a web interface to display real-time weather data and alerts using Flask or Django.

# Conclusion
This weather monitoring system meets the objectives of real-time data processing,visualizations, daily aggregation, and alerting based on configurable thresholds. The codebase is modular and can be extended with additional features like a web interface.
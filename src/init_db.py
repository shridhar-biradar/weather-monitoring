# src/init_db.py

import sqlite3
import os

def create_database():
    # Create the 'data' directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    # Specify the database file path
    db_path = os.path.join('data', 'weather_data.db')
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the weather_summary table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_summary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        date TEXT NOT NULL,
        temp REAL NOT NULL,
        weather_condition TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("Database and table created successfully.")

if __name__ == "__main__":
    create_database()

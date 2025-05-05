import pandas as pd
import requests
from dotenv import load_dotenv
import os
import datetime
import psycopg2

def extract():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    latitude = 14.17
    longitude = 121.32
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    return data

def transform(data):
	return {
        'Time': datetime.datetime.now(),
        'Location': data['name'],
        'Temperature': data['main']['temp'],
        'Min Temperature': data['main']['temp_min'],
        'Max Temperature': data['main']['temp_max'],
        'Humidity': data['main']['humidity'],
        'Weather Condition': data['weather'][0]['description'],
        'Wind Speed': data['wind']['speed'],
        'Direction': data['wind']['deg'],
        'Cloud Coverage': data['clouds']['all']
    } 

def load(data):
 
    try:
        load_dotenv()
        password_key = os.getenv("db_pass")

        connection = psycopg2.connect(
              host='localhost',
              database='demo',
              user='postgres',
              password=password_key
         )
        cursor = connection.cursor()

        insert_query = f"INSERT INTO weather_data VALUES({data['Time']},{data['Location']}, {data['Temperature']},{data['Min Temperature']},{data['Max Temperature']},{data['Humidity']},{data['Weather Condition']},{data['Wind Speed']},{data['Direction']},{data['Cloud Coverage']})"

        cursor.execute(insert_query)
        connection.commit()

    except Exception as e:
         print(f"Insertion failed... Error {e}")
    
    finally:
         cursor.close()
         connection.close()


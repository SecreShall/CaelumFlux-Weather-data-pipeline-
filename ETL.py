import requests
from dotenv import load_dotenv
import os
import datetime
import psycopg2

def extract():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    latitude = 14.599512
    longitude = 120.984222
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    return data

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def transform(data):
    
	return {
        'Time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Temperature': kelvin_to_celsius(data['main']['temp']),
        'Min Temperature': kelvin_to_celsius(data['main']['temp_min']),
        'Max Temperature': kelvin_to_celsius(data['main']['temp_max']),
        'Humidity': data['main']['humidity'],
        'Wind Speed': data['wind']['speed'],
        'Direction': data['wind']['deg'],
        'Weather Condition': data['weather'][0]['description']
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

        insert_query = f"INSERT INTO weather_data (timestamp, temperature, min_temp, max_temp, humidity, wind_speed, direction, condition) VALUES('{data['Time']}', {data['Temperature']},{data['Min Temperature']},{data['Max Temperature']},{data['Humidity']},{data['Wind Speed']},{data['Direction']},'{data['Weather Condition']}')"

        cursor.execute(insert_query)
        connection.commit()
        print("Insert successful...")

    except Exception as e:
         print(f"Insertion failed... Error {e}")
    
    finally:
         cursor.close()
         connection.close()

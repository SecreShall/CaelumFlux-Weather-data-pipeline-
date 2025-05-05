import pandas as pd
import requests
from dotenv import load_dotenv
import os
import datetime


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
        'Time': datetime.now(),
        'Location': data['name'],
        'Temperature': data['main'][0]['temp'],
        'Min Temperature': data['main'][0]['temp_min'],
        'Max Temperature': data['main'][0]['temp_max'],
        'humidity': data['main'][0]['humidity'],
        'Weather Condition': data['weather'][0]['description'],
        'Wind Speed': data['speed'],
        'Direction': data['deg'],
        'Cloud Coverage': data['clouds'][0]['all']
    }

def load():
    pass

extract()
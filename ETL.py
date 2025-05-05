import pandas as pd
import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("API_KEY")
city = 'manila'
base_url = "https://api.openweathermap.org/data/2.5/weather"

params = {"q": city, "appid": api_key, "units": "metric"}
response = requests.get(base_url, params=params)
data =response.json()

print(data['weather'][0]['description'])



def extract():
    print('yameteee')


def transform():
	pass


def load():
    pass


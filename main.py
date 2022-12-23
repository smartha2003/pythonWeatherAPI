import requests
from pprint import pprint

API_Key = 'd4e3070d08cc863e1fe649a743681c89'

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" +API_Key +"&q=" +city

weather_data = requests.get(base_url).json()

pprint(weather_data)

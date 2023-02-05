import requests
import json
import math

APPID = "bcf0f458a0dee1724256aeb4cb7df12e"  
URL_BASE = "http://api.openweathermap.org/data/2.5/forecast"
URL_GEO  = "http://api.openweathermap.org/geo/1.0/direct"
lat = 0.0
lon = 0.0

def current_weather(q: str = "Ханты-Мансийск", limit: int = 1, appid: str = APPID) -> dict:
    
    jsonData = requests.get(URL_GEO, params=locals()).json()
    lat = jsonData[0]['lat']
    lon = jsonData[0]['lon']
    
    return weather_onecall(lat, lon)

def weather_onecall(lat: float = '', lon: float = '', cnt: int = 1, units: str = 'metric', lang: str = 'ru', appid: str = APPID) -> dict:
    
    jsonWeather = requests.get(URL_BASE, params=locals()).json()
    weather_des = jsonWeather['list'][0]['weather'][0]['description']
    temp = math.ceil(jsonWeather['list'][0]['main']['temp'])
    city = jsonWeather['city']['name']
    temp_max = jsonWeather['list'][0]['main']['temp_max']
    temp_min = jsonWeather['list'][0]['main']['temp_min']

    return ('Сегодня в {} {}, температура: {}°' .format(city, weather_des, temp))    
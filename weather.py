import streamlit as st

import datetime as dt
import requests

st.header("Weather API App :sun_with_face::partly_sunny::thunder_cloud_and_rain: ")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "8230aa0896b6fa4a24698661e7cf92fb"

city = st.text_input("Enter your city Name")
CITY = city

def kelvin_to_celsius_fahrenheit(kelvin):
  celsius = kelvin - 273.15
  fahrenheit = celsius * (9/5) + 32
  return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

if st.button("show"):
  temp_kelvin = response['main']['temp']
  temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
  feels_like_kelvin = response['main']['feels_like']
  feels_like_celsius , feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
  wind_speed = response['wind']['speed']
  humidity = response['main']['humidity']
  description = response['weather'][0]['description']
  sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
  sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

  st.write(f"**Temperature** :mostly_sunny: in {CITY}: {temp_celsius:.2f}°c or {temp_fahrenheit:.2f}°F")
  st.write(f"**Humidity** :sun_behind_rain_cloud: in {CITY}: {humidity}%")
  st.write(f"**wind speed** :tornado_cloud: in {CITY}: {wind_speed}m/s")
  st.write(f"**General Weather** :barely_sunny: in {CITY}: {description}")
  st.write(f"**sun rises**:sunrise: in {CITY} at {sunrise_time} local time.")
  st.write(f"**sun sets** :city_sunset: in {CITY} at {sunset_time} local time.")
else:
  st.write("Please press the show button")



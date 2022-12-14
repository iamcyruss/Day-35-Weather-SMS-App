import requests
import time
import os
from twilio.rest import Client


account_sid = ""
auth_token = ""
from_ = ""
client = Client(account_sid, auth_token)
weather_list = ["Thunderstorm", "Drizzle", "Rain", "Snow", "Mist", "Smoke", "Haze", "Dust", "Fog", "Sand", "Ash", "Squall", "Tornado", "Clouds"]
weather_codes = "https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2"
weather_params = {
    "appid": "",
    "lat": 39.557,
    "lon": -104.915,
    "units": "imperial",
    "cnt": 8,
}
response1 = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response2 = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=weather_params)
response1.raise_for_status()
response2.raise_for_status()
forcast = response1.json()
todays_list = ''


for day in forcast['list']:
    local_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(day['dt']))
    weather = day['weather']
    if weather[0]['main'] in weather_list:
        print(f"{weather[0]['main']} predicted beginning at {local_time}.\n{day['weather']}\n{weather_codes}")
        todays_list = f"{todays_list}" + f"{weather[0]['main']} predicted beginning at {local_time}.\n"

print(todays_list)
if len(todays_list) > 0:
    message = client.messages.create(body=str(todays_list), from_=from_, to='')
    print(message.sid)

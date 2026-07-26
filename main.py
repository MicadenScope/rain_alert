import os
from datetime import datetime
from twilio.rest import Client
from requests import *

ACCOUNT_SID = os.environ["ACCOUNT_SID"] #TWILIO_ACCOUNT_SID
AUTH_TOKEN = os.environ["AUTH_TOKEN"] #TWILIO_AUTH_TOKEN
WEATHER_API_KEY = os.environ["WEATHER_API_KEY"] #openweathermap.org/api_keys
SENDER_PHONE = os.environ["SENDER_PHONE"]
RECIPIENT_PHONE = os.environ["RECIPIENT_PHONE"]

today = datetime.now()
today_tuple = (today.month, today.day)

def send_notification():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain 🌧️ today. Remember to bring an ☔️.",
        from_=SENDER_PHONE,
        to=RECIPIENT_PHONE,
    )

    #print(message.body)

weather_params = {
    "lat": 43.293674,
    "lon": 13.450901,
    "appid": WEATHER_API_KEY,
    "cnt": 4,
}

response = get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
if will_rain:
    send_notification()



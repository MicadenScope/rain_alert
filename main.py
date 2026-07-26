import os
from twilio.rest import Client
from requests import *

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
API_KEY = os.environ["TWILIO_AUTH_TOKEN"]
sender_phone_number = os.environ["MY_TWILIO_PHONE_NUMBER"]
receiver_phone_number = os.environ["RECEIVER_PHONE_NUMBER"]

def send_notification():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain 🌧️ today. Remember to bring an ☔️.",
        from_=sender_phone_number,
        to=receiver_phone_number,
    )

    print(message.body)


weather_params = {
    "lat": 43.293674,
    "lon": 13.450901,
    "appid": API_KEY,
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



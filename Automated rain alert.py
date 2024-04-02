# Rain alerts
# Account Sid and auth_token found in my account (fres8@g)
# TWILIO numbers in mail

import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# OpenWeatherMap API endpoint and  API key
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("17e83e5514e0e68d0a0875960e404e18")

# Twilio credentials
account_sid = "ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")


# Parameters for weather API request
weather_params = {
    "lat": "7.9465",
    "lon": "1.0232",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# Send request to OpenWeatherMap API
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False


# Check if it's going to rain within the next 12 hours
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

 # Set up Twilio HTTP client with proxy if needed
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # Send a message using Twilio
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☔️",
        from_="TWILIO VIRTUAL NUMBER",
        to="TWILIO VERIFIED REAL NUMBER"
    )
    print(message.status)

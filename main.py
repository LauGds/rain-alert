import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "API KEY"
LAT = "LATITUDE"
LON = "LONGITUDE"
account_sid = "ACCOUNT SID"
auth_token = "TOKEN"

parameters = {
    "appid": api_key,
    "lat": LAT,
    "lon": LON,
}



response = requests.get(url=OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["weather"][0]["id"]

if int(weather_data) < 700:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_="SENDER PHONE NUMBER",
        to="RECIPIENT PHONE NUMBER"
        )
    print(message.status)
    

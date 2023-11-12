import requests
from api_key import api_key, account_sid, auth_token, phone_number
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"


# "lat": 33.4484367,
#     "lon": -112.074141,
#     "appid": api_key

weather_params = {
    "lat": 27.488510,
    "lon": -99.507591,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    print(condition_code)    
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body= "It's going to rain to day. Remember to bring an umbrella.",
            from_= "+18447800396", 
            to=phone_number
    )
    print(message.status)



import requests
from twilio.rest import Client

twilio_num = "+447897013216"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "aa485a1920ae6a669f484a5d1ca4e1fe"
account_sid = "AC8be1957cf1721251c370073cae9ad1d9"
auth_token = "ac6aa0502e819cecc644d64b4b5348ea"

weather_params = {
	"lat": 52.406822,
	"lon": -1.519693,
	"appid": api_key,
	"cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
	condition_code = hour_data["weather"][0]["id"]
	if int(condition_code) < 700:
		will_rain = True

if will_rain:
	client = Client(account_sid, auth_token)
	message = client.messages \
					.create(
						body="Bring an umbrella!☂️",
						from_= "+447897013216",
						to= "+447599566181",
					)
	print(message.status)


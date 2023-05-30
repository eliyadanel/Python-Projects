from twilio.rest import Client
import requests as rq

"""Uncomment these lines if you want to upload this code to PythonAnywhere https://www.pythonanywhere.com/"""
# from twilio.http.http_client import TwilioHttpClient
# import os
#
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}

api_key = "156bfb9d62cf9d4683421a883d66faff"

twillio_sid = "AC183fd3f6ef1c0ead3b66055bceaff28e"
twillio_auth_token = "6c24097c4a63cf9cb4c736df9eef4a25"
twillio_num = "+15077097616"
my_num = "+972528674188"

parameters = {
    "lat": 31.768318,
    "lon": 35.213711,
    "appid": api_key,
}

response = rq.get("http://api.openweathermap.org/data/2.5/weather?", params=parameters)
print(response.status_code)
data = response.json()
print(data)
sky_status = data["weather"][0]["description"]
weather_id = data["weather"][0]["id"]
kelvin_temp = data["main"]["temp"]
cel_temp = (kelvin_temp - 273.15).__round__()
print(cel_temp)

def sms(bring, emoji):
    client = Client(twillio_sid, twillio_auth_token)
    client.messages.create(body=f"{bring} an umbrella today!{emoji}", from_=twillio_num, to=my_num)


if weather_id < 700:
    sms(bring="Don't forget to bring", emoji="☔")
else:
    sms(bring="No need for", emoji="☀")

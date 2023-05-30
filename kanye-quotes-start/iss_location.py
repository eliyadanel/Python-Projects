import requests as rq
from datetime import datetime
from math import isclose
import smtplib
import time
"""
Requests codes meaning: 
1XX: Conection is slow- hold on
2XX: Success
3XX: No permissions
4XX: Something is wrong on your end
5XX: Something is wrong on my end
"""
MY_EMAIL = "ddeliya2@gmail.com"  # source email
MY_PASS = "pvvnfutgttrmsimu"  # app password for gmail account
MY_LAT = 31.768318
MY_LNG = 35.213711
MY_POS = (MY_LNG, MY_LAT)

# this function calculates if the iss is close to my coordinates:
def iss_close():
    iss_response = rq.get(url='http://api.open-notify.org/iss-now.json')
    iss_response.raise_for_status()  # checks for errors
    iss_data = iss_response.json()
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    if isclose(MY_LNG, iss_longitude, rel_tol=10, abs_tol=0) and isclose(MY_LAT, iss_latitude, rel_tol=10, abs_tol=0):
        return True

# this function checks if it is nighttime in my coordinates:
def is_night():
    location_parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }

    sun_response = rq.get("https://api.sunrise-sunset.org/json", params=location_parameters)
    sun_response.raise_for_status()  # checks for errors
    sun_data = sun_response.json()
    # isolating the sunrise and sunset values and storing them in variables,
    # then isolating the hour digits in which the sun sets and rises in my location:
    sunset = int(sun_data['results']['sunset'].split('T')[1].split(':')[0])
    sunrise = int(sun_data['results']['sunrise'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour  # the time from the datetime module
    if sunset <= time_now <= sunrise:
        # it's dark
        return True

while True:
    time.sleep(60)
    if iss_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # oppening the connection with the gmail smtp server and port 587
            connection.starttls()  # securing the connection with TL: transport layer security.
            connection.login(user=MY_EMAIL, password=MY_PASS)  # loggin into the gmail account with the email and pass
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="eliyadanel@gmail.com",
                msg="Subject:The ISS is positioned above you!\n\nYou should go outside and try to spot the ISS.\n"
                    "It's dark outside so you should be able to see it ‍🚀🌛🪐⭐🌌‍"
            )




import requests
import os
from datetime import datetime

location = input("Enter the city name:")
data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=b102b0d2cbcc149cb68ce97704aad006").json()   

if data['cod'] == '404':
    print("Invalid City: {}, Please check your city name.".format(location))
else:
    temp_city = ((data['main']['temp'])- 273.15)
    weather_desc = data['weather'][0]['description']
    hmdt = data['main']['humidity']
    wind_spd= data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

print("----------------------------------------------")
print("Weather Stats for - {} || {}".format(location.upper(),date_time))
print("----------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc:",weather_desc)
print("Current humidity:",hmdt, '%')
print("Current weather desc:",wind_spd, 'kmph')


import requests
import os
from datetime import datetime
user_api = b102b0d2cbcc149cb68ce97704aad006

location = input("Enter the city name:")

complete_api_link = "http://api.openweathermap.org/geo/1.0/direct?q="+location+"&limit={limit}&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print("Invalid City: {}, Please check your city name.".format(location))
else:
    temp_city = ((api_data['main']['temp'])- 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd= api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

print("----------------------------------------------")
print("Weather Stats for - {} || {}".format(location.upper(),date_time))
print("----------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc:",weather_desc)
print("Current humidity:",hmdt, '%')
print("Current weather desc:",wind_spd, 'kmph')


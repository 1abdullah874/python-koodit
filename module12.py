import json

import requests
server = "https://api.chucknorris.io/"
request = server + "/jokes/random"
try:
    response = requests.get(request).json()
    print(json.dumps(response, indent=2))
except requests.exceptions.RequestException as error:
    print("hello", error)




APIKEY = ""

def open_weather(city):
    server = "https://api.openweathermap.org/"
    req = f"{server}data/2.5/weather?q={city}&appid={APIKEY}"
    response = requests.get(req)
    return response.status_code, response.json()

def temp_celsius(kelvin):
    return kelvin - 273.15

city = input("Enter city: ")
status_code, weather_data = open_weather(city)

if status_code == 200:
    kelvin_temp = weather_data['main']['temp']
    celsius_temp = temp_celsius(kelvin_temp)
    print(f"The temperature in {city} is {celsius_temp:.2f}°C.")
else:
    print("Error fetching data:", weather_data.get("message", "Unknown error"))




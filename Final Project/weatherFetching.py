import requests
import json
import datetime


cityName = input("Enter the city you wisth to see weather: ")
userApi = "c75922bf9e3274652f0112981a5560f8"

response_API = requests.get(
    'https://api.openweathermap.org/data/2.5/weather?q={cityName}&units=metric&appid={userApi}'.format(cityName=cityName, userApi=userApi))
data = response_API.text

cityData = json.loads(data)

reqData = {
    "Temperature": {
        "Temp":cityData["main"]["temp"],
        "Min": cityData["main"]["temp_min"],
        "Max": cityData["main"]["temp_max"]
    },
    "WindSpeed": cityData["wind"]["speed"],
    "Humidity": cityData["main"]["humidity"],
    "Cloud": cityData["weather"][0]["main"],
    "Pressure": cityData["main"]["pressure"]/100,
    "Sunrise": datetime.datetime.fromtimestamp(cityData["sys"]["sunrise"]),
    "Sunset": datetime.datetime.fromtimestamp(cityData["sys"]["sunset"])

}
print("{cityName} has Temp: {temp}°C\nMin-Temp: {minTemp}°C\nMax-Temp: {maxTemp}°C\nWindspeed: {windspeed} m/s\nHumidity: {humidity}%\nCloud: {cloud}\nPressure: {pressure} N/m² \nSunrise: {sunrise}\nSunset: {sunset}".format(cityName = cityName, temp = reqData['Temperature']["Temp"], minTemp = reqData['Temperature']["Min"], maxTemp=reqData['Temperature']["Max"], windspeed = reqData['WindSpeed'], humidity = reqData['Humidity'], cloud = reqData['Cloud'], pressure = reqData['Pressure'], sunrise = reqData["Sunrise"], sunset = reqData["Sunset"]))



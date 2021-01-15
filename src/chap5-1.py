# 都市名で指定して、天気を取得
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
import requests
import json
from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe,JP", key="")
jsondata = requests.get(url).json()
pprint(jsondata)

#print(jsondata["name"])
#print(jsondata["main"]["temp"])
#print(jsondata["weather"][0]["main"])
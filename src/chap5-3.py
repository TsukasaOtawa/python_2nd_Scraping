import requests
import json
from datetime import datetime, timedelta, timezone
from pprint import pprint # pprint (pretty-print)
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# https://openweathermap.org/api
url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={key}&lang=ja&units=metric"
url = url.format(city="Kobe,JP", key="")

jsondata = requests.get(url).json()
# pprint(jsondata)
# print(jsondata[0]["name"]) #3hごと 8/day * 5 day = 40
#'list': [{'clouds': {'all': 24},
#           'dt': 1610712000,
#           'dt_txt': '2021-01-15 12:00:00',
df = pd.DataFrame(columns=["気温"])
tz = timezone(timedelta(hours=+9), "JST")
for dat in jsondata["list"]:
    jst = str(datetime.fromtimestamp(dat["dt"], tz))[:-9]
    weather = dat["weather"][0]["description"]
    temp = dat["main"]["temp"]
    # print("日時={jst}, 天気={w}, 気温={t}度".format(jst=jst, w=weather, t=temp))
    df.loc[jst] = temp

# pprint(df)
df.plot(figsize=(15, 8))
plt.ylim(-10, 40)
plt.grid()
plt.show()
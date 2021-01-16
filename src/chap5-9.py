from datetime import datetime, timedelta, timezone

#'list': [{'clouds': {'all': 24},
#           'dt': 1610712000,
#           'dt_txt': '2021-01-15 12:00:00',

# UTC を JST に変換
timestamp = 1610712000
tz  = timezone(timedelta(), "UTC")
utc = datetime.fromtimestamp(timestamp, tz)
print(utc)

tz  = timezone(timedelta(hours=+9), "JST")
jst = datetime.fromtimestamp(timestamp, tz)
print(jst)
print(str(jst)[:-9])
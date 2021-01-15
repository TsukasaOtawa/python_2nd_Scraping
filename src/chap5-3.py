import json
from pprint import pprint # pprint (pretty-print)

with open("test_chap5_2.json") as f:
    jsondata = json.loads(f.read())
    pprint(jsondata)
    print(jsondata[0]["name"])
import requests

url = "https://www.ymori.com/books/pythons2nen/test1.html"
response = requests.get(url)

response.encoding = response.apparent_encoding

print(response.text)
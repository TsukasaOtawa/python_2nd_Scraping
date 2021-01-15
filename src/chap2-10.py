import requests
from bs4 import BeautifulSoup
import urllib

load_url = "https://www.ymori.com/books/python2nen/test2.html"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

filename = "linklist.txt"
with open(filename, mode="w") as f:
    for element in soup.find_all("a"):
        url = element.get("href")
        print(url)
        link_url = urllib.parse.urljoin(load_url, url)
        f.write(element.text + "\n")
        f.write(link_url + "\n")
        f.write("\n")

image_url = "https://www.ymori.com/books/python2nen/sample1.png"
imgdata = requests.get(image_url)
filename = image_url.split("/")[-1]

with open(filename, mode="wb") as f:
    f.write(imgdata.content)

import requests
from pathlib import Path
out_folder = Path("download")
out_folder.mkdir(exist_ok=True)

out_path = out_folder.joinpath(filename)

with open(out_path, mode="wb") as f:
    f.write(imgdata.content)
import requests
from bs4 import BeautifulSoup
import time

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text, 'html.parser')

containers = html.select("div.inner")
rank = 1
for container in containers:
    title = container.select_one("dt.title")
    chn = container.select_one("dd.chn")
    hit = container.select_one("span.hit")
    like = container.select_one("dd.meta span.like")

    print(str(rank)+"위")
    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)
    rank += 1

containers = html.select("div.cds")
for container in containers:
    title = container.select_one("dt.title")
    chn = container.select_one("dd.chn")
    hit = container.select_one("span.hit")
    like = container.select_one("span.like")

    print(str(rank)+"위")
    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("=" * 50)
    rank += 1
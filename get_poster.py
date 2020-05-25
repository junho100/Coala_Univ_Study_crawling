#상세 정보로 들어가 영화 포스터 이미지 파일 저장하기

#컨테이너 : div.lister-item-content
#제목 href : h3 a (https://www.imdb.com 생략)
#포스터 : div.poster img

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

raw = requests.get("https://www.imdb.com/list/ls016522954/")
html = BeautifulSoup(raw.text, "html.parser")

containers = html.select("div.lister-item-content")

for container in containers:
    title = container.select_one("h3 a")
    in_raw = requests.get("https://www.imdb.com"+title.attrs['href'])
    in_html = BeautifulSoup(in_raw.text, "html.parser")
    img_src = in_html.select_one("div.poster img").attrs['src']

    urlretrieve(img_src, "posters/"+title.text+".png")
import requests
from bs4 import BeautifulSoup

#컨테이너 ul.type01 > li
#제목 a._sp_each_title
#출처 span._sp_each_source

f = open("news.csv", "w", encoding = 'UTF-8')
f.write("제목,언론사\n")
for page in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코알라&start="+str(page))
    html = BeautifulSoup(raw.text, 'html.parser')

    containers = html.select("ul.type01 > li")

    for container in containers:
        title = container.select_one("a._sp_each_title").text
        source = container.select_one("span._sp_each_source").text
        title = title.replace(',', "")
        source = source.replace(',', "")
        f.write(title + ',' + source + '\n')

f.close()
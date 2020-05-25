#imdb 현재 상영중인 영화의 제목/평점/감독,배우(같이)
#심화-Action장르의 영화면 출력

#컨테이너 : div.lister-item-content
#제목 : h3 a
#메타스코어 : span.metascore
#감독 및 배우 : p.text-muted > a
#장르 : p.text-muted > span.genre

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/list/ls016522954/", headers={'User-Agent':'Mozilla/5.0'})
html = BeautifulSoup(raw.text, "html.parser")

containers = html.select("div.lister-item-content")
#제목, 메타스코어, 감독 및 배우 출력
for container in containers:
    title = container.select_one("h3 a").text
    try:
        meta = container.select_one("span.metascore").text
    except:
        meta = " "
    dir_act_list = container.select("p.text-muted > a")

    print(title, meta)
    for dir_act in dir_act_list:
        print(dir_act.text, end=" ")
    print("\n=============================================")

#심화 -> action 장르만 출력
print("<심화>")

for container in containers:
    gen = container.select_one("p.text-muted > span.genre").text
    if "Action" in gen:
        title = container.select_one("h3 a").text
        try:
            meta = container.select_one("span.metascore").text
        except:
            meta = " "
        dir_act_list = container.select("p.text-muted > a")

        print(title, meta)
        for dir_act in dir_act_list:
            print(dir_act.text, end=" ")
        print(gen)
        print("=============================================")
    else:
        continue
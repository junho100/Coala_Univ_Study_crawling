#2. 컨테이너 : div.section-result
# 제목 : h3.section-result-title, 평점 : span.section-result-rating > span(모두 x), 위치 : span.section-result-location
#https://www.google.com/maps/search/
#다음버튼 : span.n7lv7yjyC35__button-next-icon
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromeDriver\chromedriver.exe')
driver.get("https://www.google.com/maps/search/카페")
time.sleep(10)
cnt = 0
for i in range(5):
    containers = driver.find_elements_by_css_selector("div.section-result")
    for container in containers:
        title = container.find_element_by_css_selector("h3.section-result-title").text
        try:
            score = container.find_element_by_css_selector("span.section-result-rating > span").text
        except:
            score = "None"
        loc = container.find_element_by_css_selector("span.section-result-location").text
        print(title, score, loc)
        cnt +=1
        print(cnt)
        print("="*15)
    btn = driver.find_element_by_css_selector("span.n7lv7yjyC35__button-next-icon")
    btn.click()
    time.sleep(3)
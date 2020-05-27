#1. (1) 크롬을 연다 (2) 파파고에 접속한다 (3) seize the day 를 입력한다 (4) 변역하기를 누른다 (5) 번역된 결과를 받는다
#2. 입력창 : textarea#txtSource
#   번역버튼 : button#btnTranslate
#   결과창 : div#targetEditArea
#드라이버 위치 : 'C:\chromeDriver\chromedriver.exe'

from selenium import webdriver
import time

driver = webdriver.Chrome('C:\chromeDriver\chromedriver.exe')
driver.get("https://papago.naver.com/")
time.sleep(10)
input_box = driver.find_element_by_css_selector("textarea#txtSource")
input_box.send_keys("seize the day!")
btn = driver.find_element_by_css_selector("button#btnTranslate")
time.sleep(1)
result = driver.find_element_by_css_selector("div#targetEditArea").text
print(result)
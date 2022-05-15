#네이버 주간 날씨

import requests
from bs4 import BeautifulSoup

#1.주소결정
url = 'https://weather.naver.com/today/02173101'

#2. 페이지 요청
resp = requests.get(url)

#3. 구문분석
text=resp.text
html=BeautifulSoup(text, 'html.parser')

#4. 자료수출\
#4_1. 주간 닐씨 html 블록 수출
block = html.find('ul', class_='week_list')
#4_2. 블록에서 날짜 코드를 모두 수출
date = block.find_all('span', class_='date')
print(date)
#4_3. 블록에서 요일 코드 모두 수출(w_day)
w_day = block.find_all('strong', class_='day')
#4-4 블록에서 최저기온 수출(tmp_l)
tmp_l = block.find_all('span', class_='lowest')
#4-5 블록에서 최고 기온 수출(tmp_h)
tmp_h = block.find_all('span', class_='highest')
#4-6. 지역명 추출 및 출력(loc)
loc = html.find('strong', class_='location_name')

block = html.find('ul', class_='week_list')
date = block.find_all('span', class_='date')
w_day = block.find_all('strong', class_='day')
tmp_l = block.find_all('span', class_='lowest')
tmp_h = block.find_all('span', class_='highest')
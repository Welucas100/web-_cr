#1년전 영화 순위

import requests
from bs4 import BeautifulSoup

#1. 주소결정 (순위를 조회할 날짜를 입력하세요(yyyymmdd): )
date = input('순위를 조회할 날짜를 입력하세요(yyyymmdd): ' )
url = f'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cnt&tg=0&date={date}'

#2. 페이지 요청
resp= requests.get(url)

#3. 구문분석
text = resp.text
html = BeautifulSoup(text, 'html.parser')

#4. 자료추출
r_tag = html.find_all('div', class_='tit3')

#5. 출력
# 1~10위 까지 영화 출력하기
for idx in range(5):
    title = r_tag[idx].text.strip()
    print(idx + 1, title)


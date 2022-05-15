#네이버 영화 순의

import requests
from bs4 import BeautifulSoup

#1. 주소 결정
url =  'https://movie.naver.com/movie/sdb/rank/rmovie.naver'

#2. 페이지 요청
resp = requests.get(url)

#3. 구문분석
text = resp.text
html = BeautifulSoup(text, 'html.parser')

#4. 자료추출
ts = html.find_all('div', class_='tit3')

#5. 출력 (순위, 영화 제목)
for idx, one in enumerate(ts):
    rank = idx + 1
    title = one.text.strip()
    print(f'{rank}위. {title}')
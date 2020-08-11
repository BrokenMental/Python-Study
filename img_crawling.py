from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

#폴더 생성을 위한 라이브러리
import os

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어 입력 : ')
resultUrl = baseUrl + quote_plus(plusUrl)

html = urlopen(resultUrl).read()
soup = BeautifulSoup(html, 'html.parser')

img = soup.find_all(class_='_img')

path = './img/'

#mkdir은 현재 없는 폴더 밑에 다른 폴더를 한번에 생성하지 못한다.
#makedirs는 한번에 깊이 있는 폴더를 만들 수 있다.
#exist_ok=True : 폴더가 존재하지 않으면 생성, 존재하면 넘어감
os.makedirs(path, exist_ok=True)

n = 1
for i in img:
    #해당 태그의 속성에 접근할때 attrs 없이 ['{key}'] 사용 가능
    imgUrl = i['data-source']

    with urlopen(imgUrl) as f:
        #wb : binary파일 write
        with open(path + plusUrl + str(n) + '.png', 'wb') as h:
            imgread = f.read()
            h.write(imgread)

    n += 1

print('종료')
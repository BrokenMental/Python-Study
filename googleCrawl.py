from urllib.parse import quote_plus
from bs4 import BeautifulSoup
#selenium : web test에 사용되는 프레임워크, webdriver API를 통해 렌더링이 완료된 후의 DOM 결과물에 접근할 수 있음
#브라우저 제어가 필요
#직접 브라우저를 제어하기 때문에 header값 없이도 크롤링이 가능
#여기선 Chrome 사용 webdriver 설치 : https://chromedriver.chromium.org/downloads
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('검색어 입력 : ')
resultUrl = baseUrl + quote_plus(plusUrl)

#chrome webDriver 위치가 현재 개발폴더 위치와 다르면 Chrome({경로})와 같이 사용
driver = webdriver.Chrome()

#브라우저가 열리고 입력된 url로 이동
driver.get(resultUrl)

html = driver.page_source
soup = BeautifulSoup(html)

#select로 가져올 경우 list형식으로 가져옴
r = soup.select('.r')
for i in r:
    #list object의 경우엔 text를 가져올 수 없음, 텍스트를 불러오기 위해 select_on 사용
    print(i.select_one('.LC20lb.DKV0Md').text)
    #print(i.select_one('.iUh30.bc').text)
    print(i.a.attrs['href'], '\n')

driver.close()
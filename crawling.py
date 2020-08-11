#request 라이브러리
#urllib은 URL 요청 승인 확인, urllib2는 URL 요청에 대한 헤더를 설정하기 위해 Request 오브젝트를 승인 할 수 있음
#urllib은 GET 쿼리 문자열 생성에 사용되는 urlencode 메소드를 제공, urllib2에는 해당 기능이 없음(가끔 함께 사용되는 이유)
#urllib은 매개변수를 전달하기 전 urllib.encode() 메서드를 사용해서 인코딩을 해야함
#python3에선 urllib2는 urllib으로 포팅되었음
#requests는 http 라이브러리로 매개변수를 자동으로 인코딩함, 응답을 유니코드로 자동 디코딩
#응답 실패시 urllib2는 URLError를 발생시키는 반면 requests는 정상적인 응답 객체를 반환
import urllib.request
import requests

#url 한글처리
import urllib.parse

#크롤링 라이브러리
from bs4 import BeautifulSoup

#403에러 방지 헤더 추가
headers = {'User-Agent' : 'Mozilla/5.0'}

baseUrl = 'https://www.google.com/search?q='
inputUrl = input('검색어를 입력하세요 : ')
inputStart = input('페이지 번호를 입력하세요 : ')

#검색어 한글 처리, url에선 영어가 아닐경우 아스키코드로 바뀌기 때문에 변환 작업이 필요
url = baseUrl + urllib.parse.quote_plus(inputUrl) + 'start=' + str((int(inputStart)-1)*10)
req = urllib.request.Request(url, headers=headers)

#html.parser와 lxml의 차이점
#html.parser : 단순한 HTML문서 파싱에 사용
#lxml : 매우 빠른 파싱 속도, lxml 추가 설치 필요
#추가, html5lib : 웹 브라우저와 같은 방식으로 페이지 파싱, 유효한 HTML5 생성, 매우느림, html5lib 설치 필요

#urllib.request 활용
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

#requests 모듈 활용
res = requests.get(url)
soup2 = BeautifulSoup(res.text, 'lxml')

#출력
#print(soup)
print('\n')

#값의 개수 출력
#print(len(soup))

#python에서 class가 예약어이기 때문에 html class를 가져올땐 class_ 를 사용한다.
#find는 index가 제일 작은 1개의 결과 값
#find_all은 모든 결과 값
#total = soup.find_all('div')

#find 세부검색
#soup.find('div', {'class': 'className'})

#파이썬 for문
for g in soup2.find_all(class_='kCrYT'):
    if(g.find('a', {'class':''}) != None and g.find('a', {'class':''}).find('div', {'class':'BNeawe'}) != None):
        print('제목 : ', g.find('a', {'class':''}).find('div', {'class':'BNeawe'}).text)
        print('url : ', g.find('a', {'class':''}).attrs['href'], '\n')

#구글 검색결과 크롤링 시 원하는 결과가 제대로 나오지 않음, 리스트 결과 순서가 제멋대로이거나 리스트 데이터가 여러번 반복됨
# for i in total:
#     for j in i: #.find_all(class_='ZINbbc xpd O9g5cc uUPGi'):
#         print(j)
    # for j in i.find_all(class_='kCrYT'):
    #     if j.find('a') == None or j.find('div', class_='BNeawe').text == "길찾기":
    #         continue
    #     else:
    #         if len(j) == 1:
    #             print('제목 : ', j.find('div', class_='BNeawe').text)
    #             print('url : ', j.find('a').attrs['href'], '\n')

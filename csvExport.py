import csv
from urllib.request import urlopen
from urllib.parse  import quote_plus
from bs4 import BeautifulSoup

search = input('검색어 입력 : ')
#f.{} formatting, 변수를 문자열에 나타낼 때 사용
url = f'https://m.search.naver.com/search.naver?where=m_view&sm=mtb_jum&query={quote_plus(search)}'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

total = soup.select('.api_txt_lines.total_tit')
searchList = []

#리스트로 나타내기 위해 반복
for i in total:
    temp = []
    temp.append(i.text)
    temp.append(i.attrs['href'])
    searchList.append(temp)

#파일 생성
#newline : csv 모듈에서 데이터를 쓸 때 각 라인 뒤에 빈 라인이 추가되는 문제를 해결하기 위해 python3에서 추가된 옵션
f = open(f'{search}.csv', 'w', encoding='utf-8', newline='')
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i) #writerow() 메서드를 통해 list 데이터 추가

f.close()

print('완료')
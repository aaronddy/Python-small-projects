import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs


'웹 문서 자료를 가져와 가공하기_quotes to scrape'

'''
1. urlopen으로 웹 사이트 정보 가져오기
- url 객체에 접속하고 싶은 웹 사이트의 URL 주소를 저장. 여기서 url 객체에 저장되는 건 그냥 문자열일 뿐, 아무런 의미가 없음
- 이 주소에 해당하는 웹 사이트에 원하는 정보를 요청해서 그 결과물을 반환하는 명령: urllib.request.urlopen('URL 주소')
- read() 이용해서 결과물 읽어오기
'''

url = 'http://quotes.toscrape.com/'
html = ur.urlopen(url)

# print(html.read()[:200])



'''
2. 뷰티풀수프로 자료형 변환하기
- html 객체에 저장한 자료의 정보를 쉽게 추출할 수 있는 형태, 즉 parsing하기 쉬운 혀앹로 변환
- 'parsing'이란 웹 문서에서 원하는 패턴이나 순서로 자료를 추출해 가공하는 것을 말함.
'''

soup = bs(html.read(), 'html.parser')
# print("soup", soup)

# print('html', type(html))
# print('soup', type(soup))


a_soup = bs(ur.urlopen(url).read(), 'html.parser')
# print("a_soup", a_soup)



'3. `find_all`로 원하는 태그만 모으기'

# print(a_soup.find_all('span')[0].text)
# print(a_soup.find_all('span')[1].text)

span_list = a_soup.find_all('span')

'span 태그 텍스트 출력'
# for i in span_list:
#   print(i.text) 




'''
4. 태그 안에 정의된 특정 클래스를 찾아 모으기
'''

quotes = a_soup.find_all('div', {'class':'quote'})
# print("quote", quote)

quotes_list = []
for i in quotes:
  contents = i.text

  content = re.findall('.+', contents)
  quote = content[0]
  author = content[1][2:]
  tags = content[5:]

  print(quote, author, tags)

  quotes_list.append([quote, author, tags])

print(quotes_list)


usecsv.writecsv('the_quotes.csv', quotes_list)
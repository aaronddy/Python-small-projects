import os
import re
import codecs


'''

2. 대본에 등장하는 인물 리스트 만들기

'''

fhand = codecs.open('friends101.txt', 'r', 'utf-8')
script101 = fhand.read()

char = re.findall('[A-Z][a-z]+:', script101)              
charSet = set(char)                                        # set으로 중복된 원소 지우기, list와 달리 set은 중복 허용 x
# print(type(charSet))

nameList = []

for item in charSet:
  item = item[:-1]
  # print(item)
  
  nameList.append(item)
print(nameList)



'''
1) char = re.findall('[A-Z][a-z]+:', script101)      
=> ['Waitress', 'Joey', 'All', 'Customer', 'Phoebe', 'Scene', 'Rachel', 'Frannie', 'Note', 'Paul', 'Monica', 'Chandler', 'Ross']

2) char = re.findall('[A-Za-z]+:', script101)        
=> ['All', 'Joey', 'Paul', 'Ross', 'Monica', 'by', 'Frannie', 'Note', 'Chandler', 'Phoebe', 'Customer', 'TV', 'Scene', 'me', 'Rachel', 'Waitress']

1)은 대문자 뒤에 소문자가 오는 걸로 구분
2)은 대문자든 소문자든 문자가 오면 되기 때문에 'by', 'me'와 같은 것도 추출이 됨.


그럼에도 'All', 'Scene', 'Note'와 같은 게 들어갔지만 이와 같은 부분을 제거하기 위해서 코드작성은 어려워 보임.
'''

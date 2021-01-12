import os
import re
import codecs

fhand = codecs.open('friends101.txt', 'r', 'utf-8')
script101 = fhand.read()
# print(type(script101), script101[:100])

'''

1. 특정 등장인물의 대사만 모아서 텍스트 파일로 저장하기
  
findall : 특정 패턴을 문자열에서 모두 찾아 '리스트' 형태로 반환
(search, match문은 제대로 찾았는지 확인하는 절차가 따로 필요한 반면 findall은 찾으면 결과값이 빈 리스트[]로 출력)

'''

monicaLines = []                                          # 모니카 대사를 담을 빈 리스트 생성

lines = re.findall('.+\r', script101)                     # \r을 기준으로 하나의 대사로 구분
print(len(lines))                                         # 343 

for line in lines:
  line = line.rstrip()

  monica = re.findall('Monica: .+',  line)                # 'Monica: ' 에 해당하는 대사만 추출  
  if len(monica) != 1 : continue                          # 빈 리스트(모니카가 아닌 다른 인물의 대사)일 경우엔 skip

  monicaLines.append(monica[0])                           # 모니카의 대사들만 monicaLines 리스트에 append

print(monicaLines)




# 텍스트 파일로 저장

item = ''

for line in monicaLines:
  item += line + '\n'
print(item)

f = open('monica_lines.txt', 'w', encoding='utf-8')
f.write(item)
f.close()


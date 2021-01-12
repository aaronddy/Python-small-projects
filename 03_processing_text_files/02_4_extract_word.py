import os
import re

'''

4. 특정 단어의 예문만 모아서 텍스트 파일로 저장하기

- readlines : 한 줄에 들어간 문장을 하나의 원소로 갖는 리스트를 반환하는 명령어
- writelines : 리스트에 들어있는 원소를 하나씩 꺼내서 한 줄씩 나열하는 명령어

'''

fhand = open('friends101.txt', 'r')
sentences = fhand.readlines()                                                     


lines = [item for item in sentences if re.match('[A-Z].+: ', item)]          # 대사만 뽑아내기
# print(lines)


'''
for item in sentences:
  # print('item',item)
  if re.match('[A-Z].+: ', item):
    print(item)
'''
  

# 특정 문자가 들어간 예문 찾기
 
would = [item for item in sentences if re.match('[A-Z].+: ', item) and re.search('would', item)]
for i in would:
  print(i)



# 특정 문자가 들어간 예문만 모아서 텍스트로 저장
newf = open('would.txt', 'w')
newf.writelines(would)
newf.close



maybe = [item for item in sentences if re.match('[A-Z].+: ', item) and re.search('maybe', item)]
print("maybe examples:", maybe)


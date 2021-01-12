import os
import re
import codecs

'''

3. 지문만 모으기
  
- 소문자 or .)
- (대소문자 공백)

'''

fhand = codecs.open('friends101.txt', 'r', 'utf-8')
script101 = fhand.read()

stuff = re.findall('\([A-Za-z].+[a-z|\.]\)', script101)
print(stuff)
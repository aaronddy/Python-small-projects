import os, re
import usecsv

os.chdir('C:\Learning\Python\eleven_projects_python\data_sources')

total = usecsv.opencsv('popSeoul.csv')
# print(len(total))


'''
1. list value와 index에 대해서


f = ['사과', '딸기', '바나나']
print(f[0])                      => 사과(value)
print(f.index('사과'))            => 0 (index number)

'사과' = '호박'
print(f)                         => ['사과', '딸기', '바나나'], 변동 X

f['사과'] = '호박'
print(f)                         => ['호박', '딸기', '바나나'], 변동 O

리스트의 값을 바꾸려면 index로 접근을 해야 값이 바뀜.

'''


i = total[1]

for j in i:
  
  '''
  print("j",j)                             => value (ex. '사과')
  print("i.index(j)", i.index(j))          => index number   (ex. 0)
  print("i[i.index(j)]", i[i.index(j)])    => 리스트의 인덱스로 접근한 값 (ex. f['사과'])
  '''

  if re.search('[a-z가-힣!]', j):
    i[i.index(j)] = j
  else:
    i[i.index(j)] = int(re.sub(',', '', j))
 
print(i)    
# ['Total', 9740398, 285529, 1468146]
    



'''
2. 예외처리로 오류 넘어가기 (try ~ catch statement)

조건문을 피하는 경우의 수에 예외처리로 대응하기


'
try:
  실행할 명령문

except:
  예외 처리 규정
'

'''


# '' 빈 문자열을 숫자형으로 바꾸려 할 때 오류 발생

p = ['123!!', '153,452', '11,032', '294', '0.034', '']

for i in p:

  try:
    '''
     if re.search('[a-z가-힣!]', i):
      p[p.index(i)] = i
    
     elif re.search('[0-9]\.', i):
      p[p.index(i)] = float(i)

     else:
      p[p.index(i)] = float(re.sub(',', '', i))

    ''' 
    p[p.index(i)] = float(re.sub(',', '', i))         
    # float() 함수가 오류를 일으키면 예외로 처리해 넘어가고, 일으키지 않는 경우에만 실수형으로 바꾸라고 명령 가능

  except:
    pass
    # 오류 발생하면 pass

print(p)



'''
3. 예외처리로 숫자만 골라서 숫자형으로 바꾸기


'''

# 리스트 하나만 가져와서 작동 체크

j = total[2]

for k in j:

  try:
    j[j.index(k)] = float(re.sub(',', '', k))

  except:
    pass

print(j)


# total 객체의 모든 리스트 가져와서 적용하기

for i in total:
  for j in i:
    try:
      i[i.index(j)] = float(re.sub(',', '', j))

    except:
      pass

  print("a list", i)
print("all", total)
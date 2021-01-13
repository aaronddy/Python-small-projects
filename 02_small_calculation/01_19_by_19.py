# object: n단 곱셈표 출력


# 1) 2단 곱셈표 출력
for i in range(1, 20):         
  # print(2 * i)
  print('2 X', i, '=', 2*i)

'range(시작할 정수, 끝나는 정수+1)'


# 2) 19단 곱셈표 출력
for i in range(2,20):
  for j in range(1,20):
    print(str(i), 'X', str(j), '=', i*j)
    print(i, 'X', j, '=', i*j)
    print('%d X %d = %d' %(i,j,i*j))



# 3) n*m단 곱셈표 출력
def n_multiple(n,m):
  for i in range(2,n):
    for j in range(1,m):
      print('%d X %d = %d' %(i,j,i*j))

print(n_multiple(5,10))


'None이 뜨는 이유를 모르겠다'
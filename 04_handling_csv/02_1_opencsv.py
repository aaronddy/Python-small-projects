import csv, os 

os.chdir('C:\Learning\Python')                     # 원하는 파일이 있는 path 이동
fhand = open('popSeoul.csv', 'r')                  # 해당 파일 open

read_file = csv.reader(fhand)                      # csv 파일 읽기
print(read_file)

for i in read_file:
  print(i)                                         # print lists of csv


'''
1. 해당 파일을 파이썬에서 사용할 수 있도록 csv형 리스트로 변경 ==> [[]]

csv 형태 자체로 사용하는 게 아니라 왜 파이썬으로 csv형 리스트로 변경하는 이유는?

    => csv형 리스트로 변경하면 파이썬 리스트의 기능을 활용해서 작업할 수 있는 작업이 무궁무진하기 때문. 
'''

csv_list = []

for i in read_file:
  csv_list.append(i)
  
print("csv_list:", csv_list)                        # [] 출력 


'''
csv.reader(fhand)로 해당 파일을 읽은 값을 read_fild에 저장하면서 커서가 맨 마지막으로 이동

2. seek() 함수를 이용해 커서를 처음으로 이동

'''

fhand.seek(0)

for i in read_file:
  csv_list.append(i)
  
print("csv_list_2:", csv_list)                      # 정상 출력



'3. 위의 작업을 수행하는 함수 opencsv 만들기'

def opencsv(file_name):
  fhand = open(file_name, 'r', encoding='utf-8')
  read_file = csv.reader(fhand)

  csv_list = []
  for lst in read_file:
    csv_list.append(lst)

  return "opencsv_working:", csv_list
  
  fhand.close()

# opencsv('popSeoul.csv')




import csv, os

os.chdir('C:\Learning\Python')

'1. opencsv 함수 이용해서 원하는 csv 파일 읽어오기'

def opencsv(file_name):
  fhand = open(file_name, 'r', encoding='utf-8')
  read_file = csv.reader(fhand)

  csv_list = []
  for lst in read_file:
    csv_list.append(lst)

  return "opencsv_working:", csv_list
  
  fhand.close()


# print(opencsv('popSeoul.csv'))



'2. popSeoul.csv를 file_obj 라는 새로운 객체에 저장'

file_obj = opencsv('popSeoul.csv')                                        # 새로운 파일에 들어갈 내용을 file_obj에 저장




'''
3. file_obj 이용해서 new_popSeoul.csv 파일 새로운 파일 생성

- csv.writer()는 CSV형 리스트를 파일에 쓸 수 있게 만들어 줌.
- CSV형 리스트가 저장된 객체를 파일에 쓸 때는 writerows()를 사용해 완성된 리스트 형태로 자료를 만든 후 한 번에 입력.
- newfile_csv내용을 new_popSeoul.csv에 넣기
'''

fhand = open('new_popSeoul.csv', 'w', newline='', encoding='utf-8')      # 새 csv 파일을 쓰기 모드로 fhand에 저장

csv_obj = csv.writer(fhand, delimiter=',')                               # fhand에 쓰기 모드, ','로 구분한 환경을 csv_obj에 저장

csv_obj.writerows(file_obj)                                              # csv_obj 환경에 file_obj 내용을 쓰기
fhand.close()




'4. 위의 작업을 수행하는 writecsv() 함수 생성하기'

def writecsv(file_name, file_obj): 
  # file_name은 만들 파일 이름이고, file_obj는 csv형 리스트를 저장한 객체

  with open(file_name, 'w', newline='', encoding='utf-8') as fhand:
    #파일을 바로 닫기 위해 with문 사용
    csv_obj = csv.writer(fhand, delimiter=',')
    csv_obj.writerows(file_obj)

'opencsv()와 writecsv() 함수를 합친 usecsv 모듈 만들어서 사용하기'


import csv, os

def opencsv(file_name):
  
  fhand = open(file_name, 'r', encoding='utf-8')
  read_file = csv.reader(fhand)

  csv_list = []
  for lst in read_file:
    csv_list.append(lst)

  return csv_list 


def writecsv(file_name, file_obj):

  with open(file_name, 'w', newline='', encoding='utf-8') as fhand:

    csv_obj = csv.writer(fhand, delimiter=',')
    csv_obj.writerows(file_obj)


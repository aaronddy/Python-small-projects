'usecsv 모듈 만들어서 사용하기'


import csv, os, re

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




def switch(list_name):
  
  for i in list_name:
    for j in i:
      try:
        i[i.index(j)] = float(re.sub(',', '', j))
        
      except:
        pass

  return list_name
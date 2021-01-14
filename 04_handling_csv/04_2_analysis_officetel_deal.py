import os, re, csv
import usecsv

os.chdir('C:\Learning\Python\eleven_projects_python\data_sources')


'1. data_sources폴더에서 오피스텔가격 csv 파일 불러서 CSV형 리스트로 전환 후(usecsv.opencsv_cp949), 문자형을 실수형으로 변경(usecsv.switch)'

fhand = usecsv.opencsv_cp949('officetel_price.csv')  
# print(fhand[:10])

officetel_info = usecsv.switch(fhand)
# print(officetel_info[:10])

print("count_deal:", len(officetel_info))
# 7667, 2020년 12월 한달 간 오피스텔 거래 수


'''
2. 슬라이싱으로 원하는 자료 출력하기


'''

# for i in officetel_info[:30]:
#   print(i[0], i[4], i[5], i[6], i[9], i[10])


'3. 궁금한 실거래 조건 검색해서 csv로 저장하기'

count = 0
the_officetel = []
print('내가 궁금한 실거래 조건')
print("오피스텔 헤더:", officetel_info[0])

for i in officetel_info:  

  try:
    
    if i[5] == '전세' and (i[6] >= 30 and i[6] <= 60) and re.search('성남', i[0]):
      count += 1
      the_officetel.append(i)
      print("officetel_info:", i)
      # print("total count:", count)
  
  except:
    pass

print(count)

usecsv.writecsv('the_future_house.csv', the_officetel)
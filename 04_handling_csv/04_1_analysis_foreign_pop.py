import os, re
import usecsv

os.chdir('C:\Learning\Python\eleven_projects_python\data_sources')

fhand = usecsv.opencsv('popSeoul.csv')
new_pop = usecsv.switch(fhand)
# print("new_pop",new_pop)



'1. 서울시 전체 외국인 비율 계산'

tot = new_pop[1]
ratio = (tot[2] / (tot[1]+tot[2])) * 100
f_ratio = round(ratio, 2)
# print("foreign_ratio:", f_ratio)




'''
2. 각 구의 외국인 비율 계산

- try ~ except 구문으로 문자열일 경우는 pass 예외처리 하기

for lst in new_pop:
  ratio = 0

  try:
    ratio = (lst[2] / (lst[1] + lst[2])) * 100
    f_ratio = round(ratio, 2)
    # print(lst[0], ":", f_ratio, "%")

  except:
    pass

'''



'3. 첫 행 지정하기'

new_table = [['Gu', 'Korean_pop', 'Foreign_pop', 'Foreign_ratio(%)']]

'''
new_table.append([tot[0], tot[1], tot[2], f_ratio])
print(new_table)
'''



'4. 외국인 비율이 3% 넘을 때만 출력하기'

for lst in new_pop:
  ratio = 0

  try:
    ratio = (lst[2] / (lst[1] + lst[2])) * 100
    f_ratio = round(ratio, 2)

    if f_ratio > 5.0:
      new_table.append([lst[0], lst[1], lst[2], f_ratio])
    
    print("write",new_table)

  except:
    pass



'5. writecsv로 저장'

usecsv.writecsv('foreign_table.csv', new_table)
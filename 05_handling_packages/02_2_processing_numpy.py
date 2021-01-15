import numpy as np
import usecsv, os

os.chdir('C:/Learning/Python/eleven_projects_python/data_sources')
quest_csv = usecsv.switch(usecsv.opencsv('quest.csv'))
print(quest_csv)
print("quest_csv type: list")

quest_array = np.array(quest_csv)
print(quest_array)
print("quest_array.dtype: float64, quest_array type: array(numpy)")


'quest_array에 조건 적용'

print('1. quest_array 원소들이 5보다 크면 True')
print(quest_array > 5)   

print("2. indexing 으로 조건에 맞는 index의 값만 가져오기")
print(quest_array[quest_array>4.5])

print("3. 해당 조건에 맞는 값들을 10으로 변경")
quest_array[quest_array>4.5] = 10
print(quest_array)

print("4. writecsv이용해서 csv로 저장")
usecsv.writecsv('new_quest_array.csv', list(quest_array))
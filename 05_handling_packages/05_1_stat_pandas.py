import re, os
import pandas as pd

os.chdir('C:/Learning/Python/eleven_projects_python/data_sources')
df = pd.read_csv('survey.csv')

print(df.head())
print('================')
print(df.describe())
print('================')


'1. 빈도 분석: value_counts()'
print(df.sex.value_counts())
print(df.income.value_counts())
print(df.stress.value_counts())


'2. 두 집단 평균 구하기: groupby()'
'df.groupby(그룹을 나누는 변수).연산'

print(df.groupby(df.sex).mean())
print(df.groupby(df.income).mean())
import pandas as pd
import re, os

os.chdir('C:/Learning/Python/eleven_projects_python/data_sources')

df = pd.read_csv('apt_comma.csv', encoding='cp949')
# print(df)

# print(df.가격 > 100000)     TypeError

df['가격'] = df['가격'].str.replace(',', '').astype('int64')
# print(df)

print(df[df.가격 > 30000][(df['건축년도'] > 2013)].sort_values(by='건축년도').loc[:, '가격'])
print(df[df.가격 > 30000][(df['건축년도'] > 2013)].loc[:, '가격'])
import pandas as pd
import re, os

os.chdir('C:/Learning/Python/eleven_projects_python/data_sources')

df = pd.read_csv('the_future_house.csv')
# print(len(df), df)



'1. 데이터 프레임 출력하기'

'''
print("head:\n", df.head())
print("tail:\n", df.tail())
print("시군구:\n", df.시군구)
'''

# print("면적 35 이상, 보증금 2억원 이하의 오피스텔 보증금 가격:\n", df['보증금(만원)'][(df['전용면적(㎡)'] > 35) & (df['보증금(만원)'] < 20000)])



'2. loc 사용하기'

'df.loc[원하는 행의 조건, 원하는 열의 조건]'
print(df.loc[10:20, :] [df['보증금(만원)'] < 30000])



'3. 새로운 값 추가'

df['단가'] = df['보증금(만원)'] / df['전용면적(㎡)']
print("단가 열 추가:", round(df, 2))


'4. 데이터 정렬(sorting)'
print(df.sort_values(by='단가') [(df['건축년도'] > 2010) & (df['보증금(만원)'] < 25000)])

print(df[df['보증금(만원)'] > 30000].sort_values(by='전용면적(㎡)', ascending = 'False').loc[:, ('단지명', '건축년도')])


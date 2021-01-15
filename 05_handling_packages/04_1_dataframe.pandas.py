import pandas as pd

data = {'name' : ['Mark', 'Jane', 'Chris', 'Ryan'], 'age' : [22, 34, 13, 54], 'score' : [89, 100, 78, 60]}
print(type(data))       # <class 'dict'>

df = pd.DataFrame(data)
# print(df)
print("types:",df.dtypes)

df['score'] = df['score'].astype(float)
print("change score column data type:\n", df['score'])


'sum(), mean() 사용해보기'

sum_df = df.sum()
print("sum_df:\n", sum_df)

mean_df = df.mean()
print("mean_df:\n", mean_df)


'특정 column 선택'
print(df['age'])
print(df.age)
import pandas as pd
import os,sys

def basePath():
  return os.path.dirname(os.path.abspath(sys.argv[0]))

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df.set_index('PassengerId', inplace=True)

print(df.columns)
print()
print(df.loc[[1,2], ['Name', 'Sex', 'Age', 'Survived']])
print()
print(df.loc[1:5])
print()
print(df.loc[1:7:2, ['Name','Sex','Age', 'Survived']])
print()
print(df.query('(Age > 50 | Age < 20) & Sex=="male"').head(10))
df.to_csv(f'{basePath()}/dataset.csv',sep=';',index=False, encoding='utf-8-sig')
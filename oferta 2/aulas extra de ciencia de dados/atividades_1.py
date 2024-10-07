import pandas as pd
import os, sys

archives = []

def basePath():
  return os.path.dirname(os.path.abspath(sys.argv[0]))

def Save(query, nome):
  parameter = df.query(query)
  try:
    parameter.to_csv(f'{basePath()}/datasets/{nome}', sep=';',index=False, encoding='utf-8-sig')
  except Exception as err:
    print("erro: ", err)

df = pd.read_csv(f'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df.set_index('PassengerId', inplace=True)

# Quantas crianças abaixo de 10 anos sobreviveram?

Save(query='Age < 10 & Survived==1', nome='underten.csv')

# Quantas mulheres sobreviveram?

Save(query='Sex=="female" & Survived==1', nome='women.csv')

# Quantos homens sobreviveram?

Save(query='Sex=="male" & Survived==1', nome='men.csv')

# Quantos idosos acima de 50 anos sobreviveram?

Save(query='Age > 50 & Survived==1', nome='eldery.csv')

# Quantas crianças abaixo de 12 anos do sexo feminnino sobreviveram?

Save(query='Age < 12 & Sex=="female"', nome='children.csv')
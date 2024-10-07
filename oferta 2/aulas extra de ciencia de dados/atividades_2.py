import pandas as pd
from atividades_1 import basePath
import matplotlib.pyplot as plt

df = pd.read_csv(f'{basePath()}/datasets/all_seasons.csv')
plt.xlabel("Peso")
plt.ylabel("Altura")
altura = df.loc[0:11145,['player_height']]
peso = df.loc[0:11145,['player_weight']]

plt.scatter(peso, altura)
plt.show()
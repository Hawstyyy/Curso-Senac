import matplotlib.pyplot as plt
import requests
import pandas as pd

cidades = {1:'campo-grande',2:'tres-lagoas',3:'dourados',4:'corumba',5:'ponta-pora'}

for key,value in cidades.items():
  request = requests.get(f'https://cdn-apuracao.estadao.com.br/2024/apuracao/primeiro-turno/prefeito/ms/{value}.json').json()
  df = pd.DataFrame(request['candidatos'])

  candidatos = df.loc[0:30 ,['nome','votos']]

  nome = candidatos['nome'].tolist()
  votos = candidatos['votos'].tolist()
  print(votos)

  plt.subplot(1, 6, key)
  plt.pie(votos, labels=nome, autopct='%.1f%%', pctdistance=0.8)
  plt.subplot(3,6,key)
  plt.bar(height=nome, x=votos)

cg = requests.get('https://cdn-apuracao.estadao.com.br/2024/apuracao/primeiro-turno/vereador/ms/campo-grande.json').json()
df_cg = pd.DataFrame(cg['candidatos'])

candidatos_cg = df_cg.loc[0:30 ,['nome','votos']]

nome = candidatos_cg['nome'].tolist()
votos = candidatos_cg['votos'].tolist()

plt.subplot(1, 6, 6)
plt.pie(votos, labels=nome, autopct='%.1f%%', pctdistance=0.8)
plt.subplot(3, 6, 6)
plt.bar(height=nome, x=votos)

plt.show()
# Crie um dado. A função deve sortear um número aleatório de 1 até 6. Agora, faça
# com que o dado seja lançado 100 vezes, mil vezes e 1 milhão de vezes. Armazene o valor
# que ele forneceu em cada lançamento e mostre quantas vezes cada número foi sorteado.
# Compare os resultados com a estatística.

import random

def dado(n):
  dado = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
  stat = {}

  for i in range(n):
    choice,value = random.choice(list(dado.items()))
    if choice in dado:
      dado[choice] += 1

  for key,value in dado.items():
    stat[key] = ((value/n) * 100)

  print(f"- A rolagem de cada número foi: ")
  for key, value in dado.items():
    print(f"- {key} foi rolado {value} vezes")
  
  print("\n- E as estatísticas foram: ")
  for key,value in stat.items():
    print(f"- {key} = {value}%")

dado(1000)
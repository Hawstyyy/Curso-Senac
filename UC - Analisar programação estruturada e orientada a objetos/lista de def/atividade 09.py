# Crie um programa que
# determine se a soma do número escolhido com um número aleatório é par ou ímpar.

import random
import sys

def par_impar(n):
  num_aleatorio = random.randint(1,sys.maxsize)
  soma = num_aleatorio + n

  if soma % 2 == 0:
    print(f"- Este número {n} somado com {num_aleatorio} é par! soma = {soma}")
  else:
    print(f"- Este número {n} somado com {num_aleatorio} é impar! soma = {soma}")

par_impar(int(input("\n- Insira um número para somar com um número aleatório e verificar se é par ou impar: ")))
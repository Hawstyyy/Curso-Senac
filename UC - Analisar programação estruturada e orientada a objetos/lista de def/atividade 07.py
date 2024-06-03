# Faça um programa para lançar uma moeda. Quando chamamos uma função, ela deve
# retornar “cara” ou “coroa”. Em outra função, faça ‘n’ lançamentos de moedas (onde ‘n’ é o
# valor que o usuário quiser) e mostre a porcentagem de vezes que deu cara e Coroa. O que
# tende a acontecer se você jogar a moeda 10, 100, 1000 ou um milhão de vezes?

import random
import time

def cara_ou_coroa_por(n):
  coroa = 0
  cara = 0
  moeda = ['Cara', 'Coroa']

  for i in range(n):
    select = random.choice(moeda)
    if select == 'Coroa':
      coroa += 1
    else:
      cara += 1
  cara_porc = (cara*100)/n
  coroa_porc = (coroa*100)/n
  print(f"- E a porcentagem das jogadas foram de: {cara_porc}% cara e {coroa_porc}% coroa")

def cara_ou_coroa(n):
  moeda = ['Cara', 'Coroa']

  for i in range(n):
    select = random.choice(moeda)
  print(f"- De {n} jogadas a moeda caiu em: {select}")

print("\n#------------------------- Cara ou Coroa -------------------------#")
n = int(input("\n- Insira quantas vezes quer jogar a moeda: "))

print("\ncarregando...\n")
time.sleep(1)

cara_ou_coroa(n)
cara_ou_coroa_por(n)
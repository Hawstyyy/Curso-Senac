# Crie um dicionário com palavras e suas definições. O programa deve escolher
# uma palavra aleatória e pedir ao usuário para adivinhar seu significado.
import random

dicionario = {
    "Python":'linguagem de programação',
    "Girafa": "um animal de pescoço longo",
    "Melancia": "uma fruta grande",
    "Algoritmo": "uma lista de instruções",
    "Astronomia": "a ciência que estuda os astros"}

escolha = key, value = random.choice(list(dicionario.items()))

while True:
  adivinha = input(f"\n- A palavra escolhida foi: {key}. Qual seu significado? ")
  if adivinha == value:
    print(f"\n- Correto! a palavra {key} tem o significado de: {value}\n")
    break
  else:
    print("\n- !errado!\n")
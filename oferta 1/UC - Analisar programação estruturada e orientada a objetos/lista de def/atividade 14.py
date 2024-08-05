# Escreva uma função que recebe uma string e conta quantas vogais (a, e, i, o, u) ela contém.

def vogais_counter(palavra):
  vogais = {"a":0,"e":0,"i":0,"o":0,"u":0}

  for i in palavra.lower():
    if i in vogais:
      vogais[i] += 1

  print(f"\n- A palavra \"{palavra}\" tem a seguinte quantidade de cada vogal: \n")
  for key,value in vogais.items():
    print(f"- {key} = {value}")
  print()

vogais_counter(input("\n- Insira a palavra que gostaria de contar as vogais: "))


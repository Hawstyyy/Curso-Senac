# 4 – Faça um algoritmo que receba uma lista com 10 elementos. O algoritmo deve remover o
# elemento 8 e mostrar a lista após a remoção. O exercício deve ser feito sem utilizar as funções do
# Python de remoção.

numeros = input("\n- Insira seus números desejados, separados por,: ").split(",")
lista = []

for x in numeros:
  if x == '8':
    continue
  else:
    lista.append(x)

print(lista)
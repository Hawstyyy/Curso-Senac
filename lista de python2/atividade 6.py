# Faça um programa que imprima na tela os números de 1 a 20, um
# abaixo do outro. Depois modifique o programa para que ele mostre os
# números um ao lado do outro.

lista = []

for x in range (1,21):
  print(x)
  lista.append(str(x))

print(", ".join(lista))
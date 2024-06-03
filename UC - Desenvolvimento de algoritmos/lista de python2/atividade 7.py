# Faça um programa que leia 5 números e informe o maior número

numeros = []

for x in range(1,6):
  numeros.append(float(input(f'Insira o seu {x}° número: ')))
print(max(numeros))
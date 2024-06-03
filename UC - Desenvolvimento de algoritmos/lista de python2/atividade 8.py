# Faça um programa que leia 5 números e informe a soma e a média
# dos números. 

numeros = []
soma = 0

for x in range(1,6):
  numeros.append(float(input(f'Insira o seu {x}° número: ')))

for i in numeros:
  soma += i

print(f"A média dos numeros {numeros} será de:", soma/5)
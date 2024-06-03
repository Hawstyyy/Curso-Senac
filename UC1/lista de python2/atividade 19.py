# Faça um programa que, dado um conjunto de N números, determine
# o menor valor, o maior valor e a soma dos valores. 

numeros = []
numero = 0
soma = 0

while True:
  numero = int(input("Insira seus números, digite 0 para sair: "))

  if numero == 0:
    print(numeros)
    break
  
  numeros.append(numero)

for x in numeros:
  soma += x

print(f"""
- O menor valor da lista foi: {min(numeros)}.
- O maior valor da lista foi: {max(numeros)}.
- A soma de todos os valores da lista foi de: {soma}.
\n""")
# Encontrar números primos é uma tarefa difícil. Faça um programa 
# que gera uma lista dos números primos existentes entre 1 e um número 
# inteiro informado pelo usuário. 

num = int(input("\n- Insira o número que deseja verificar: "))
primo = []

for x in range(1,(num//2)+1):
    if not num % x == 0:
      primo.append(str(x))
    else:
      continue

print(primo)
# Encontrar números primos é uma tarefa difícil. Faça um programa 
# que gera uma lista dos números primos existentes entre 1 e um número 
# inteiro informado pelo usuário. 

num = int(input("\n- Insira o número que deseja verificar: "))
div = []

for x in range(1,num+1):

  if  % x == 0:
    continue
  else:
    div.append(str(x))

print(div)
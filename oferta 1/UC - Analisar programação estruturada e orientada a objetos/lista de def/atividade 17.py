# Escreva uma função que recebe um número inteiro positivo ‘n’ e retorna a soma de todos
# os números pares de 1 até ‘n’.

def soma_par(n):
  soma = 0
  for i in range(1,n+1):
    if i % 2 == 0:
      soma += i
  print(f"\n- As somas dos números pares até {n} será de: {soma}")

soma_par(int(input("\n- Insira um número inteiro para fazermos as somas dos pares: ")))
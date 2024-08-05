# Escreva uma função que recebe um número inteiro e retorna a soma de seus dígitos. Por
# exemplo, se o número for 123, a função deve retornar 6 (1 + 2 + 3).

def soma_digitos(n):
  alg = 0
  for i in str(n):
    alg += int(i)
  
  print(f"\n- a soma dos digitos do número {n} será: {" + ".join(i for i in str(n))} = {alg}")

soma_digitos(int(input("\n- Insira um número para somarmos os seus digitos: ")))
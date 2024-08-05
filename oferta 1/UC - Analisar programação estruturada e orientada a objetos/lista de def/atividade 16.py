# Faça um programa que verifica se um número é primo. Um número é primo se ele não
# possui divisores além de 1 e ele mesmo.

def primo_ou_n(n):
  primo = 0
  for i in range(1,n+1):
    if n % i == 0:
      primo += 1
    else:
      continue
  if primo == 2:
    print(f"- O {n} número é primo")
  else:
    print(f"- O número {n} não é primo")

primo_ou_n(int(input("\n- Insira um número inteiro: ")))
# Um número é dito ser perfeito quando ele é igual à soma de seus divisores. Por exemplo, o
# seis é perfeito, pois: 6=1+2+3
# Crie um programa que pede um número ao usuário e diga se ele é perfeito ou não.

def perfeito(n):
  divisor = 0
  for i in range(n):
    if i == 0:
      continue
    elif n % i == 0:
      divisor += i
  if n == divisor:
    print(f"\n- O número {n} é perfeito!")
  else:
    print(f"\n- O número {n} não é perfeito!")

perfeito(int(input("\n- Insira o número que deseja ver se é perfeito ou não: ")))
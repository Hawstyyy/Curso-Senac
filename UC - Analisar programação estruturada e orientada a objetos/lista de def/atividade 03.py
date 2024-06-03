# Faça um programa que peça um número inteiro positivo ‘n’ ao usuário e imprima um
# quadrado de lado ‘n’ preenchido com hashtags.

def quadrado(n):
  for i in range(n):
    print("#"*n)

quadrado(int(input("\n- Insira o número que deseja transformar em quadrado de hashtag: ")))
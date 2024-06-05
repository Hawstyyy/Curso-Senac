# Crie um programa que recebe um número inteiro positivo ‘n’ e calcula o fatorial desse
# número. O fatorial de ‘n’ é o produto de todos os números inteiros positivos de 1 até ‘n’.
# Por exemplo, 5!=5⋅4⋅3⋅2⋅1=120

def fatorial(n):
  numero = []
  res = 1

  for i in range(n,0,-1):
    numero.append(i)
  
  for i in numero:
    res *= i
  
  print(f"""\n- O fatorial no número {n} é: 
{n} != {" * ".join(str(i) for i in numero)} = {res}""")

n = int(input("\n- Insira o número que deseja fatorar: "))
fatorial(n)
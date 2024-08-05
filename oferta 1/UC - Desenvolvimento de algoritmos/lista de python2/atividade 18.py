# Faça um programa que calcule o fatorial de um número inteiro
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120 

n = int(input("\n- Qual o número que deseja fatorar? "))
numero = []
multi = 1

for i in range(1, n+1):
  numero.append(i)

for i in numero:
  multi *= i

numero.reverse()

print(f"""
- O fatorial da lista: {numero}
- será de: {multi}""")
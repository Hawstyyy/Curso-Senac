# Faça um programa que calcule o fatorial de um número inteiro 
# fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input("\n- Qual o número que deseja fatorar? "))
numero = []
multi = 1
numero_str = []

for i in range(1, n+1):
  numero.append(i)

for i in numero:
  multi *= i

for x in numero:
  numero_str.append(str(x))

numero_str.reverse()

print(f"""
- O fatorial de: {n}
- 5! = {" . ".join(numero_str)} = {multi}""")
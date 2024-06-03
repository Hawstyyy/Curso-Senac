# Altere o programa de cálculo do fatorial, permitindo ao usuário
# calcular o fatorial várias vezes e limitando o fatorial a números inteiros
# positivos e menores que 16.

while True:
  n = int(input("\n- Qual o número que deseja fatorar? "))

  if n > 16 or n < 0:
    print("Erro")

  else:
    break
  
numero = []
multi = 1

while True:
  for i in range(1, n+1):
    numero.append(i)

  for i in numero:
    multi *= i

  print(f"""
  - O fatorial da lista: {numero}
  - será de: {multi}""")
  coiso = input("Deseja continuar? ").capitalize()
  if coiso == "N":
    break
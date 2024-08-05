# Faça um programa que peça um número inteiro e determine se ele é
# ou não um número primo. Um número primo é aquele que é divisível
# somente por ele mesmo e por 1. 

primo = []

while True:
  try:
    num = int(input("\nInsira o seu número que deseja descobrir se é primo: "))
    break
  except:
    print("!!!!!!!!!! Número inválido !!!!!!!!!!")

for i in range(1,num+1):
  if num % i == 0 and num % num == 0:
    primo.append(i)

if len(primo) == 2:
  print(f"\n- O número {num} é primo\n")

else:
  print(f"\n- O número {num} não é primo\n")
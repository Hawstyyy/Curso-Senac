# Altere o programa de cálculo dos números primos, informando, caso
# o número não seja primo, por quais número ele é divisível. 

primo = []

while True:
  try:
    num = int(input("\nInsira o seu número que deseja descobrir se é primo: "))
    break
  except:
    print("!!!!!!!!!! Número inválido !!!!!!!!!!")

for i in range(1,num+1):
  if num % i == 0:
    primo.append(i)

if len(primo) == 2:
  print(f"\n- O número {num} é primo\n")

else:
  print(f"""
\n- O número {num} não é primo, mas ele é divisivel pelos seguintes números:
{primo}""")
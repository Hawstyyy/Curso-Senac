# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de
# qualquer número inteiro entre 1 a 10. O usuário deve informar de qual
# numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo
# abaixo: 

while True:
  try:
    tabuada = int(input("\nInsira o número que deseja ver a tabuada: "))
    numero = int(input("\nInsira até onde quer ver a tabuada: "))
    break
  except:
    print("\n!!!!!!!!!!!!!!!!!!!!! Número inválido !!!!!!!!!!!!!!!!!!!!!")

for x in range(1, numero + 1):
  r = tabuada * x
  print(f"\n{tabuada} x {x} = {r}")

print()
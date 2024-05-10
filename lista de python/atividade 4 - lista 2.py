numeros = input("Insira seus números desejados para verificarmos a ordem: ").split(",")

while True:
  try:
    num, num2, num3 = int(numeros[0]), int(numeros[1]), int(numeros[2])
    break
  except:
    numeros = input("Algum número é inválido ou faltante, tente de novo: ").split(",")

if num < num2 and num2 < num3:
  listafinal = str(numeros).replace("[", "").replace("]", "")
  print(f"A sequência de números: {listafinal} , está em ordem crescente!")
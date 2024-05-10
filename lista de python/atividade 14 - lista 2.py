numeros = input("Insira seus números desejados para verificarmos a ordem: ").split(",")

num, num2, num3 = int(numeros[0]), int(numeros[1]), int(numeros[2])

if num < num2 and num2 < num3:
  listafinal = str(numeros).replace("[", "").replace("]", "")
  print(f"A sequência de números, está em ordem crescente!")
else:
  listafinal = str(numeros).replace("[", "").replace("]", "")
  print(f"A sequência de números, não está em ordem crescente!")
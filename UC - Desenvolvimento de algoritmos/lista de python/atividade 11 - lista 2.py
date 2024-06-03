while True:
  numero = int(input("Insira o número desejado para identificar se é par ou ímpar: "))

  if numero < 0:
    print("O número é inválido")

  elif numero % 2 == 0:
    print(f"O número {numero} é par")
    break

  else:
    print(f"O número {numero} é ímpar")
    break
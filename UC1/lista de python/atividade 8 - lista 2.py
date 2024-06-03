while True:
  numero = int(input("Insira o seu número para ver a raiz quadrada: "))

  if numero > 0:
    r = numero ** (1/2)
    print(f"O resultado da raiz quadrada será de: {r}")
    break
  else:
    print("O número inserido é inválido")
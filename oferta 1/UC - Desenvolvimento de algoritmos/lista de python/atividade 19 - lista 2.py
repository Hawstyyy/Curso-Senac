numero = str(0)
while numero == "0":
  numero = input("Insira o número desejado acima de zero: ")

  if numero[0] == "0" or numero[0] == "-":
    print("Número inválido")

  i = 0
  soma = 0

  while i < len(numero):
    soma += int(numero[i])
    i += 1

  print(f"A soma dos algarismos do número {numero} será: {soma}")

while True:
  try:
    numero = int(input("Insira seu número inteiro: "))
    break
  except:
    print("Inválido")

if numero > 10:
  print(f"O número \"{numero}\" maior que 10")
else:
  print(f"O número \"{numero}\" não é maior que 10")
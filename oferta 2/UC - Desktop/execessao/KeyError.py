dict = { 0:1 }

for key, value in dict.items():
  print(f"| Chave = {key} - Valor = {value}")

while True:
  choice = int(input("- insira a chave que gostaria de acessar: "))
  try:
    dict[choice]
    print("Acessada!")
  except KeyError:
    print("Chave fora do dicionário")
valor = float(input("Insira o valor do objeto: "))
estado = input("Pra qual estado quer mandar: ")

estado = estado.upper()

if estado == "MG":
  taxa = 7
elif estado == "SP":
  taxa = 12
elif estado == "RJ":
  taxa = 15
elif estado == "MS":
  taxa = 8
else:
  print("Estado inválido")

taxafinal = (valor * taxa) / 100
valor += taxafinal

print(f"O valor do produto com a taxa será de: R$ {valor}")
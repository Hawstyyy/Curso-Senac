numero = []
for i in range (1, 11):
  numero.append(int(input("Insira seu número: ")))
for numeros in numero:
  r = numeros ** 2
  print(f"{numeros}² tem o resultado de: {r}")
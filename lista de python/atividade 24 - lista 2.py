base_maior = float(input("Insira a base maior do trapézio: "))

while base_maior < 0:
  print("Número inválido")
  base_maior = float(input("Insira a base maior do trapézio: "))

base_menor = float(input("Insira a base menor do trapézio: "))

while base_menor < 0:
  print("Número inválido")
  base_menor = float(input("Insira a base menor do trapézio: "))

altura = float(input("Insira a altura do trapézio: "))

while altura < 0:
  print("Número inválido")
  altura = float(input("Insira a altura do trapézio: "))

area = ((base_maior + base_menor) * altura) / 2

print(f"A área do trapézio será de: {area}")
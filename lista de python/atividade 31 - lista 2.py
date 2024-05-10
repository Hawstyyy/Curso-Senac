km = float(input("Insira a quantidade de kilometros percorridos no percurso: "))
litros = float(input("Insira a quantidade de litros consumidos por todo o percurso: "))

gasto = km/litros

if gasto < 8:
  print("Venda o carro!")
elif gasto > 8 and gasto < 14:
  print("Econômico!")
else:
  print("Super econômico!")
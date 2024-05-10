lista = []
somaposi = 0
somaneg = 0

for cont in range(10):
  lista.append(int(input("insira numero: ")))

for i in lista:
  if i < 0:
    somaneg += 1
  else:
    somaposi += 1

print(f"""
      + - - - - - - - - - - - - - - - - - - - - - - -
      | Total de números negativos: {somaneg}
      | Total de Números postiivos: {somaposi}
      + - - - - - - - - - - - - - - - - - - - - - - -
""")
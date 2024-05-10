valor = float(input("Insira o valor de aquisição da peça: "))

if valor < 50.00:
  porcentagem = ( valor * 45 ) / 100
  valor += porcentagem
  print(f"O valor final da peça será de: {valor}")
else:
  print(f"O valor final da peça será de: {valor}")
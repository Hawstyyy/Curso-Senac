custo = float(input("Insira o custo da fábrica: "))

if custo <= 12000.00:
  porcentagem = (custo * 5) / 100
  custofinal = custo + porcentagem
  print(f"O custo ao consumidor será de: R${custofinal}, e não haverá acréscimo de imposto")

elif custo > 12000 and custo <= 25000:
  porcentagem = (custo * 10) / 100
  imposto = (custo * 15) / 100
  custofinal = custo + porcentagem + imposto
  print(f"O custo ao consumidor será de: R${custofinal}, com acréscimo de imposto")

else:
  porcentagem = (custo * 15) / 100
  imposto = (custo * 20) / 100
  custofinal = custo + porcentagem + imposto
  print(f"O custo ao consumidor será de: R${custofinal}, com acréscimo de imposto")
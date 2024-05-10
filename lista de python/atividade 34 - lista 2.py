antigo = float(input("Insira o preço antigo do produto: "))

if antigo <= 50.00:
  taxa = (antigo * 5) / 100
  novo = antigo + taxa
  print(f"O novo preço devera ser de R${novo}")

elif antigo > 50.00 and antigo < 100.00:
  taxa = (antigo * 10) / 100
  novo = antigo + taxa
  print(f"O novo preço devera ser de R${novo}")

else:
  taxa = (antigo * 15) / 100
  novo = antigo + taxa
  print(f"O novo preço devera ser de R${novo}")
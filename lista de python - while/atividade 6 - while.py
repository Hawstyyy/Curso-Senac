controle = 0
valor = 1
total = 0
preco = 0

while valor != controle:
  print ("""Tabela de valores:
         100 - Refrigerante (R$ 6.00)
         101 - Salgados (R$ 5.00)
         102 - Cigarro (R$ 7.00)
         103 - Cerveja (R$ 4.50)""")
  
  total += preco
  print(f"\n\n-  O total da compra até o momento é: R$ {total}")
  valor = int(input("\nInsira o valor dos produtos ou digite 0 para encerrar a compra: "))

  if valor == 100:
    preco = 6.00
  elif valor == 101:
    preco = 5.00
  elif valor == 102:
    preco = 7.00
  elif valor == 103:
    preco = 4.50

pagamento = float(input("Insira a nota que foi fornecido no pagamento: "))
troco = pagamento - total
print(total)

print(f"O troco deverá ser: R${troco}")
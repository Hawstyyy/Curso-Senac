codigo, quantidade = input("Insira o código do produto e a sua quantia: ").split(",")

if codigo == "100":
  produto = "Hot Dog"
  preco = 12.00

elif codigo == "102":
  produto = "X-Salada"
  preco = 18.50

elif codigo == "103":
  produto = "X-BACON"
  preco = 25.50

elif codigo == "104":
  produto = "X-Burguer"
  preco = 17.00

elif codigo == "105":
  produto = "Suco de Laranja"
  preco = 9.50

elif codigo == "106":
  produto = "Refrigerante"
  preco = 6.00

quantidade = int(quantidade)

precofinal = preco * quantidade

print(f"O preço a pagar do pedido {produto} com {quantidade} quantidades, será de: R${precofinal}")
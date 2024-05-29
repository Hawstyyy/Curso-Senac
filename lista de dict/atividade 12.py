# Crie um programa que simule um carrinho de compras. O usuário pode adicionar
# produtos (com nome e preço) ao carrinho e, no final, exiba o total da compra

carrinho = {}
produtos = {
  'Carne': 8.00,
  'Papel higienico': 12.00,
  'Sofa': 800.00
}
total = 0

while True:
  print("\n+---------------------------------------------------------------------------+")
  for key,value in produtos.items():
    print(f"- {key} - preço: {value}")
  print("+---------------------------------------------------------------------------+")
  print(f"Carrinho - {carrinho}")

  nome = input("\n- Insira o nome do produto: ").capitalize()

  for key,value in produtos.items():
    if nome in key:
      carrinho.update({key:value})
      print("\n--------------------! Pedido adicionado !--------------------\n")
      break

  saida = input("- Deseja realizar o pagamento? (S/N) ").capitalize()
  if saida == "S":
    break

for key,value in carrinho.items():
  total += value

print(f"\n- O preço total da compra foi: R${total}\n")
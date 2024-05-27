# Crie um dicionário para controlar o estoque de produtos em uma loja. Permita
# adicionar, remover e atualizar a quantidade de cada produto.
produtos = {'Caderno': 0, 'Caneta':0}

while True:
  print("""
+----------------------------------------+""")
  for key, value in produtos.items():
    print(f"| {key} - {value}")
  print("+----------------------------------------+")

  controle = input("""
+----------------------------------------+
| A - Adicionar quantidade de produtos   |
| R - Remover quantidade de produtos     |
| ATT - Atualizar quantidade de produtos |
+----------------------------------------+
- """).upper()

  if controle == "A":
    nome = input("\n- Insira o nome do produto: ").capitalize()

    for i in produtos:
      if nome in i:
        add = int(input("- Insira a quantidade que deseja adicionar: "))
        produtos.update({nome:add})
        break
      else:
        print("-! O produto não existe no estoque !-")
        break
  
  elif controle == "R":
    nome = input("\n- Insira o nome do produto: ").capitalize()

    for key, value in produtos.items():
      if nome in key:
        rev = int(input("- Insira a quantidade que deseja remover: "))
        sub = int(value) - rev
        produtos.update({nome:sub})
        break
      else:
        print("-! O produto não existe no estoque !-")
        break
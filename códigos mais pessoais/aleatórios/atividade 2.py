estoque = []

while True:
  print()
  for produto in estoque:
    print(f"| Nome: {produto[0]} - Quantidade: {produto[1]}")

  try:
    choice = int(input(("""
- 1 - Adicionar estoque
- 2 - Remover estoque
- 3 - Exibir estoque
- 4 - Sair
    - """)))
  except:
    print("- Escolha inválida")
  
  if choice == 1:
    try:
      nome = input("- Insira o nome do produto: ").capitalize()
    except:
      print("- Não insira números")
    try:
      quantidade = int(input("- Insira a quantidade do produto: "))
    except:
      print("- Insira um valor, não uma letra")
    estoque.append([nome, quantidade])
  
  elif choice == 2:
    print()
    for produto in estoque: 
      print(f"| Nome: {produto[0]} - Quantidade: {produto[1]}")
    try:
      nome = input("\n- Insira o nome do produto: ").capitalize()
    except:
      print("- Não insira números")
    i = 0
    for produto in estoque:
      if produto[0] == nome:
        break
      i += 1
    del estoque[i]

  elif choice == 3:
    for produto in estoque:
      print(f"| Nome: {produto[0]} - Quantidade: {produto[1]}")
  
  elif choice == 4:
    break

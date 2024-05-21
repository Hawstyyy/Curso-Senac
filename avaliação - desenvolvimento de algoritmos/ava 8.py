func_log = ['1', '1','1', '1']
carrinho = []
preco = 0.00
produtos = [
  ['Alimentos', 'Frios', '0', 'Carne', 8.00, 'Pedaço de carne de vaca'],
  ['Higiene', 'Pessoal', '1', 'Papel higienico', 12.00, 'Papel para higienização'],
  ['Movéis', 'Casa', '2', 'Sofa', 800.00, 'Sofá para aconchego'],
  ]

while True:
  ator = input("""
  +===================================================+
  |                 Bem-Vindo ao mercado!             |
  +===================================================+
  | C - Cadastro ou login de cliente                   |
  | F - Login de funcionário                          |
  +===================================================+
    - """)

  if ator == "C" or ator == "c":
    print("\n!!!!!!!!!!!!!!!!! Bem - vindo cliente !!!!!!!!!!!!!!!!!\n")
    nome_cliente = input("- Insira seu nome completo: ")
    cpf = input("- Insira o seu cpf: ")
    break

  elif ator == "F" or ator == "f":
    print("\n!!!!!!!!!!!!!!!!! Bem - vindo funcionário !!!!!!!!!!!!!!!!!\n")
    nome_f = input("- Insira o seu nome completo: ")
    matricula = input("- Insira a sua matrícula: ")
    nasc = input("- Insira a sua data de nascimento: ")
    cpf_f = input("- Insira o seu cpf: ")

    if nome_f == func_log[0] and matricula == func_log[1] and nasc == func_log[2] and cpf_f == func_log[3]:
      print("\n!-! Login realizado com sucesso !-!\n")
      login = True
      break
    else:
      print("\n!-! Login incorreto !-!\n")

if ator == "F" or ator == "f" and login == True:
  while True:
    op_func = input("""
+==========================================+
| E - Entrada no estoque                   |
| R - Relatório do estoque                 |
| P - Atualizar preço de produto           |
| X - Sair                                 |
+==========================================+

    - """)
    if op_func == "E" or op_func == "e":
      print("+---------------------------------------------------------------------------+")
      for x in produtos:
        print(f" - Sessão: {x[0]}")
        print(f" -- Subcategoria: {x[1]}")
        print(f" ---- Produto: ({x[2]}) - {x[3]} - R${x[4]:.2f} - desc:{x[5]}")
        print("+---------------------------------------------------------------------------+")
      
      sessao = input("\n- Insira o nome da sessão: ")
      categoria = input("- Insira o nome da categoria: ")
      codigo = input("- Insira o codigo do produto: ")
      tem = False
      for i in produtos:
        if i[2] == codigo:
          tem = True
      if not tem:
        produto = input("- Insira o nome do produto: ")
        preco = float(input("- Insira o preço do produto: "))
        desc = input("- Insira uma pequena descrição do produto: ")
        produtos.append([sessao, categoria, codigo, produto, preco, desc])
      else:
        print("- O código do produto já existe no estoque")


    elif op_func == "R" or op_func == "r":
      print("+---------------------------------------------------------------------------+")
      for x in produtos:
        print(f" - Sessão: {x[0]}")
        print(f" -- Subcategoria: {x[1]}")
        print(f" ---- Produto: ({x[2]}) - {x[3]} - R${x[4]:.2f} - desc:{x[5]}")
        print("+---------------------------------------------------------------------------+")

    elif op_func == "P" or op_func == "p":
      print("+---------------------------------------------------------------------------+")
      for x in produtos:
        print(f" - Sessão: {x[0]}")
        print(f" -- Subcategoria: {x[1]}")
        print(f" ---- Produto: ({x[2]}) - {x[3]} - R${x[4]:.2f} - desc:{x[5]}")
        print("+---------------------------------------------------------------------------+")
      
      sessao = input("\n- Insira o nome da sessão: ")
      categoria = input("- Insira o nome da categoria: ").capitalize()
      codigo = input("- Insira o codigo do produto: ")
      tem = False
      for i in produtos:
        if i[0] == sessao or i[1] == categoria or i[2] == codigo:
          tem = True
          preco = float(input(f"- Insira o novo preço ({i[4]}): "))
          i[4] = preco
      if not tem:
        print("- O código do produto não existe no estoque")

    elif op_func == "X" or op_func == "x":
      print("\n!!!!!!!!!!!!!!!!!! Programa encerrado !!!!!!!!!!!!!!!!!!\n")
      break

if ator == "C" or ator == "c":
  while True:
    print("\n+---------------------------------------------------------------------------+")
    for x in produtos:
      print(f" - Sessão: {x[0]}")
      print(f" -- Subcategoria: {x[1]}")
      print(f" ---- Produto: {x[3]} - R${x[4]:.2f} - desc:{x[5]}")
      print("+---------------------------------------------------------------------------+")

    print(f"Carrinho: {carrinho}")

    nome = input("\n- Insira o nome do produto: ").capitalize()
    if len(carrinho) > 0:
      for i in carrinho:
        if i == nome:
          rev = input("\n- Deseja Remover esse item? (S/N) ").capitalize()
          if rev == "S":
            for x in produtos:
              if x[3] == nome:
                carrinho.remove(nome)
                print("\n--------------------! Pedido removido !--------------------\n")
                break
          else:
            for x in produtos:
              if x[3] == nome:
                carrinho.append(nome)
                print("\n--------------------! Pedido adicionado !--------------------\n")
                break
    else:
      for x in produtos:
        if x[3] == nome:
          carrinho.append(nome)
          print("\n--------------------! Pedido adicionado !--------------------\n")
          break
    saida = input("- Deseja realizar o pagamento? (S/N) ").capitalize()
    if saida == "S":
      break
    else: 
      continue
  for i in carrinho:
    for x in produtos:
      if i == x[3]:
        preco += x[4]
  imposto_nacional = (preco * 5) / 100
  imposto_estadual = (preco * 8) / 100
  imposto_municipal = (preco * 12) / 100

  print(f"""
- O imposto nacional dentro do valor total da compra foi de: {imposto_nacional}%
- O imposto estadual dentro do valor total da compra foi de: {imposto_estadual}%
- O imposto municipal dentro do valor total da compra foi de: {imposto_municipal}%
- E o preço total da compra foi de: R${preco}""")
  
  while True:
    op = input("\n- Qual a forma de pagamento? ").capitalize()

    if op == "Dinheiro":
      nota = float(input("- Qual o valor fornecido? "))
      if nota < preco:
        print("\n-!!!!!!!!!!!!!!!!!!!!! Dinheiro insuficiente !!!!!!!!!!!!!!!!!!!!!-\n")
      else:
        troco = nota - preco
        print(f"- O troco deve ser de: R${troco}")
        print("\n-!!!!!!!!!!!!!!!!!!!!! Pagamento realizado com sucesso !!!!!!!!!!!!!!!!!!!!!-\n")
        break
    
    if op == "Pix":
      print("- Realize o pix: \"mvMQK5a&;W(AR4y?KVHURsLUVLiTk&Cg=Sn((R6q#gcJukm)Bc\"")
      print("\n-!!!!!!!!!!!!!!!!!!!!! Pagamento realizado com sucesso !!!!!!!!!!!!!!!!!!!!!-\n")
      break
    
    if op == "Cartão" or "Cartao":
      tipocartao = input("\n- Crédito, Débito ou Voucher?").capitalize
      saldo = float(input("\n- Insira o saldo do cartão: "))
      if saldo < preco:
        print("\n-!!!!!!!!!!!!!!!!!!!!! Saldo Insuficiente !!!!!!!!!!!!!!!!!!!!!-\n")
      else:
        print("\n-!!!!!!!!!!!!!!!!!!!!! Pagamento realizado com sucesso !!!!!!!!!!!!!!!!!!!!!-\n")
        break
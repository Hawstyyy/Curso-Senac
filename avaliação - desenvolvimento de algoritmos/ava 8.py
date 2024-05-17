func_log = ['1', '1','1', '1']

produtos = [
  'Alimentos', [
    'Frios', ['Carne']
  ],
  'Higiene', [
    'Pessoal', ['Papel']
  ],
]

print(produtos[1])

while True:
  ator = input("""
  +===================================================+
  |                 Bem-Vindo ao mercado!             |
  +===================================================+
  | C - Cadastro e login de cliente                   |
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
| S - Saída no estoque                     |
| R - Relatório do estoque                 |
| Rp - Registro de produto                 |
| X - Sair                                 |
+==========================================+

    - """)
    if op_func == "E" or op_func == "e":
        cod = int(input("\n- Insira o codigo do produto: "))

    elif op_func == "S" or op_func == "s":
        cod = int(input("\n- Insira o codigo do produto: "))

    elif op_func == "Rp" or op_func == "rp":
      cod = int(input("\nInsira o codigo do novo produto: "))
      nome = input("\nInsira o nome do produto: ").capitalize()
      
    elif op_func == "X" or op_func == "x":
      print("\n!!!!!!!!!!!!!!!!!! Programa encerrado !!!!!!!!!!!!!!!!!!\n")
      break
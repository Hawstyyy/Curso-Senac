func_log = ['Carlos', '123','1/1/1', '123.123.123-12']

while True:
  ator = input("""
  +===================================================+
  |                 Bem-Vindo ao mercado!             |
  +===================================================+
  | C - Cadastro e login de cliente
  | F - Login de funcionário
  +===================================================+
  - """)

  if ator == "C" or ator == "c":
    print("\n!!!!!!!!!!!!!!!!! Bem - vindo cliente !!!!!!!!!!!!!!!!!\n")
    nome_cliente = input("- Insira seu nome completo: ")
    cpf = input("- Insira o seu cpf: ")

  elif ator == "F" or ator == "f":
    print("\n!!!!!!!!!!!!!!!!! Bem - vindo funcionário !!!!!!!!!!!!!!!!!\n")
    nome_f = input("- Insira o seu nome completo: ")
    matricula = input("- Insira a sua matrícula: ")
    nasc = input("- Insira a sua data de nascimento: ")
    cpf_f = input("- Insira o seu cpf: ")

    if nome_f == func_log[0] and matricula == func_log[1] and nasc == func_log[2] and cpf_f == func_log[3]:
      print("\n!-! Login realizado com sucesso !-!\n")
      break
    else:
      print("\n!-! Login incorreto !-!\n")
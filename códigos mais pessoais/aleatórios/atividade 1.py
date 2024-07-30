lista_das_lista = []
while True:
  lista = []

  choice = int(input("""\nBem-Vindo ao sistema de saúde!

- 1 - Cadastrar Cliente 
- 2 - Sair 
      - """))

  if choice == 1:
    lista.append(input("- Insira o nome do paciente: ").capitalize())
    lista.append(input("- Digite o RG do paciente: "))
    lista.append(input("- Digite o CPF do paciente: "))
    lista.append(input("- Digite o telefone do paciente: "))
    lista_das_lista.append(lista)

  if choice == 2:
    for x in lista_das_lista:
      print(f"Nome: {x[0]} RG: {x[1]} CPF: {x[2]} Telefone: {x[3]}")
    break
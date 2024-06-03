# Crie um programa que permita adicionar, buscar e remover contatos de uma
# agenda telefônica usando um dicionário.

agenda = {'Pedro':'(99)9999-9999',
          'Ana': '(99)9999-9999'}

while True:
  print("\n+---------------------Agenda---------------------+")
  for key, value in agenda.items():
    print(f"| Nome: {key} - {value}")
  print("+------------------------------------------------+")

  select = input("""
+-------------------------------------+
| B - Buscar contato                  |
| A - Adicionar contato               |
| R - Remover contato                 |
| X - Digite qualquer coisa para sair |
+-------------------------------------+
  - """).capitalize()

  if select == "B":
    nome = input("\n- Insira o nome do contato: ").capitalize()
    for i in agenda:
      if nome in i:
        print(f"| Nome:{i[0]} - {i[1]}")

  elif select == "A":
    nome = input("\n- Insira o nome do contato: ").capitalize()

    for i in agenda:
      if nome in i:
        print("- Esse contato já existe")
        break
      else:
        telefone = input("- Insira o número do contato (EX:(99)9999-9999): ")
        agenda.update({nome:telefone})
        break
  
  elif select == "R":
    nome = input("\n- Insira o nome do contado que deseja remover: ").capitalize()

    for i in agenda:
      if nome in i:
        del agenda[i]
        print(f"\n--------------------! Contato \"{nome}\" removido com sucesso !--------------------")
        break
      else:
        print("\n- O contato não existe")
  else:
    print("\n!-------------------- Programa encerrado --------------------!\n")
    break
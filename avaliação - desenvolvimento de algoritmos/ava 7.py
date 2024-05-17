idade_min = 18
nota_min = 7.0

while True: 
  cargo = input("\n- Insira o cargo que deseja: ")
  nome_completo = input("- Insira o nome completo: ")
  idade = int(input("- Insira a sua idade: "))
  if idade >= idade_min:
    print(f"\n!!!!! o participante {nome_completo}, foi aprovado na primeira fase !!!!!\n")
  else:
    print(f"\n!!!!! o participante {nome_completo}, foi reprovado na primeira fase por não possuir a idade miníma para a vaga de {cargo}!!!!!\n")
    break

  email = input("- Insira o seu email para contato: ")
  curso = input("- O participante já realizou curso de qualificação na área? ")
  if curso == "S" or curso == "s":
    print(f"\n!!!!! o participante {nome_completo}, foi aprovado na segunda fase !!!!!")
  else:
    print(f"\n!!!!! o participante {nome_completo}, foi reprovado na segundafase por não possuir um curso de qualificação para a vaga de {cargo} !!!!!\n")
    break

  nota = float(input("- Insira a nota do candidato: "))
  mensagem = f"Agradecemos a participação do candidato {nome_completo}, mas infelizmente o candidato não conseguiu atingir a nota miníma para a etapa final da vaga"

  if nota >= nota_min:
    print(f"\n!!!!! o participante {nome_completo}, foi aprovado na terceira fase e está apto para a etapa final da vaga de {cargo}!!!!!\n")
  else:
    print(mensagem)
  break
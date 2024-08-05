caderno = 10
caneta = 20
lapis = 30
borracha = 40
regua = 50

while True:
  print("""
- - - - - - - - - Selecione a sua operação desejada - - - - - - - - - 
| E - Entrada no estoque
| S - Saída no estoque
| R - Relatório do estoque
| X - Sair
""")
  operacao = input("- ").capitalize()
  
  if operacao == "E":
    while True:
      codigo,quantia = input("\nInsira o código produto que deseja adicionar ao estoque e a quantia: ").split(",")
      quantia = int(quantia)
      
      if codigo == "10":
        caderno += quantia
        print(f"\n- - - - - - - - Adicionado mais {quantia} cadernos para o estoque")
        break

      elif codigo == "20":
        caneta += quantia
        print(f"\n- - - - - - - - Adicionado mais {quantia} canetas para o estoque")
        break

      elif codigo == "30":
        lapis += quantia
        print(f"\n- - - - - - - - Adicionado mais {quantia} lápis para o estoque")
        break

      elif codigo == "40":
        borracha += quantia
        print(f"\n- - - - - - - - Adicionado mais {quantia} borrachas para o estoque")
        break

      elif codigo == "50":
        regua += quantia
        print(f"\n- - - - - - - - Adicionado mais {quantia} réguas para o estoque")
        break
  
  elif operacao == "S":
    while True:
      codigo,quantia = input("\nInsira o código produto que deseja retirar do estoque e a quantia: ").split(",")
      quantia = int(quantia)
      
      if codigo == "10":
        if quantia > caderno:
          print("A quantia inserida excede o estoque atual de produtos")

        else: 
          caderno -= quantia
          print(f"\n- - - - - - - - Adicionado mais {quantia} cadernos para o estoque")
          break
      
      elif codigo == "20":
        if quantia > caneta:
          print("A quantia inserida excede o estoque atual de produtos")

        else:
          caneta -= quantia
          print(f"\n- - - - - - - - Retirado {quantia} canetas do estoque")
          break

      elif codigo == "30":
        if quantia > lapis:
          print("A quantia inserida excede o estoque atual de produtos")

        else:
          lapis -= quantia
          print(f"\n- - - - - - - - Retirado {quantia} lápis do estoque")
          break

      elif codigo == "40":
        if quantia > borracha:
          print("A quantia inserida excede o estoque atual de produtos")

        else:
          borracha -= quantia
          print(f"\n- - - - - - - - Retirado {quantia} borrachas do estoque")
          break

      elif codigo == "50":
        if quantia > regua:
          print("A quantia inserida excede o estoque atual de produtos")

        else:
          regua -= quantia
          print(f"\n- - - - - - - - Retirado {quantia} réguas do estoque")
          break

  elif operacao == "R":
    print(f"""
    - - - - - - - - - - - - - Estoque atual - - - - - - - - - - - - -
    10 - {caderno} Cadernos
    20 - {caneta} Canetas
    30 - {lapis} Lápis
    40 - {borracha} Borracha
    50 - {regua} Régua
    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    """)

  elif operacao == "X":
    break
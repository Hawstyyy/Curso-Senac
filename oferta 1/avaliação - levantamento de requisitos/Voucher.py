produtos = {'Celular': 0, 'Notebook': 0, 'Fone': 0, 'Videogame': 0}
codigo = {1: 'Celular', 2: 'Notebook', 3: 'Fone', 4: 'Videogame'}

while True:
  print('\n+ - - - - - - - - - - - - - Estoque - - - - - - - - - - - - - -')
  for x in codigo:
    print(f"| {x} - {codigo[x]} - {produtos[codigo[x]]}")
  print('+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

  operacao = input("""
+ Selecione a sua operação desejada - 
| E - Entrada no estoque
| S - Saída no estoque
| R - Relatório do estoque
| RG - Registro de produto
| X - Sair
      - """).upper()

  if operacao == "E":
    cod = int(input("\n- Insira o codigo do produto: "))

    for x in codigo:
      if cod == x:
        addquanti = int(input("\n- Insira a quantia: "))
        produtos[codigo[cod]] += addquanti
        break

  elif operacao == "S":
    cod = int(input("\n- Insira o codigo do produto: "))

    for x in codigo:
      if cod == x:
        rvquanti = int(input("\n- Insira a quantia: "))
        produtos[codigo[cod]] -= rvquanti
        break

  elif operacao == "RG":
    cod = int(input("\nInsira o codigo do novo produto: "))
    nome = input("\nInsira o nome do produto: ").capitalize()
    produtos[nome] = 0
    codigo[cod] = f'{nome}'
  
  elif operacao == "X":
    print("\n!!!!!!!!!!!!!!!!!! Programa encerrado !!!!!!!!!!!!!!!!!!\n")
    break
from registro import Registro
registro = Registro

banco = open("banco.txt", "r")
linhas = banco.readlines()

class UI(registro):
  def __init__(self, codigo, nome, quantidade):
    super().__init__(codigo, nome, quantidade)

  while True:
    print('+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
    for line in linhas:
      campos = line.strip().split(',')

      if len(campos) == 3:
        codigo = campos[0]
        nome = campos[1]
        quantidade = campos[2]
        print(f"| {codigo} - {nome} - {quantidade}")
    banco.close()
    print('+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

    operacao = input("""
  + Selecione a sua operação desejada - 
  | E - Entrada no estoque
  | S - Saída no estoque
  | R - Relatório do estoque
  | RG - Registro de produto
  | X - Sair
        - """).upper()
    if operacao == 'RG':
      codigo = int(input('- Insira o código do produto: '))
      nome = input('-Insira o nome do produto: ')
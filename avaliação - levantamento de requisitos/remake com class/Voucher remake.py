from registro import Registro
registro = Registro

banco = open("./banco.txt", "r")
linhas = banco.readlines()

while True:
  print('\n+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
  for line in linhas:
    campos = line.strip().split(',')

    if len(campos) == 3:
      codigo = campos[0]
      nome = campos[1]
      quantidade = campos[2]
      print(f"| {codigo} - {nome} - {quantidade}")
  banco.close()
  print('+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

  operacao = int(input("""
  + - Selecione a sua operação desejada - 
  | 1 - Entrada no estoque
  | 2 - Saída no estoque
  | 3 - Relatório do estoque
  | 4 - Registro de produto
  | 5 - Sair
        - """))
  if operacao == 'RG':
    codigo = int(input('- Insira o código do produto: '))
    nome = input('-Insira o nome do produto: ')
    check = registro.check(codigo, nome)

    if check == True:
      print("- Código ou nome já existente")
    else:
      print('a')
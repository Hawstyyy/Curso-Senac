from bingo import Bingo
from tabela import Tabela

bingo = Bingo()
tabela = Tabela()
tabela.gerar_num()
tabela.printa()

while True:
  choice = int(input("""
  +--------------------------------------+
  | Bem-vindo ao jogo de velho aka bingo |
  | 1 - Cartela                          |
  | 2 - Sortear número                   |
  +--------------------------------------+
      - """))

  if choice == 1:
    tabela.printa()
  elif choice == 2:
    bingo.sorte()
  else:
    print("Opção inválida. Escolha 1 ou 2.")
import bingo
from tabela import Tabela

def salvar_cartela(cartela):
    with open('cartela.txt', 'w') as arquivo:
        for linha in cartela:
            arquivo.write('\t'.join(map(str, linha)) + '\n')

tabela = Tabela()
tabela.gerar_num()
cartela = tabela.printa()

salvar = cartela
for linha in cartela:
  print('\t'.join(map(str, linha)))

choice = int(input("""
+--------------------------------------+
| Bem-vindo ao jogo de velho aka bingo |
| 1 - Cartela
| 2 - Sortear número
    -"""))

if choice == 1:
  for linha in cartela:
    print('\t'.join(map(str, linha)))
elif choice == 2:
  # Implemente a lógica para sortear um número, se necessário
  pass
else:
  print("Opção inválida. Escolha 1 ou 2.")
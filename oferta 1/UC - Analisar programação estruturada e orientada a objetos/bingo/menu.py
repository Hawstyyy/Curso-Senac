from bingo import Bingo
from tabela import Tabela

bingo = Bingo()
tabela = Tabela()

tabela.printa()

while True:
    choice = int(input("""
+--------------------------------------+
| Bem-vindo ao jogo de velho aka bingo |
| 1 - Mostrar Cartela                  |
| 2 - Sortear número                   |
| 3 - Inserir número sorteado          |
+--------------------------------------+
Escolha uma opção: """))

    if choice == 1:
        tabela.printa()

    elif choice == 2:
        sorted_num = bingo.sorte()

    elif choice == 3:
        sorted_num = int(input("- Insira o número que foi sorteado: "))
        tabela.marcar_numero(sorted_num)

        if tabela.verificar_bingo():
            tabela.printa()
            print("\nBINGO!!! Você ganhou!")
            break

    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")
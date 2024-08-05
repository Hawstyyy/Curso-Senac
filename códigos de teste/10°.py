#10. Um almoxarifado controla o estoque de 5 produtos indentificados pelo seu código abaixo:

# +======================+
# |  Código  |  Produto  |
# +==========+===========+
# |    10    | -Caderno  |
# |    20    | -Caneta   |
# |    30    | -Lápis    |
# |    40    | -Borracha |
# |    50    | -Régua    |
# +======================+

# Faça um programa que leia o estoque inicial de cada um dos produtos,
# e depois processe um certo número de operações, de acordo com o código abaixo:

# +=======================================================================================================+
# |  Código  |      Operação      |                                Ação                                   |
# |----------+--------------------+-----------------------------------------------------------------------|
# |     E    | Entrada do Estoque | Ler o código do produto que está entrando no estoque e a quantidade.  |
# |          |                    | Atualizar o estoque do produto.                                       |
# |----------+--------------------+-----------------------------------------------------------------------|
# |     S    | Saída no Estoque   | Ler o código do produto que está saindo do estoque e a quantidade.    |
# |          |                    | Atualizar o estoque do produto.                                       |
# |----------+--------------------+-----------------------------------------------------------------------|
# |     R    | Relatório          | Imprime um relatório mostrando as quantidades atuais de cada produto. |
# |----------+--------------------+-----------------------------------------------------------------------|
# |     X    | Sair               | Encerra a execução do programa.                                       |
# +=======================================================================================================+

# Antes de ler cada operação, o programa deve imprimir um menu de opções, assim:

# Escolha a operação:
# E -Entrada no Estoque;
# S -Saída no Estoque;
# R -Relatório;
# X -Sair;

# A operação de saída do estoque deve checar se a quantidade em estoque é suficiente para atender
# à quantidade que está sendo retirada do estoque. Se não for, deve exibir mensagem e impedir a operação.

pessoas = []
produtos = {'Caderno': 0,'Caneta': 0,'Lápis': 0,'Borracha': 0,'Régua': 0}
cod = {10: 'Caderno', 20: 'Caneta', 30: 'Lápsis', 40: 'Borracha', 50: 'Régua'}

i = 0
cont = True

print("""
+======================+
|  Código  |  Produto  |
+==========+===========+
|    10    | -Caderno  |
|    20    | -Caneta   |
|    30    | -Lápis    |
|    40    | -Borracha |
|    50    | -Régua    |
+======================+
      
Escolha a operação:
      
# E -Entrada no Estoque;
# S -Saída no Estoque;
# R -Relatório;
# X -Sair;
""")
while cont:
    i += 1
    nome = input("\nDigite seu nome: ")
    opera = input("Digite a operação que deseja efetuar: ").capitalize()

    if opera == 'E':
        codigo_produto = int(input("\nDigite o código do produto deseja adicionar: "))
        if codigo_produto == 10 or codigo_produto == 20 or codigo_produto == 30 or codigo_produto == 40 or codigo_produto == 50:
            produtos[cod[codigo_produto]] += 1
            print("\n-Produto adcionado! \n")
        else:
            print("-Produto Inválido! ")
        
    elif opera == 'S':
        saida_estoque = int(input("\nDigite o código do produto deseja retirar: "))
        if saida_estoque in produtos:
            if produtos[saida_estoque] > 0:
                produtos[saida_estoque] -= 1
            print("\n-Produto retirado! \n")
        else:
            print("\n-Produto Inválido! \n")
    elif opera == 'R':
        print(f"""
+===============+============+
| Estoque Atual | Quantidade |
+================================>>>
| -Caderno;     | {produtos.get('Caderno')}     
| -Caneta;      | {produtos.get('Caneta')}
| -Lápis;       | {produtos.get('Lápis')}
| -Borracha;    | {produtos.get('Borracha')}
| -Régua;       | {produtos.get('Régua')}
+================================>>>
""")    
    
    elif opera == 'X':
        cont = False
    else:
        print("\n-Operação Inválida! \n")


print("\nSocorro Felipe!!!!")

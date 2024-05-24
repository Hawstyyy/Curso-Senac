# Foi feita uma estatística em cinco cidades brasileiras para coletar
# dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio (em 1999);
# c. Número de acidentes de trânsito com vítimas (em
# 1999). Deseja-se saber:
# d. Qual o maior e menor índice de acidentes de transito e a que
# cidade pertence;
# e. Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com
# menos de 2.000 veículos de passeio.

lista = []
menor_indice = 0
maior_indice = 0

for i in range(5):
  codigo = int(input("\n- Insira o código da cidade: "))
  veiculos = int(input("- Insira o número de veículos de passeio: "))
  acidentes = int(input("- Insira o número de acidentes de transito com vítimas: "))
  lista.append([codigo,veiculos,acidentes])

for x in lista:
  if menor_indice > x[2] or menor_indice == 0:
    menor_indice = x[2]
  else:
    continue

for x in lista:
  if maior_indice < x[2] or maior_indice == 0:
    maior_indice = x[2]
  else:
    continue

for x in lista:
  veiculos += int(x[1])

media = veiculos / 5


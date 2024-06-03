# Faça um programa que leia dez conjuntos de dois valores, o primeiro
# representando o número do aluno e o segundo representando a sua altura
# em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o
# número do aluno mais alto e o número do aluno mais baixo, junto com suas
# alturas.

altura_min = 0
cod_baixo = 0

altura_max = 0
cod_alto = 0

lista = []

while True:
  codigo = int(input("\n- Insira o número do aluno, escreva 0 para sair: "))
  if codigo == 0:
    break
  else:
    altura = int(input("- Insira a altura do aluno, em cm: "))
    lista.append([codigo,altura])

for x in lista:
  if altura_min > x[1] or altura_min == 0:
    altura_min = x[1]
    cod_baixo = x[0]
  else:
    continue

for x in lista:
  if altura_max < x[1] or altura_max == 0:
    altura_max = x[1]
    cod_alto = x[0]

print(f"""
- O aluno mais alto tem: {altura_max} cm de altura, e é o número: {cod_alto}
- O aluno mais baixo tem: {altura_min} cm de altura, e é o número: {cod_baixo}""")
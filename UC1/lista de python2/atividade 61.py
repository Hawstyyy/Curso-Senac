# Em uma competição de ginástica, cada atleta recebe votos de sete
# jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a
# média dos votos restantes. Você deve fazer um programa que receba o
# nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua
# apresentação e depois informe a sua média, conforme a descrição acima
# informada (retirar o melhor e o pior salto e depois calcular a média com as
# notas restantes). As notas não são informados ordenadas. Um exemplo de
# saída do programa deve ser conforme o exemplo abaixo: 

notas = []

atleta = input("Insira o nome do atleta: ")
while True:
  try:
    nota = float(input("Insira a nota: "))
    menor = float(nota)
    maior = float(nota)
    soma = float(0)
    break

  except:
    print("Número inválido")
notas.append(nota)

for x in range(7):
  nota = float(input("Insira a próxima nota: "))
  notas.append(nota)

  if menor > nota:
    menor = nota
  else:
    maior = nota

media_final = sum(notas)/len(notas)

notas_finais = []
for i in notas:
  notas_finais.append(str(nota))

print(f"""
      +-------------------------Ficha final do atleta----------------
      | Nome do atleta: {atleta}
      | Notas: {', '.join(notas_finais)}
      | Menor nota: {menor}
      | Maior nota: {maior}
      | Media final do atleta: {media_final}
      +--------------------------------------------------------------""")
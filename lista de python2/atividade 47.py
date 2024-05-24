# Em uma competição de salto em distância cada atleta tem direito a
# cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior
# resultados são eliminados. O seu resultado fica sendo a média dos três
# valores restantes. Você deve fazer um programa que receba o nome e as
# cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a
# média dos saltos conforme a descrição acima informada (retirar o melhor e
# o pior salto e depois calcular a média). Faça uso de uma lista para
# armazenar os saltos. Os saltos são informados na ordem da execução,
# portanto não são ordenados. O programa deve ser encerrado quando não
# for informado o nome do atleta. A saída do programa deve ser conforme o
# exemplo abaixo: 

notas = []

atleta = input("Insira o nome do atleta: ")

while True:
  try:
    salto = float(input("Insira a salto: "))
    menor = float(salto)
    maior = float(salto)
    soma = float(0)
    break

  except:
    print("Número inválido")

notas.append(salto)

for x in range(5):
  salto = float(input("Insira o próximo salto: "))
  notas.append(salto)

  if menor > salto:
    menor = salto

  else:
    maior = salto

media_final = sum(notas)/len(notas)

notas_finais = []
for i in notas:
  notas_finais.append(str(salto))

print(f"""
      +-------------------------Ficha final do atleta----------------
      | Nome do atleta: {atleta}
      | Notas: {', '.join(notas_finais)}
      | Menor salto: {menor}
      | Maior salto: {maior}
      | Media final do atleta: {media_final}
      +--------------------------------------------------------------""")

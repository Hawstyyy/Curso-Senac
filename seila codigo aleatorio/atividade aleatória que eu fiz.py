contador = 0
contagem = 7
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

contador += 1
notas.append(nota)

while contador < contagem:
  nota = float(input("Insira a próxima nota: "))
  notas.append(nota)

  if menor > nota:
    menor = nota

    contador += 1
  elif maior < nota:
    maior = nota

    contador += 1
  else:

    contador += 1

for nota in notas:
  soma += nota

media_final = soma/len(notas)

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

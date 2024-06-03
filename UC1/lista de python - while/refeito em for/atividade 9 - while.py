candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
votonulo = 0
votobranco = 0
contagem = 0

while True:
  codigo = int(input("\n- Insira o número do seu respectivo candidato (1,2,3,4) ou insira 5 para voto nulo ou 6 para voto branco, (digite 0 para sair): "))

  if codigo == 0:
    break
  elif codigo == 1:
    candidato1 += 1
  elif codigo == 2:
    candidato2 += 1
  elif codigo == 3:
    candidato3 += 1
  elif codigo == 4:
    candidato4 += 1
  elif codigo == 5:
    votonulo += 1
  elif codigo == 6:
    votobranco += 1

  print("\n\n------------Voto computado com sucesso!------------\n")
  
  contagem += 1

print(f"""\n
      + - - - - - - - Tabela final da votação - - - - - - - - - - - - - - -
      | Candidato 1 recebeu: {candidato1} votos
      | Candidato 2 recebeu: {candidato2} votos
      | Candidato 3 recebeu: {candidato3} votos
      | Candidato 4 recebeu: {candidato4} votos
      | A quantidade de votos nulos foi de: {votonulo} votos
      | A quantidade de votos em branco foi de: {votobranco} votos
      | O total de votações realizadas no dia foi de: {contagem} votos
      + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      """)
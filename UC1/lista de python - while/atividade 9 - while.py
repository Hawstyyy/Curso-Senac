votos = {'Candidato1': 0, 'Candidato2': 0, 'Candidato3': 0, 'Candidato4': 0, 'votonulo': 0, 'votobranco': 0}
loca = {1: 'Candidato1', 2: 'Candidato2', 3: 'Candidato3', 4: 'Candidato4', 5: 'votonulo', 6: 'votobranco'}
contagem = 0

while True:
  while True:
    try:
      codigo = int(input("\n- Insira o número do seu respectivo candidato (1,2,3,4) ou insira 5 para voto nulo ou 6 para voto branco, (digite 0 para sair): "))
      if codigo < 0 or codigo > 6:
        print("\n- Voto inválido")
      else:
        break
    except:
      print("\n- Número inválido")

  if codigo == 1 or codigo == 2 or codigo == 3 or codigo == 4 or codigo == 5 or codigo == 6:
    votos[loca[codigo]] += 1

  elif codigo == 0:
    break
    
  print("\n\n------------Voto computado com sucesso!------------\n")
  
  contagem += 1

print(f"""\n
      + - - - - - - - Tabela final da votação - - - - - - - - - - - - - - -
      | Candidato 1 recebeu: {votos.get('Candidato1')} votos
      | Candidato 2 recebeu: {votos.get('Candidato2')} votos
      | Candidato 3 recebeu: {votos.get('Candidato3')} votos
      | Candidato 4 recebeu: {votos.get('Candidato4')} votos
      | A quantidade de votos nulos foi de: {votos.get('votonulo')} votos
      | A quantidade de votos em branco foi de: {votos.get('votobranco')} votos
      | O total de votações realizadas no dia foi de: {contagem} votos
      + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      """)
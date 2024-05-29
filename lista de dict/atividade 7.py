# Crie um dicionário com algumas palavras e seus sinônimos. Peça ao usuário
# para digitar uma palavra e exiba seus sinônimos.

dicionario = {'Feliz': 'contente, alegre, satisfeito, radiante, jubiloso.',
'Triste': 'melancólico, abatido, desanimado, desolado, inconsolável.',
'Grande': 'enorme, vasto, amplo, gigantesco, imenso.',
'Pequeno': 'diminuto, minúsculo, miúdo, reduzido, ínfimo.',
'Rápido': 'veloz, ágil, ligeiro, acelerado.'}
while True:
  texto = input("\n- Insira a palavra que você deseja pesquisar: ").capitalize()

  if texto not in dicionario:
    print("\n-! Esse texto não está presente no dicionário! ")
  else:
    for key, value in dicionario.items():
      if texto in key:
        print(f"\n- A palavra {key} tem os sinônimos de: {value}")
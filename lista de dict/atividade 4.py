#  Crie um dicionário com algumas palavras em inglês e suas traduções em
# português. Peça ao usuário para digitar uma palavra em inglês e exiba a tradução
# correspondente.

dict = {'mother':'mãe',
'light':'luz',
'parts':'partes',
'country':'país',
'father':'pai',
'picture':'imagem',
'eyes':'olhos',
'times':'vezes',
'help':'ajuda',
'thought':'pensamento',
'show':'show',
'night':'noite',
'story':'história',
'boys':'meninos'}

while True:
  select = input("\n- Insira a sua palavra em inglês ou x para sair: ")

  if select not in dict:
    print("\nA palvra inserida não existe!")
  else:
    for key, value in dict.items():
      if select in key:
        print(f"\nA palavra {key}, tem a tradução de: {value}")
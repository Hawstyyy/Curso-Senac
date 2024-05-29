# Crie um programa que leia um texto e conte quantas vezes cada palavra aparece.
# Armazene as letras e suas contagens em um dicionário.

texto = input("\n- Insira o seu texto para fazermos a contagem de palvras! ").lower()

letras = {}

for letra in texto:
  if letra == " ":
    continue
  else:
    conta = texto.count(letra)
    letras.update({letra:conta})

for i in letras:
  print(f"| {i} - apareceu o total de: {letras[i]}")
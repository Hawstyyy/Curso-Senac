# Crie um programa que leia um texto e conte quantas vezes cada palavra aparece.
# Armazene as palavras e suas contagens em um dicionário.

texto = input("\n- Insira o seu texto para fazermos a contagem de palvras! ").lower().split(" ")

palavras = {}

for palavra in texto:
  x = texto.count(palavra)
  palavras.update({palavra:x})

for i in palavras:
  print(f"| {i} - apareceu o total de: {palavras[i]}")
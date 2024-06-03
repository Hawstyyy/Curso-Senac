# Leia um texto e conte quantas vezes cada caractere (letras, números, símbolos)
# aparece. Armazene os caracteres e suas contagens em um dicionário.

texto = input("\n- Insira o seu texto para fazermos a contagem de palvras! ").lower()

caracteres = {}

for caracter in texto:
  if caracter == " ":
    continue
  else:
    conta = texto.count(caracter)
    caracteres.update({caracter:conta})

for i in caracteres:
  print(f"| {i} - apareceu o total de: {caracteres[i]}")
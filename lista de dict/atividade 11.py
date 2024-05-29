# Leia um texto e conte quantas vezes cada vogal (a, e, i, o, u) aparece. Armazene
# as vogais e suas contagens em um dicionário.

vogais = ["a", "e", "i", "o", "u"]
letras = {}

texto = input("\n- Insira seu texto que deseja contar as suas vogais: ").lower()

for vogal in vogais:
  if vogal in texto:
    conta = texto.count(vogal)
    letras[vogal] = conta

print(letras)
# 2 - Implemente um algoritmo em Python que receba uma string como parâmetro e imprima as
# vogais dessa string. Exemplo: string ‘univesp’ → deve imprimir os caracteres ‘u’, ‘i’ e ‘e’.

palavra = input("\n- Insira a sua palavra que deseja remover as vogais: ")
vogais = ['a','e','i','o','u']

print(f"\nAs vogais da palavra \"{palavra}\" são:")
for x in palavra:
  for z in vogais:
    if x == z:
      print(f"- {x}")
print()
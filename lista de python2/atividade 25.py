# Faça um programa que calcule o mostre a média aritmética de N
# notas. 

notas = []
nota = 0

while True:
  try:
    nota = float(input("\nInsira suas notas, digite 123 para sair: "))

  except:
      print("\n!!!!!!!!! Número inválido !!!!!!!!!")
      continue
  
  if nota == 123:
    break

  elif nota < 0 or nota > 10:
      print("\n!!!!!!!!! Nota inválida !!!!!!!!!")
      continue
  
  notas.append(nota)

media = sum(notas) / len(notas)

print(f"""
- A média das notas: {notas} contendo {len(notas)} notas será de:
- {round(media,2)}
""")

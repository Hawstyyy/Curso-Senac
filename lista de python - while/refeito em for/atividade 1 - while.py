while True:
  try:
    nota = float(input("Insira a nota desejada: "))
    break
  except:
    print("Nota inv")

while nota > 10 or nota < 0:
  nota = float(input("Nota inválida, tente de novo: "))

print("Nota válida")
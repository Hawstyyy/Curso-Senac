idade = int(input("Insira a idade do competidor: "))

if idade >= 5 and idade <= 12:
  print("Categoria do competidor: Infantil")
elif idade >= 12 and idade <= 17:
  print("Categoria do competidor: Juvenil")
elif idade >= 18:
  print("Categoria do competidor: Sênior")
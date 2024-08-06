a = input("teste: ")
try:
  a = float(a)
  print(f"String convertida com sucesso: {a}")
except ValueError:
  print("Não foi possível converter a string para um número")
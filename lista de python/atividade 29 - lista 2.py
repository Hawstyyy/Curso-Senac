idade = int(input("Insira a idade do trabalhador: "))
tempo = int(input("Insira o tempo de serviço em anos: "))

if idade >= 65:
  print("O trabalhador pode se aposentar")
elif tempo >= 30:
  print("O trabalhador pode se aposentar")
elif idade >= 60 and tempo >= 25:
  print("O trabalhador pode se aposentar")
else:
  print("O trabalhador não pode se aposentar ainda")
peso = float(input("Insira o peso da pessoa: "))
altura = int(input("Insira a altura da pessoa em cm: "))

imc = peso / (altura * altura)

if imc <= 18.5:
  print("Abaixo do peso")

elif imc >= 18.6 and imc <= 24.9:
  print("Saudável")

elif imc >= 25 and imc <= 29.9:
  print("Peso em excesso")

elif imc >= 30 and imc <= 34.9:
  print("Obesidade grau I")

elif imc >= 35 and imc <= 39.9:
  print("Obesidade grau II(sevéra)")

else:
  print("Obesidade grau III(mórbida)")
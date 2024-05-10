sexo = input("Insira o sexo da pessoa (M/F): ").capitalize()
altura = int(input("Insira a altura da pessoa em cm: "))

if sexo == "M":
  peso = 72.7 * altura

  if peso > 58.00:
    print("A pessoa está acima do seu peso ideal")
  else:
    print("A pessoa está no peso ideal")

elif sexo == "F":
  peso = 62.1 * altura

  if peso > 44.7:
    print("A pessoa está acima do seu peso ideal")
  else:
    print("A pessoa está no peso ideal")
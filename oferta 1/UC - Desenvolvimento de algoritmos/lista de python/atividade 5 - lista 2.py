while True:
  sexo = input("Insira o seu sexo: ").capitalize()

  if sexo != "F" and sexo != "M":
    print("Sexo inválido")
  else:
    print(f"Seu sexo é: {sexo}")
    break
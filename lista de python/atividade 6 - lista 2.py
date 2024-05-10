while True:
  turno = input("Insira o turno que você estuda na sua escola/faculdade/curso: ").capitalize()

  if turno != "M" and turno != "V" and turno != "N":
    print("Valor inválido")
  elif turno == "M":
    print("Bom dia!")
    break
  elif turno == "V":
    print("Boa tarde!")
    break
  elif turno == "N":
    print("Boa noite!")
    break
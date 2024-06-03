while True:
  notas = input("Insira as notas do aluno: ").split(",")

  nota1, nota2 = float(notas[0]), float(notas[1])

  if nota1 < 0.00 or nota1 > 10 or nota2 < 0 or nota2 > 10 :
    print("Nota inválida")

  else:
    media = (nota1 + nota2) / 2
    print(f"A média do aluno será de {media}")
    break
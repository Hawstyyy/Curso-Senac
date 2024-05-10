while True:
  trab = float(input("Insira a primeira nota do aluno: "))


  ava = float(input("Insira a segunda nota do aluno: "))


  exam = float(input("Insira a terceira nota do aluno: "))

  
  media = ((trab * 2) + (ava * 3) + (exam * 5)) / (2 + 3 + 5)
  
  if media < 2.9 and media < 2.9:
      print("O aluno está reprovado")
      break
  elif media > 3 and media < 5.9:
    print("O aluno está de recuperação")
    break
  else:
    print("O aluno foi aprovado")
    break
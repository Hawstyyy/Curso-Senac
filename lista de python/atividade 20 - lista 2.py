nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))
nota3 = float(input("Insira a terceira nota do aluno: "))

media = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / (1 + 1 + 2)

if media >= 60:
  print("O aluno está aprovado")
else:
  print("O aluno está reprovado")

#  Crie um dicionário com nomes de alunos e suas notas. Calcule a média das
# notas e exiba o resultado

alunos = {'Ana': [6.5,7.0,8.0], 'Júlia': [5.0,6.0,5.0]}

while True:
  print("""
+-------------------- Alunos cadastrados --------------------+""")
  for key,value in alunos.items():
    print(f"| {key} - Notas: {value[0]}, {value[1]}, {value[2]}")
  print("+------------------------------------------------------------+")

  select = input("\n- Qual aluno gostaria dever a média? ").capitalize()

  if select not in alunos:
    select_add = input("\n- Esse aluno não existe, gostaria de adicionar? (S/N): ").capitalize()

    if select_add == "S":
      notas = {}
      nome = select
      nota = input("- Insira as notas do aluno dividos por uma vírgula: ").split(",")
      notas = [float(nota[0]), float(nota[1]), float(nota[2])]
      alunos.update({nome:notas})
      print("\n-! Aluno adicionado !-")

    else:
      continue

  else:
    for key,value in alunos.items():
      if select in key:
        media = (value[0] + value[1] + value[2])/3

        if media >= 6:
          print(f"\n- O aluno(a) {key}, tem a média de {round(media,2)} e está aprovado(a)")
        else:
          print(f"\n- O aluno(a) {key}, tem a média de {round(media,2)} e está de recuperação")
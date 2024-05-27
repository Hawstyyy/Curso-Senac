#  Crie um dicionário com nomes de alunos e suas notas. Calcule a média das
# notas e exiba o resultado

alunos = {('Ana', 6.5,7.0,8.0), ('Júlia', 5.0,6.0,5.0)}

print("""
+-------------------- Alunos cadastrados --------------------+""")
for i in alunos:
  print(f"| {i[0]} - Notas: {i[1]}, {i[2]}, {i[3]}")
print("+------------------------------------------------------------+")

select = input("\n- Qual aluno gostaria dever a média? ").capitalize()
for i in alunos:
  if select in i:
    media = (i[1] + i[2] + i[3])/3

    if media >= 6:
      print(f"\n- O aluno(a) {i[0]}, tem a média de {round(media,2)} e está aprovado(a)")
    else:
      print(f"\n- O aluno(a) {i[0]}, tem a média de {round(media,2)} e está de recuperação")
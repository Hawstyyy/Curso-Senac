# Desenvolver um programa para verificar a nota do aluno em uma
# prova com 10 questões, o programa deve perguntar ao aluno a resposta de
# cada questão e ao final comparar com o gabarito da prova e assim calcular
# o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada
# aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai
# utilizar o sistema. Após todos os alunos terem respondido informar:
# a. Maior e Menor Acerto;
# Total de Alunos que utilizaram o

resposta_correta = ['a', 'b', 'c', 'd', 'e', 'e', 'd', 'c', 'b', 'a']
quantidade = 0
notas = []

while True:
  nota = 0
  respostas = input("\n- Insira todas as suas respostas, separados por uma virgula: ").split(",")

  for x in range(len(resposta_correta)):
    if respostas[x] == resposta_correta[x]:
      nota += 1
  
  quantidade += 1
  print(f"- Sua nota foi: {nota}")
  notas.append(nota)

  controle = input("- Outro aluno irá usar o sistema? (S/N)").capitalize()
  if controle == "N":
    break

media = sum(notas)/quantidade

print(f"""
- O total de alunos que usaram o sistema foi de: {quantidade} alunos
- O maior acerto foi de: {max(notas)}
- O menor acerto foi de: {min(notas)}
- A média da turma foi de: {media}""")
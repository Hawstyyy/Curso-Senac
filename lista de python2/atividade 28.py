# Faça um programa que calcule o número médio de alunos por turma. 
# Para isto, peça a quantidade de turmas e a quantidade de alunos para cada 
# turma. As turmas não podem ter mais de 40 alunos. 
while True:
  turmas = int(input("\n- Insira a quantidade de turmas presentes na escola: "))
  alunos = int(input("\n- Insira a quantidade de alunos totais: "))

  m_alunos = alunos // turmas

  if m_alunos > 40:
    print(f"""
- O limite de alunos por turma é 40!
- Com a quantia de turmas atual, cada turma teria que suportar {m_alunos} alunos por turma.
""")

  else:
    print(f"""
    - Haverá {turmas} turmas em uma escola com o total de {alunos} alunos.
    - Cada turma conterá {m_alunos} alunos em cada.
    """)
    break
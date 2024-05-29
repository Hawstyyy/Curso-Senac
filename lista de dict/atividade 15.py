# Crie um dicionário com nomes de disciplinas e suas notas. Exiba a disciplina
# com a maior nota.

disciplinas = {
  'Língua Portuguesa': 8.00,
  'Matemática': 9.00,
  'Literatura': 6.00,
  'Inglês':9.00,
  'Espanhol':7.00
}

min = 10.00
max = 0.00

for key,value in disciplinas.items():
  if value < min:
    min = value
    min_dis = key
  elif value > max:
    max = value
    max_dis = key

print(f"""\n- A disciplina com maior nota é a {max_dis} com a nota de: {max}
- A disciplina com a menor nota é a {min_dis} com a nota de: {min}
""")
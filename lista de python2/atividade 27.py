# Numa eleição existem três candidatos. Faça um programa que peça 
# o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o 
# número de votos de cada candidato. 

eleitores_totais = int(input("\n- Insira o total de eleitores presentes: "))

candidatos = {'Candidato 1': 0, 'Candidato 2': 0, 'Candidato 3': 0, 'Voto Nulo': 0, 'Voto Branco': 0}
num_candidato = {1: 'Candidato 1', 2: 'Candidato 2', 3: 'Candidato 3', 4: 'Voto Nulo', 5: 'Voto Branco'}

for x in range(1,eleitores_totais+1):
  voto = int(input("\n- Insira o seu candidato (1 = candidato 1; 2 = candidato 2; 3 = candidato 3; 4 = Voto nulo; 5 = Voto branco): "))

  candidatos[num_candidato[voto]] += 1

print("""
\n+ - - - - - - - - - Tabela final da eleição - - - - - - - - - - - -""")

for x in num_candidato:
  print(f"| {x} - {num_candidato[x]} - {candidatos[num_candidato[x]]} votos")

print("""+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n""")
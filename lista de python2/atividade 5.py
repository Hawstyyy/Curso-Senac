# Altere o programa anterior permitindo ao usuário informar as
# populações e as taxas de crescimento iniciais. Valide a entrada e permita
# repetir a operação. 

pais_a = float(input("\nInsira o tamanho da população A: "))
pais_b = float(input("\nInsira o tamanho da população B: "))
PAIS_A = pais_a
PAIS_B = pais_b

per_a = float(input("\nInsira a porcentagem de crescimento do país A: ")) / 100
per_b = float(input("\nInsira a porcentagem de crescimento do país B: ")) / 100

ano = 0

while pais_a <= pais_b:
  pais_a += (pais_a * per_a)
  pais_b += (pais_b * per_b)
  ano += 1

print(f"\n - A quantia de anos para o país A (com {PAIS_A} de pessoas) ultrapassar o país B (Com {PAIS_B} de pessoas) será de: {ano} anos")
# Supondo que a população de um país A seja da ordem de 80000
# habitantes com uma taxa anual de crescimento de 3% e que a população
# de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça
# um programa que calcule e escreva o número de anos necessários para
# que a população do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

pais_a = 80000
pais_b = 200_000

per_a = 0.03
per_b = 0.015

ano = 0

while pais_a <= pais_b:
  pais_a += (pais_a * per_a)
  pais_b += (pais_b * per_b)
  ano += 1

print(f"A quantia de anos para o país A ultrapassar o país B será de: {ano} anos")
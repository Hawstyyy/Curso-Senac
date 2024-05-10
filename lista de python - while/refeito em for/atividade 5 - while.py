a = int(input("Insira a população inicial do país A: "))
b = int(input("Insira a população inicial do país B: "))
porcentagem_a = float(input("Insira a porcentagem de crescimento do país A: "))
porcentagem_b = float(input("Insira a porcentagem de crescimento do país b: "))
ano = 0

while a <= b:
  porcentagem = (a * porcentagem_a) / 100
  a += porcentagem

  porcentagem = (b * porcentagem_b) / 100
  b+= porcentagem
  ano += 1

print(f"Demoraram {ano} anos para o país A, ficar igual ao país")
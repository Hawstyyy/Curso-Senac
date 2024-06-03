a = 80000
b = 200000
ano = 0

while a <= b:
  porcentagem = (a * 3) / 100
  a += porcentagem

  porcentagem = (b * 1.5) / 100
  b+= porcentagem
  ano += 1

print(f"Demoraram {ano} anos para o país A, ficar igual ao país")
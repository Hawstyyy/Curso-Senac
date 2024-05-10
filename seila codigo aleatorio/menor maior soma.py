numeros = []
for cont in range(5):
  numeros.append(int(input("bota numero sei la porra: ")))

maior = 0
menor = 0

for i in numeros:
  if i > maior:
    maior = i
  if i < menor or menor == 0:
    menor = i

soma = maior + menor
print(f"Menor número é {menor}")
print(f"Maior número é {maior}")
print(f"A soma do número é {soma}")
lista = []
soma = 0

for cont in range(10):
  lista.append(int(input("insira numero: ")))

for x in lista:
  soma += x

print(f"A soma dos números inseridos pelo usuário é: {soma}")
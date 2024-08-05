# Altere o programa anterior para que ele aceite apenas números entre
# 0 e 1000. 

numeros = []
numero = 0
soma = 0

while True:
  numero = int(input("Insira seus números, digite 0 para sair: "))


  if numero < 0 or numero > 1000:
    print("Erro")
    continue
  
  elif numero == 0:
    print(numeros)
    break
  
  numeros.append(int(numero))

for x in numeros:
  soma += x

print(f"""
- O menor valor da lista foi: {min(numeros)}.
- O maior valor da lista foi: {max(numeros)}.
- A soma de todos os valores da lista foi de: {soma}.
\n""")
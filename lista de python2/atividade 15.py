# Faça um programa que peça 10 números inteiros, calcule e mostre a
# quantidade de números pares e a quantidade de números ímpares. 

numeros = []
impar = []
par = []

for x in range(10):
  numeros.append(int(input(f"\nInsira o seu {x+1}° número: ")))

for i in numeros:
  if i % 2 == 0:
    par.append(str(i))
  else:
    impar.append(str(i))

print(f"""
- A quantidade de números pares foi de: {", ".join(par)}
- A quantiadade de númeoros ímpares foi de: {", ".join(impar)}\n""")
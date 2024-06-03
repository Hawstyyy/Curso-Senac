# Faça um programa que receba dois números inteiros e gere os
# números inteiros que estão no intervalo compreendido por eles. 


numeros = []
while True:
  try:
    numero2 = int(input("\nInsira seu número inteiro: "))
    numero1 = int(input("\nInsira seu segundo número inteiro: "))
    break
  except:
    print("\n!!!!!!!!!!!!!!!! Número inválido !!!!!!!!!!!!!!!!")

if numero1 < numero2:
  numero1, numero2 = numero2, numero1

for x in range(numero2, numero1):
  numeros.append(str(x))

print(f"\n- Os números que estão no intervalo de {numero1} e {numero2} são:\n")
print(", ".join(numeros), "\n")
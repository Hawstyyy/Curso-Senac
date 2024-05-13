# Altere o programa anterior para mostrar no final a soma dos
# números. 

numeros = []
soma = 0

while True:
  try:
    numero2 = int(input("\nInsira seu número inteiro: "))
    numero1 = int(input("\nInsira seu segundo número inteiro: "))
    break
  except:
    print("\n!!!!!!!!!!!!!!!! Número inválido !!!!!!!!!!!!!!!!")

if numero1 < numero2:
  numero1, numero2 = numero2, numero1

for x in range(numero2, numero1 + 1):
  soma += x
  numeros.append(str(x))

print(f"\n- Os números que estão no intervalo de {numero1} e {numero2} são:\n")
print(", ".join(numeros), "\n")
print(f"E a soma dos números acima é de: {soma}")
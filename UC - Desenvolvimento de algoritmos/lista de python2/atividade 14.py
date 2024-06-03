# Faça um programa que peça dois números, base e expoente, calcule
# w
while True:
  try:
    base = int(input("\nInsira a base: "))
    expoente = int(input("\nInsira o expoente: "))
    break
  except:
    print("\n!!!!!!!!!!!!!!!!! Número inválido !!!!!!!!!!!!!!!!!")

r = base ** expoente

print(f"\nO número {base} elevado a {expoente} tem o resultado de: {r}\n")
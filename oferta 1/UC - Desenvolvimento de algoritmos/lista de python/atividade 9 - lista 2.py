numeros = input("Insira seus dois números desejados: ").split(",")

numero1, numero2 = int(numeros[0]), int(numeros[1])

temp = numero1
numero1 = numero2
numero2 = temp

print(f"A inversão dos números será: {numero1} e {numero2}")
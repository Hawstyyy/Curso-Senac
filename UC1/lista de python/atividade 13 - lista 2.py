numeros = input("Insira os números que deseja comparar: ").split(",")

numero1, numero2 = int(numeros[0]), int(numeros[1])

if numero1 > numero2:
  diff = numero1 - numero2
  print(f"O número: {numero1} é maior que o número: {numero2}")
  print(F"E a sua diferença é de: {diff}")

elif numero2 > numero1:
  diff = numero2 - numero1
  print(f"O número: {numero2} é maior que o número: {numero1}")
  print(F"E a sua diferença é de: {diff}")

elif numero1 == numero2:
  print("Os números são iguais")
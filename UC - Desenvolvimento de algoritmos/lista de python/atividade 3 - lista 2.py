numeros = input("Insira os números para compararmos eles entre si!: ").split(",")

while True:
  try:
    numero1, numero2 = int(numeros[0]), int(numeros[1])
    break
  except:
    numeros = input("algum número foi inválido ou faltou algum, tente de novo: ").split(",")

if numero1 > numero2:
  print(f"O número \"{numero1}\" é maior que o número \"{numero2}\"")
elif numero2 > numero1:
  print(f"O número \"{numero2}\" maior que o número \"{numero1}\"")
else:
  print(f"Os números são iguais")
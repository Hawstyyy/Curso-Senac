while True:
  try:
    numero = int(input("numero: "))
    tabuada = int(input("ate que numero: "))
    break

  except:
    print("Número inválido")
tabuada += 1

for x in range(1,tabuada):
  print(f"{numero} x {x} = ", (numero * x))
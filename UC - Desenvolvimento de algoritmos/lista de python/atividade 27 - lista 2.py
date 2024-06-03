lado1 = float(input("Insira um dos lados do triangulo: "))
lado2 = float(input("Insira um dos lados do triangulo: "))
lado3 = float(input("Insira um dos lados do triangulo: "))

if lado1 + lado2 > lado3 or lado2 + lado3 > lado1:
  if lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("O triângulo é equilátero")
  elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("O triângulo é isósceles")
  elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print("O triângulo é escaleno")

else:
  print("Não é um triângulo")
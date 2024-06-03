# Crie um programa que recebe os três lados de um triângulo e passa esses valores para uma
# função que verifica se esse triângulo existe ou não. Para que um triângulo exista, cada lado
# deve ser maior que o módulo da subtração dos outros dois lados e menor que a soma dos
# outros dois lados.

def triangulo(lado1,lado2,lado3):
  lado1_maior = lado1 > (lado2 - lado3)
  lado1_menor = lado1 < (lado2 + lado3)

  lado2_maior = lado2 > (lado1 - lado3)
  lado2_menor = lado2 < (lado1 + lado3)

  lado3_maior = lado3 > (lado1 - lado2)
  lado3_menor = lado3 < (lado1 + lado2)

  if lado1_maior == False or lado1_menor == False or lado2_maior == False or lado2_menor == False or lado3_maior == False or lado3_menor == False:
    print("Esse triangulo não existe!")
  else:
    print("Esse triangulo existe!")

print("\n#--------------------- Bem-vindo ao identificador de triângulo! ---------------------#")

lado1 = float(input("\n- Insira o primeiro lado do triângulo: "))
lado2 = float(input("- Insira o segundo lado do triângulo: "))
lado3 = float(input("- Insira o terceiro lado do triângulo: "))

triangulo(lado1,lado2,lado3)
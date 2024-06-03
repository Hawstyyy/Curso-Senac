# Crie um programa que recebe os dois lados menores de um triângulo retângulo e uma
# função retorna o valor da hipotenusa.

def hipotenusa(ladomenor1,ladomenor2):
  print("A hipotenusa é: ", ((ladomenor1**2)+(ladomenor2**2))**(1/2))

ladomenor1 = float(input("\n- Insira um dos lados menores de seu triângulo: "))
ladomenor2 = float(input("- Insira o outro lado menor de seu triângulo: "))
hipotenusa(ladomenor1,ladomenor2)
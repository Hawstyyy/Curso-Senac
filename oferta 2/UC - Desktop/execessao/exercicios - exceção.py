class Div():
  def __init__(self, a, b):
    self.a = a
    self.b = b
  
  def divisao(a,b):
    try:
      div = a / b
      return div
    except ArithmeticError:
      print("Não é possível realizar uma divisão por zero!")

try:
  a = float(input("Primeiro número: "))
except ValueError:
  print("Insira um número válido")

try:
  b = float(input("Segundo número: "))
except ValueError:
  print("Insira um número válido")

div = Div.divisao(a,b)
print(div)
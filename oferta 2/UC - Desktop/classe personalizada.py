class Custom(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)
    print("- Não é possível somar o número 0")

class Math():
  def soma(a,b):
    return a + b

if __name__ == "__main__":
  while True:
    a = int(input("- Insira os seu primeiro número: "))
    b = int(input("- Insira os seu segundo número: "))

    if a == 0 or b == 0:
      raise Custom()
    else:
      Math.soma(a,b)
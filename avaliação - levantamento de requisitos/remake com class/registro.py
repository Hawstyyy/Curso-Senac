banco = open("banco.txt", "r")
linhas = banco.readlines()

class Registro():
  def __init__(self, codigo, nome):
    self.codigo = int(self.codigo)
    self.nome = self.nome

  def check(self, codigo, nome):
    for line in linhas:
      campos = line.strip().split(',')
      if self.nome in campos and self.codigo in campos or self.codigo in campos:
        return True
      else:
        return False
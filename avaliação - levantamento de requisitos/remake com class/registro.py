banco = open("banco.txt", "r")
linhas = banco.readlines()

class Registro:
  def __init__(self, codigo, nome, quantidade):
    self.codigo = int(self.codigo)
    self.nome = self.nome
    self.quantidade = int(self.quantidade)

  def check(self, codigo, nome, quantidade):
    for line in linhas:
      campos = line.strip().split(',')

      if len(campos) == 3:
        codigo = campos[0]
        nome = campos[1]
    if self.codigo == codigo:
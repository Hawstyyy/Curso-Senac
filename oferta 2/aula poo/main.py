class Animal:
  def __init__(self,nome, nome_cien, alimentacao, reproducao):
    self.nome = nome
    self.nome_cien = nome_cien
    self.alimentacao = alimentacao
    self.reproducao = reproducao
  
  def respirar(self):
    print(f'O animal {self.nome} respirou')

  def seReproduzir(self):
    print(f'O animal {self.nome} se reproduzido')

class Vertebrados(Animal):
  def __init__(self, nome, nome_cien, alimentacao, reproducao):
    super().__init__(nome, nome_cien, alimentacao, reproducao)
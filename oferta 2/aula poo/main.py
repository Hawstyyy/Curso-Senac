class Animal:
  def __init__(self,nome, nome_cien, alimentacao, reproducao):
    self.nome = nome
    self.nome_cien = nome_cien
    self.alimentacao = alimentacao
    self.reproducao = reproducao
  
  def respirar(self):
    print(f'O animal {self.nome} respirou')

  def seReproduzir(self):
    print(f'O animal {self.nome} se reproduziu')

class Vertebrados(Animal):
  def __init__(self, nome, nome_cien, alimentacao, reproducao, esqueleto, coluna):
    super().__init__(nome, nome_cien, alimentacao, reproducao)
    self.esqueleto = esqueleto
    self.coluna = coluna

  def seMover(self):
    print(f'O animal {self.nome} se moveu')

class Mamiferos(Vertebrados):
  def __init__(self, nome, nome_cien, alimentacao, reproducao, esqueleto, coluna, mamarias, endotermicos):
    super().__init__(nome, nome_cien, alimentacao, reproducao, esqueleto, coluna)
    self.mamarias = mamarias
    self.endotermicos = endotermicos

  def amamentar(self):
    print(f'o animal {self.nome} está amamentando')

class Ornitorrinco(Mamiferos):
  def __init__(self, nome, nome_cien, alimentacao, reproducao, esqueleto, coluna, mamarias, endotermicos, bico, habitat):
    super().__init__(nome, nome_cien, alimentacao, reproducao, esqueleto, coluna, mamarias, endotermicos)
    self.bico = bico
    self.habitat = habitat
  
  def nadar(self):
    print(f'O {self.nome} está nadando')

class Morcego(Mamiferos):
  def __init__(self, nome, nome_cien, alimentacao, reproducao, esqueleto, coluna, mamarias, endotermicos, asas, sonar):
    super().__init__(nome, nome_cien, alimentacao, reproducao, esqueleto, coluna, mamarias, endotermicos)
    self.asas = asas
    self.sonar = sonar
  
  def voar(self):
    print(f'O {self.nome} está voando')

class Baleia(Mamiferos):
  def __init__(self, nome, nome_cien, alimentacao, reproducao, esqueleto, coluna, mamarias, endotermicos, tamanho, peso):
    super().__init__(nome, nome_cien, alimentacao, reproducao, esqueleto, coluna, mamarias, endotermicos)
    self.tamanho = tamanho
    self.peso = peso
    
  def borrifar(self):
    print(f'o {self.nome} borrifou')

ornitorrinco = Ornitorrinco(
    nome="Ornitorrinco",
    nome_cien="Ornithorhynchus anatinus",
    alimentacao="Insetos e crustáceos",
    reproducao="Ovo",
    esqueleto=True,
    coluna=True,
    mamarias=True,
    endotermicos=True,
    bico="Bico de pato",
    habitat="Rios e lagos da Austrália"
)

morcego = Morcego(
    nome="Morcego",
    nome_cien="Chiroptera",
    alimentacao="Frutos e insetos",
    reproducao='Sexuada',
    esqueleto=True,
    coluna=True,
    mamarias=True,
    endotermicos=True,
    asas=True,
    sonar=True
)

baleia = Baleia(
    nome="Baleia",
    nome_cien="Balaenoptera musculus",
    alimentacao="Plâncton",
    reproducao="Sexuada",
    esqueleto=True,
    coluna=True,
    mamarias=True,
    endotermicos=True,
    tamanho="Até 30 metros",
    peso="Até 200 toneladas"
)
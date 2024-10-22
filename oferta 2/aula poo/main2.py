class Usuario:
  def __init__(self,nome, senha, email, telefone):
    self.nome = nome
    self.senha = senha
    self.email = email
    self.telefone = telefone
    self.max_emprestimo = 0

class Livro:
  def __init__(self, titulo, autor, genero, disponivel):
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.disponivel = disponivel

  @staticmethod
  def emprestar():
    if Livro.disponivel == True and Usuario.max_emprestimo <= 3:
      Livro.disponivel = False
      Usuario.max_emprestimo += 1
    else:
      print('Livro já emprestado')
  
  def cadastro(self):
    self.titulo = input()
    self.autor = input()
    self.genero = input()
    self.disponivel = True
  
  def listar(self):
    print(f'{self.titulo} - {self.autor}')

class Biblioteca:
  @staticmethod
  def devolucao():
    Livro.disponivel = True
    Usuario.max_emprestimo -= 1
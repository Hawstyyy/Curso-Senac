from pessoa import Pessoa
class Estudante(Pessoa):
  def __init__(self, nome, trabalho, idade, turma, media):
    super().__init__(nome, trabalho, idade)
    self.turma = turma
    self.media = media
  
  def printar(self):
    print(f"""
| Nome: {self.nome}
| Idade: {self.idade}
| Trabalho: {self.trabalho}
| Turma: {self.turma}
| Média: {self.media}
""")

  def tirar_nota():
    return True
  def estudar():
    return False

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
trabalho = input("Insira o seu trabalho: ")
turma = input("Insira a sua turma: ")
media = float(input("Insira a sua média: "))

x = Estudante(nome=nome, idade=idade, trabalho=trabalho, turma=turma, media=media)
x.printar()
from pessoa import Pessoa
class Trabalhador(Pessoa):
  def __init__(self, nome, idade, trabalho, salario, cargo, rico):
    super().__init__(nome, idade, trabalho)
    self.salario = salario
    self.cargo = cargo
    self.rico = rico

  def printar(self):
    print(f"""
| Nome: {self.nome}
| Idade: {self.idade}
| Trabalho: {self.trabalho}
| Salário: {self.salario}
| Cargo: {self.cargo}
| Rico? {self.rico}
""")

  def sofrer(self):
    return True
  def trabalhar(self):
    return False

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
trabalho = input("Insira o seu trabalho: ")
salario = float(input("Insira o seu salário: "))
cargo = input("Insira o seu cargo: ")
rico = "Falso"

x = Trabalhador(nome, idade, trabalho, salario, cargo, rico)

x.printar()
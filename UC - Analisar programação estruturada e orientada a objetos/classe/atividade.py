#Crie uma Classe de Empresa com atributos e comportamentos
print()

def gerar_nota():
  print("nota fiscal uau")
def trabalho_escravoexe():
  print("carteira de trabalho clt")

class Empresa:
  nome = ("governo do ms")
  cnpj = ("15.412.257/0001-28")
  ramo = ("governar")

  def detalhes(self):
    return self.nome, self.cnpj, self.ramo
  
  print("------------------------------------------------------------------")
  gerar_nota()
  trabalho_escravoexe()

empresa = Empresa()
print(empresa.detalhes())

class Pessoa:
  nome = "Vicente Mais ou  Menos da Silva"
  idade = 18
  cpf = "123.456.789-99"
  emprego = "CLT"
  salario = "salario? minimo"

  def detalhes_pessoa(self):
    return self.nome, self.idade, self.cpf, self.emprego, self.salario

pessoa = Pessoa()

print("------------------------------------------------------------------")
print(pessoa.detalhes_pessoa())
print("------------------------------------------------------------------")

print()
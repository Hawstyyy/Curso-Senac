from Carroceria import Carroceria

class Habilitacao(Carroceria):
  def __init__(self, nome, tipo_veiculo,tracao, quantidade_rodas, peso, tipo_motor, preco, carroceria, quant_pessoa):
    super().__init__(nome, tipo_veiculo,tracao, quantidade_rodas, peso, tipo_motor, preco, carroceria)
    self.quant_pessoa = quant_pessoa

  def tipo(self):
    if self.quantidade_rodas == 2:
      self.tipo_hab = "Habilitação para Motos"
      return "Habilitação para Motos"
    else:
      self.tipo_hab = "Habilitação para Carros"
      return "Habilitação para Carros"
    
  def pessoas(self):
    if self.quant_pessoa == 2:
      return "Moto/pequeno porte"
    elif self.quant_pessoa == 4:
      return "Carro"
    else:
      return "Grande Porte"
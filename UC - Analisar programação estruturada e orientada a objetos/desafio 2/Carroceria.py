from Tipocarro import Carro

class Carroceria(Carro):
  def __init__(self, nome, tipo_veiculo, tracao, quantidade_rodas, peso, tipo_motor, preco, carroceria):
    super().__init__(nome, tipo_veiculo, tracao, quantidade_rodas, peso, tipo_motor, preco)
    self.carroceria = carroceria

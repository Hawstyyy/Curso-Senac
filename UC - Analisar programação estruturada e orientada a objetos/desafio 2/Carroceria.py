from Tipocarro import Carro

class Carroceria(Carro):
  def __init__(self, nome, tipo_veiculo, tracao, quantidade_rodas, peso, tipo_motor, preco, potencia, carroceria):
    super().__init__(nome, tipo_veiculo, tracao, quantidade_rodas, peso, tipo_motor, preco, potencia)
    self.carroceria = carroceria

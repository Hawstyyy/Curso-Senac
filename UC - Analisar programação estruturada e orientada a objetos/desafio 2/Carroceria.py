from Tipocarro import Carro

class Carroceria(Carro):
  def __init__(self, nome, tracao, quantidade_rodas, peso, tipo_motor, carroceria):
    super().__init__(nome, tracao, quantidade_rodas, peso, tipo_motor)
    self.carroceria = carroceria

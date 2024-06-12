from Reino import Reino

class Filo(Reino):
  def __init__(self, tipo_celular, nutricao, nome_filo, reproducao):
    super().__init__(tipo_celular, nutricao)
    self.nome_filo = nome_filo
    self.reproducao = reproducao

from Filo import Filo

class Classe(Filo):
  def __init__(self, tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao):
    super().__init__(tipo_celular, nutricao, nome_filo, reproducao)
    self.sono_hab = sono_hab
    self.locomocao = locomocao
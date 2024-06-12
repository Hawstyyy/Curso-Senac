from Ordem import Ordem

class Familia(Ordem):
  def __init__(self, tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia):
    super().__init__(tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem)
    self.nome_familia = nome_familia
    self.caracteristica_familia = caracteristica_familia
from Familia import Familia

class Genero(Familia):
  def __init__(self, tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia, nome_genero, caracterisca_genero):
    super().__init__(tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia)
    self.nome_genero = nome_genero
    self.caracterisca_genero = caracterisca_genero

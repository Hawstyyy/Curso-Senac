from Genero import Genero

class Especie(Genero):
  def __init__(self, tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia, nome_genero, caracterisca_genero, tamanho_corporal, tipo_camuflagem):
    super().__init__(tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia, nome_genero, caracterisca_genero)
    self.tamanho_corporal = tamanho_corporal
    self.tipo_camuflagem = tipo_camuflagem
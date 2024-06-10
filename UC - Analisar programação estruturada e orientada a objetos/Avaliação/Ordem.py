from Classe import Classe
class Ordem(Classe):
 def __init__(self, tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao,nome_ordem,caracterisca_ordem):
  super().__init__(tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao)
  self.nome_ordem = nome_ordem
  self.caracterisca_ordem = caracterisca_ordem
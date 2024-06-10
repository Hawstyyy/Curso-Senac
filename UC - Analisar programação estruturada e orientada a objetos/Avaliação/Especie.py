from Genero import Genero

class Especie(Genero):
  def __init__(self, tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia, nome_genero, caracterisca_genero, tamanho_corporal, tipo_camuflagem):
    super().__init__(tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia, nome_genero, caracterisca_genero)
    self.tamanho_corporal = tamanho_corporal
    self.tipo_camuflagem = tipo_camuflagem
  
    def print_master():
      print(f"""
- Tipo celular: {self.tipo_celular}
- Nutrição: {self.nutricao}
- Nome do filo: {self.nome_filo}
- Reprodução: {self.reproducao}
- Hábito de sono: {self.sono_hab}
- Locomoção: {locomocao}
- Nome da ordem: {nome_ordem}
- Características da ordem: {caracterisca_ordem}
- Nome da Família: {self.nome_familia}
- Características da família: {self.caracteristica_familia}
- Nome do gênero: {self.nome_genero}
- Característica do gênero: {self.caracterisca_genero}
- Tamanho Corporal: {self.tamanho_corporal}""")
      if tipo_camuflagem == 'Ausente':
        pass
      else:
        print(f"- Tipo de Camuflagem: {self.tipo_camuflagem}")
from Genero import Genero

class Especie(Genero):
  def __init__(self, tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia, nome_genero, caracterisca_genero, tamanho_corporal, tipo_camuflagem):
    super().__init__(tipo_celular, nutricao, nome_filo, reproducao, sono_hab, locomocao, nome_ordem, caracterisca_ordem, nome_familia, caracteristica_familia, nome_genero, caracterisca_genero)
    self.tamanho_corporal = tamanho_corporal
    self.tipo_camuflagem = tipo_camuflagem
  
    def print_master(animal):
      print(f"""
- Tipo celular: {animal.tipo_celular}
- Nutrição: {animal.nutricao}
- Nome do filo: {animal.nome_filo}
- Reprodução: {animal.reproducao}
- Hábito de sono: {animal.sono_hab}
- Locomoção: {animal.locomocao}
- Nome da ordem: {animal.nome_ordem}
- Características da ordem: {animal.caracterisca_ordem}
- Nome da Família: {animal.nome_familia}
- Características da família: {animal.caracteristica_familia}
- Nome do gênero: {animal.nome_genero}
- Característica do gênero: {animal.caracterisca_genero}
- Tamanho Corporal: {animal.tamanho_corporal}
- Tipo de Camuflagem: {animal.tipo_camuflagem}""")
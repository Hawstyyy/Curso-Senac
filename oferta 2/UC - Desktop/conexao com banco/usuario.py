from db import db
class Usuario:
  def __init__(self, db_name):
    self.db = db(db_name)
    self.db.conectar()
  
  def criarUsuario(self, nome, email):
    query = "insert into usuario (nome, email) values (?, ?)"
    self.db.executar(query, (nome, email))
    self.db.commit()
  
  def listarUsuarios(self):
    query = "select * from usuarios"
    self.db.executar(query)
    dados = self.db.fetch()
    return dados
usuario = Usuario('bancoDados.db')

usuario.criarUsuario("Rafael", "Rafael@gmail.com")
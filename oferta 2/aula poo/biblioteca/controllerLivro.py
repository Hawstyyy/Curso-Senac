from livro import Livro
from database import Database
import mysql.connector

class controllerLivro:
  def inserirLivro(self):
    db = Database()
    db.conectar()
    db.executarQuery(Livro('tete','teste','testando', 123).inserirLivro())
    db.desconectar()

controllerLivro().inserirLivro()
import sqlite3
import os
import sys

class db:
  def __init__(self, dbname) -> None:
    self.dbname = dbname
    self.conn = None
    self.cursor = None

  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))

  def conectar(self):
    self.conn = sqlite3.connect(f'{self.basePath()}/{self.dbname}')
    self.cursor = self.conn.cursor()

  def commit(self):
    if self.conn:
      self.conn.commit()
  
  def executar(self, query, parametros=None):
    if parametros:
      self.cursor.execute(query,parametros)
    else:
      self.cursor.execute(query)
    self.commit()
  
  def fetch(self):
    return self.cursor.fetchall()

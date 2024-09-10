import mysql.connector as sql

def Connect():
  global conn
  conn = sql.connect(
    host="10.28.2.16",
    user="suporte",
    password="suporte",
    database="CadastrosEdni"
  )
  if conn.is_connected():
    print("Conectado")
  else:
    print("Foi nao pae")

def getUsers(user, password):
  cursor = conn.cursor(dictionary=True)
  print(user, password)
  if cursor.execute(f"select nome, senha from users where nome = '{user}' and senha = '{password}';"):
    print(cursor.fetchall())
  else:
    print("teste")
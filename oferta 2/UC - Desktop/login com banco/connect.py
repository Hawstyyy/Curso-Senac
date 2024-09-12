import mysql.connector as sql
from tkinter import messagebox
import requests, os, sys

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

def basePath():
  return os.path.dirname(os.path.abspath(sys.argv[0]))

def getUsers(user, password, user_text, url):
  cursor = conn.cursor(dictionary=True)
  cursor.execute(f"select senha from users where nome = '{user}';")
  rows = cursor.fetchone()
  if rows:
    for key, value in rows.items():
      if password != value:
        messagebox.showerror("Erro", "Senha Incorreta")
      else:
        cursor.execute(f"update users set texto = '{user_text}', image = '{url}' where nome = '{user}'")
        conn.commit()
        messagebox.showinfo("Sucesso", f"Bem-vindo ao Senac! Abrindo seu perfil...")
        download = requests.get(url)
        filename = url.split('/')[-1]
        with open(f'{basePath()}/{filename}', 'wb') as file:
          file.write(download.content)
  else:
    return messagebox.askokcancel("Erro","Usuário não encontrado, gostaria de cadastrar um?")

def signUser(user, password):
  cursor = conn.cursor(dictionary=True)
  cursor.execute(f"select senha from users where nome = '{user}';")
  rows = cursor.fetchone()
  if rows:
    messagebox.showerror("Erro", "Usuário já cadastrado")
  else:
    cursor.execute(f"insert into users(nome, senha) values ('{user}', '{password}');")
    conn.commit()
    messagebox.showinfo("Sucesso", f"Bem-vindo ao Senac! Sinta-se livre para logar agora!")
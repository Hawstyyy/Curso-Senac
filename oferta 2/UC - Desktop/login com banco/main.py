import customtkinter as CTk
from PIL import Image
import os, sys
from connect import Connect,getUsers
from cadastro import Cadastro

def basePath():
  return os.path.dirname(os.path.abspath(sys.argv[0]))

def entrada(root, text, width, fg, textcolor, pady):
  entry = CTk.CTkEntry(root, placeholder_text=text, width=width, fg_color=fg, text_color=textcolor)
  entry.pack(pady=pady)
  return entry

def Submit(user, password, user_text):
  Connect()
  if getUsers(user.get(), password.get(), user_text.get()):
    root.destroy()
    Cadastro().startApp()
  else:
    root.destroy()


root = CTk.CTk()
root.geometry("600x500")
root.title("Login")
root.resizable(False, False)
root.iconbitmap(f'{basePath()}/Senac_logo.ico')

logo = CTk.CTkImage(Image.open(f'{basePath()}/Senac_logo.png'), size=(150, 100))
logo_label = CTk.CTkLabel(root, image=logo, text="")
logo_label.pack(pady=20)

texto = CTk.CTkLabel(root, text="Bem-vindo ao Senac!", width=200, height=100, font=("Arial", 20, "bold"))
texto.pack()

user = entrada(root, "Insira seu usuário", 350, "white", "black", 10)
password = entrada(root, "Insira sua senha", 350, "white", "black", 10)
user_text = entrada(root, "Insira seu texto", 350, "white", "black", 10)

submit = CTk.CTkButton(root, text="Fazer Login", command= lambda: Submit(user, password, user_text))
submit.pack(pady=30)

root.mainloop()
import customtkinter as CTk
from PIL import Image
import os, sys
from connect import Connect, signUser

class Cadastro:
  def __init__(self) -> None:
    pass

  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))

  def Entrada(self, root, text, width, fg, textcolor, pady):
    entry = CTk.CTkEntry(root, placeholder_text=text, width=width, fg_color=fg, text_color=textcolor)
    entry.pack(pady=pady)
    return entry
  
  def Submit(self, user, password, main):
    Connect()
    signUser(user.get(), password.get())
    root.destroy()
    main.deiconify()

  def startApp(self, main):
    global root
    root = CTk.CTkToplevel()
    root.geometry("600x500")
    root.title("Login")
    root.resizable(False, False)
    root.iconbitmap(f'{self.basePath()}/Senac_logo.ico')

    logo = CTk.CTkImage(Image.open(f'{self.basePath()}/Senac_logo.png'), size=(150, 100))
    logo_label = CTk.CTkLabel(root, image=logo, text="")
    logo_label.pack(pady=20)

    texto = CTk.CTkLabel(root, text="Bem-vindo ao Cadastro do Senac!", width=200, height=100, font=("Arial", 20, "bold"))
    texto.pack()

    user = self.Entrada(root, "Insira seu usuário", 350, "white", "black", 10)
    password = self.Entrada(root, "Insira sua senha", 350, "white", "black", 10)

    submit = CTk.CTkButton(root, text="Fazer Cadastro", command= lambda: self.Submit(user, password, main))
    submit.pack(pady=30)
    root.mainloop()


if __name__ == "__main__":
  Cadastro().startApp()
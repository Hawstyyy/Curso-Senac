import customtkinter as CTk
import os, sys, requests
from connect import Connect

class CadastroImagem:
  def __init__(self) -> None:
    pass

  def Entrada(self, root, text, width, fg, textcolor, pady):
    entry = CTk.CTkEntry(root, placeholder_text=text, width=width, fg_color=fg, text_color=textcolor)
    entry.pack(pady=pady)
    return entry
  
  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))
  
  def mandarImagem(self):
    Connect()

  def startApp(self, root):
    toplevel = CTk.CTkToplevel(root)
    toplevel.geometry("400x200")
    toplevel.resizable(False, False)
    toplevel.title('Selecionar imagem')
    toplevel.iconbitmap(f'{self.basePath()}/Senac_logo.ico')

    url = self.Entrada(toplevel, 'Insira o link de sua imagem', 350, 'white', 'black', 20)
    submit = CTk.CTkButton(toplevel, text="Mandar Imagem", command= lambda: self.Donwload(url), corner_radius=20)
    submit.pack()

    toplevel.mainloop()

if __name__ == "__main__":
  CadastroImagem().startApp()
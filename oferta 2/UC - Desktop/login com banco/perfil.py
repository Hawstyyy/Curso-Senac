import customtkinter as CTk
from PIL import Image
import os, sys
from connect import Connect

class Perfil:
  def __init__(self) -> None:
    pass

  def basePath(self):
    return os.path.dirname(os.path.abspath(sys.argv[0]))

  def startApp(self, user, user_text, url):
    root = CTk.CTk()
    root.geometry('400x500')
    root.title('Seu perfil')
    root.resizable(False, False)
    root.iconbitmap(f'{self.basePath()}/Senac_logo.ico')
    filename = url.split('/')[-1]
    
    perfil = CTk.CTkImage(Image.open(f'{self.basePath()}/user.png'), size=(150, 150))
    perfil_label = CTk.CTkLabel(root, image=perfil, text="")
    perfil_label.pack(pady=20)

    nome = CTk.CTkLabel(root, text=f'{user}', font=("Arial", 20, "bold"))
    nome.pack()
    texto = CTk.CTkLabel(root, text=f'{user_text}')
    texto.pack()

    imagem_registrada = CTk.CTkLabel(root, text="Imagem registrada:", font=("Arial", 20, "bold"))
    imagem_registrada.pack()

    imagem = CTk.CTkImage(Image.open(f'{self.basePath()}\\{filename}'), size=(200, 150))
    imagem_label = CTk.CTkLabel(root, image=imagem, text="")
    imagem_label.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
  Perfil().startApp("admin", "texto", 'https://img.elo7.com.br/product/zoom/4A29F43/imagem-alta-resolucao-para-quadro-ceu-01-quadro.jpg')
from tkinter import *
from tkinter import messagebox, ttk, PhotoImage

class Entradas:
  def __init__(self) -> None:
    self.imagens = []
    self.root = Toplevel()

  def resizeImg(self, img, rely, relx, anchor):
    img = PhotoImage(file=f"{img}.png")
    factor_width = img.width() / 200
    factor_height = img.height() / 200

    factor = max(factor_width, factor_height)
    if factor > 1:
      img = img.subsample(int(factor))
    self.imagens.append(img)

    image_label = Label(self.root, image=img)
    image_label.place(rely=rely, relx=relx, anchor=anchor)

  def start_ent(self):
    
    self.root.title("Restaurante do Ederson")
    self.root.state('zoomed')

    self.resizeImg("1", 0.2, 0.2, CENTER)
    title = Label(self.root, text="Bruschetta de Tomate e Manjericão", font=("Arial", 16, "bold"))
    title.place(relx=0.2, rely=0.3, anchor=CENTER)
    preco = Label(self.root, text="R$ 24.00", font=("Arial", 16))
    preco.place(relx=0.2, rely=0.33, anchor=CENTER)
    botao = ttk.Button(self.root, text="Adicionar")
    botao.place(relx=0.2, rely=0.37, anchor=CENTER)

    self.resizeImg("2", 0.2, 0.5, CENTER)
    titleTartare = Label(self.root, text="Tartare de Salmão com Abacate", font=("Arial", 16, "bold"))
    titleTartare.place(relx=0.5, rely=0.3, anchor=CENTER)
    precoTartare = Label(self.root, text="R$ 32.00", font=("Arial", 16))
    precoTartare.place(relx=0.5, rely=0.33, anchor=CENTER)
    botaoTartare = ttk.Button(self.root, text="Adicionar")
    botaoTartare.place(relx=0.5, rely=0.37, anchor=CENTER)

    self.resizeImg("3", 0.2, 0.8, CENTER)
    titleRolinho = Label(self.root, text="Rolinho Primavera com Molho Agridoce", font=("Arial", 16, "bold"))
    titleRolinho.place(relx=0.8, rely=0.3, anchor=CENTER)
    precoRolinho = Label(self.root, text="R$ 28.00", font=("Arial", 16))
    precoRolinho.place(relx=0.8, rely=0.33, anchor=CENTER)
    botaoRolinho = ttk.Button(self.root, text="Adicionar")
    botaoRolinho.place(relx=0.8, rely=0.37, anchor=CENTER)

    self.resizeImg("4", 0.7, 0.4, CENTER)
    titleSopa = Label(self.root, text="Sopa de Cogumelos", font=("Arial", 16, "bold"))
    titleSopa.place(relx=0.4, rely=0.8, anchor=CENTER)
    precoSopa = Label(self.root, text="R$ 22.00", font=("Arial", 16))
    precoSopa.place(relx=0.4, rely=0.83, anchor=CENTER)
    botaoSopa = ttk.Button(self.root, text="Adicionar")
    botaoSopa.place(relx=0.4, rely=0.87, anchor=CENTER)

    self.resizeImg("5", 0.7, 0.6, CENTER)
    titleSalada = Label(self.root, text="Salada Caesar", font=("Arial", 16, "bold"))
    titleSalada.place(relx=0.6, rely=0.8, anchor=CENTER)
    precoSalada = Label(self.root, text="R$ 25.00", font=("Arial", 16))
    precoSalada.place(relx=0.6, rely=0.83, anchor=CENTER)
    botaoSalada = ttk.Button(self.root, text="Adicionar")
    botaoSalada.place(relx=0.6, rely=0.87, anchor=CENTER)


    self.root.mainloop()

if __name__ == "__main__":
  Entradas().start_ent()
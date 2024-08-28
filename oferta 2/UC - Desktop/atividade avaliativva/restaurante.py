from tkinter import *
from tkinter import ttk
from entradas import Entradas
from pratos import PratosPrincipais
from bebidas import BebidasNaoAlcoolicas
from bebidasalcoolicas import BebidasAlcoolicas
from sobremesa import Sobremesas
from menu import MenuChefe

class Restaurante():
  def __init__(self, usuario) -> None:
    self.usuario = usuario

  def entradaButton(self):
    Entradas().start_ent()
  
  def pratoButton(self):
    PratosPrincipais().start_ent()

  def bebidas(self):
    BebidasNaoAlcoolicas().start_ent()

  def bebidasAlcoolicas(self):
    BebidasAlcoolicas().start_ent()

  def sobremesa(self):
    Sobremesas().start_ent()

  def menu(self):
    MenuChefe().start_ent()

  def start_res(self):
    root = Tk()
    root.title("Restaurante do Ederson")
    root.state('zoomed')

    img = PhotoImage(file="0.png")

    factor_width = img.width() / 350
    factor_height = img.height() / 350

    factor = max(factor_width, factor_height)

    if factor > 1:
        img = img.subsample(int(factor))

    image_label = Label(root, image=img)
    image_label.place(rely=0.15, relx=0.5, anchor=CENTER)

    Label(root, text=f"Olá, {self.usuario}!", font=("Arial", 20)).place(relx=0.5, rely=0.7, anchor=CENTER)

    entradas = ttk.Button(root, text="Entradas", width=50, padding=10, command=self.entradaButton)
    entradas.place(relx=0.5, rely=0.35, anchor=CENTER)

    pratos = ttk.Button(root, text="Pratos principais", width=50, padding=10, command=self.pratoButton)
    pratos.place(relx=0.5, rely=0.4, anchor=CENTER)

    bebidas = ttk.Button(root, text="Bebidas", width=50, padding=10, command=self.bebidas)
    bebidas.place(relx=0.5, rely=0.45, anchor=CENTER)

    alcool = ttk.Button(root, text="Bebidas Alcoólicas", width=50, padding=10, command=self.bebidasAlcoolicas)
    alcool.place(relx=0.5, rely=0.5, anchor=CENTER)

    sobremesas = ttk.Button(root, text="Sobremesas", width=50, padding=10, command=self.sobremesa)
    sobremesas.place(relx=0.5, rely=0.55, anchor=CENTER)

    menu = ttk.Button(root, text="Menu do Chef", width=50, padding=10, command=self.menu)
    menu.place(relx=0.5, rely=0.60, anchor=CENTER)

    root.mainloop()

if __name__ == "__main__":
  Restaurante("admin").start_res()
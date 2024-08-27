from tkinter import *
from tkinter import messagebox, ttk

class Restaurante():
  def __init__(self, usuario) -> None:
    self.usuario = usuario
  def start_res(self):
    root = Tk()
    root.title("Restaurante do Ederson")
    root.state('zoomed')

    Label(root, text=f"Olá, {self.usuario}!", font=("Arial", 20)).place(relx=0.5, rely=0.3, anchor=CENTER)
    ttk.Button(root, text="Entrada")
    root.mainloop()
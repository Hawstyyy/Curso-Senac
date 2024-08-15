from tkinter import *
from tkinter import ttk

def teste():
  global cliques
  cliques += 1
  btn.config(text=f"conta {cliques}")

root = Tk()

if __name__ == "__main__":
  frm = ttk.Frame(root ,padding=50)
  frm.grid()
  ttk.Label(frm, text="Aperta ai duvido", font=("Arial", 20) ).grid(column=1,row=1)
  
  cliques = 0
  btn = ttk.Button(frm, text=f"conta {cliques}", command=teste)
  btn.grid(column=1, row=3)
  root.mainloop()
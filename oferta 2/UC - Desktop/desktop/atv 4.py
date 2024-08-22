from tkinter import *
from tkinter import messagebox, ttk

root = Tk()
root.geometry("600x400")
root.title("Botões")

def preto():
  btn.config(bg='Black', fg='White')
  root.config(bg='Black')
def roxo():
  btn2.config(bg='Purple', fg='White')
  root.config(bg='Purple')
def branco():
  btn3.config(bg='White', fg='Black')
  root.config(bg='White')

btn = Button(root, text="Preto", command=preto)
btn.place(relx=0.5, rely=0.5, anchor="center", width=100)
btn2 = Button(root, text="Roxo", command=roxo)
btn2.place(relx=0.5, rely=0.4, anchor="center", width=100)
btn3 = Button(root, text="Branco", command=branco)
btn3.place(relx=0.5, rely=0.3, anchor="center", width=100)

root.mainloop()

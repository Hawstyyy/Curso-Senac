from tkinter import *
from tkinter import ttk, filedialog

def diretorio():
  folder_selected = filedialog.askdirectory()
  folder_label.config(text=folder_selected)

root = Tk()

root.geometry("500x400")
root.resizable(False, False)

ttk.Label(root, text="Pasta selecionada:").place(relx=0.5, rely=0.35, anchor=CENTER)

folder_label = ttk.Label(root)
folder_label.place(relx=0.5, rely=0.4, anchor=CENTER)

btn1 = Button(root, text="Selecionar pasta", command=diretorio, height=2, width=20)
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()

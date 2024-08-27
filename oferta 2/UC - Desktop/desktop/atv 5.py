from tkinter import *
from tkinter import ttk, messagebox
from tkinter import PhotoImage

root = Tk()
root.geometry("600x400")
root.title("Galeria")

atual = 0

def proximo():
  global atual, img1,image_label
  try:
    img1 = PhotoImage(file=f"./{atual}.png")
    image_label = Label(root, image=img1, width=300, height=300).place(rely=0.5,relx=0.5,anchor=CENTER)
  except:
    messagebox.showinfo("Fim", "Não há mais imagens")
  atual += 1

def anterior():
  global atual, img1,image_label
  atual -= 1
  try:
    img1 = PhotoImage(file=f"./{atual}.png")
    image_label = Label(root, image=img1, width=300, height=300).place(rely=0.5,relx=0.5,anchor=CENTER)
  except:
    messagebox.showinfo("Fim", "Não há mais imagens")

def comentar():
    global comentario_entry
    comentario_text = comentario_entry.get()
    coment.config(text=comentario_text)

btn = ttk.Button(root, text="Próximo", command=proximo)
btn.place(rely=0.5,relx=0.9,anchor=CENTER)

coment = ttk.Label(root, text="nenhum")
coment.place(rely=0.1,relx=0.5,anchor=CENTER)

comentario_entry = Entry(root)
comentario_entry.place(relx=0.5, rely=0.9, anchor=CENTER, width=180)

btn = ttk.Button(root, text="Comentar", command=comentar)
btn.place(rely=0.95,relx=0.5,anchor=CENTER)

root.mainloop()
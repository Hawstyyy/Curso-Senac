from tkinter import *
from tkinter import ttk, messagebox
from tkinter import PhotoImage


images = ["moyai1.png", "moyai2.png"]

root = Tk()
root.geometry("600x400")
root.title("Galeria")

atual = 0

def proximo():
  global atual, img1,image_label
  try:
    img1 = PhotoImage(file=f"C:\\Users\\EnzoLopez\\Documents\\github\\Curso-Senac\\oferta 2\\UC - Desktop\\desktop\\assets\\{atual}.png")
  except:
    messagebox.showinfo("Fim", "Não há mais imagens")
  image_label = Label(root, image=img1, width=300, height=300).place(rely=0.5,relx=0.5,anchor=CENTER)
  atual += 1

def comentar():
  global comentario

  texto = ttk.Label(root, text="Escreva seu comentário", font=("Arial", 12, "bold"))
  texto.place(relx=0.5, rely=0.4, anchor=CENTER)

  comentario = Entry(root)
  comentario.place(relx=0.5, rely=0.5, anchor=CENTER, width=180)
  coment.config(text=comentario.get())
  

btn = ttk.Button(root, text="Próximo", command=proximo)
btn.place(rely=0.5,relx=0.9,anchor=CENTER)

coment = ttk.Label(root, text="")
coment.place(rely=0.1,relx=0.5,anchor=CENTER)

btn = ttk.Button(root, text="Comentar", command=comentar)
btn.place(rely=0.95,relx=0.5,anchor=CENTER)

root.mainloop()
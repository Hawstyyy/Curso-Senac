from tkinter import *
from tkinter import messagebox,ttk

def verificar():
  if usuario.get() == "" and senha.get() == "" and senhaConfirmar.get() == "":
    messagebox.showerror("Erro", "Por favor preencha todas as opções")
  elif usuario.get() == "" or senha.get() == "" or senhaConfirmar.get() == "":
    messagebox.showerror("Erro", "Campo não preenchido, confira os campos de cadastro e tente novamente")
  elif senhaConfirmar.get() != senha.get():
    messagebox.showerror("Erro", "As senhas não se coincidem")
  elif senha.get() == usuario.get():
    messagebox.showerror("Erro", "O usuário e a senha não podem serem iguais")
  else:
    messagebox.showinfo("Sucesso", f"O usuário {usuario.get()} foi cadastrado com sucesso")

root = Tk()
root.geometry("600x400")
root.title("Tela de cadastro")

Label(root, text="Usuário:", font=("Arial", 10, "bold")).place(relx=0.39, rely=0.25, anchor="center")
usuario = Entry(root, width=30)
usuario.place(relx=0.5, rely=0.3, anchor="center")

Label(root, text="Senha:", font=("Arial", 10, "bold")).place(relx=0.38, rely=0.4, anchor="center")
senha = Entry(root, width=30, show="*")
senha.place(relx=0.5, rely=0.45, anchor="center")

Label(root, text="Confirmar Senha:", font=("Arial", 10, "bold")).place(relx=0.44, rely=0.55, anchor="center")
senhaConfirmar = Entry(root, width=30, show="*")
senhaConfirmar.place(relx=0.5, rely=0.6, anchor="center")

btn = ttk.Button(root, text="Cadastrar", command=verificar, style='custom.TButton')
btn.place(relx=0.5, rely=0.77, anchor="center")

root.mainloop()
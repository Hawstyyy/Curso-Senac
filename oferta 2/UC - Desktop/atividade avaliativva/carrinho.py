import json
from tkinter import *
from tkinter import ttk, messagebox

class Carrinho:
    def __init__(self) -> None:
        self.carrinho = {}
        self.preco = 0
        self.root = None
        self.item_var = None
        self.item_menu = None
        self.preco_label = None
        self.carregarCarrinho()

    def criarTelaCarrinho(self):
        if self.root is None or not self.root.winfo_exists():
            self.root = Toplevel()
            self.root.title("Carrinho")
            self.root.state('zoomed')
            
            Label(self.root, text="Itens no Carrinho:", font=("Arial", 16, "bold")).place(relx=0.5, rely=0.05, anchor=CENTER)
            
            self.carrinho_text = Text(self.root, height=20, width=50)
            self.carrinho_text.place(relx=0.5, rely=0.2, anchor=CENTER)
            
            self.atualizarTelaCarrinho()
            
            Label(self.root, text="Remover Item:", font=("Arial", 14)).place(relx=0.5, rely=0.75, anchor=CENTER)
            
            self.item_var = StringVar(self.root)
            self.item_menu = OptionMenu(self.root, self.item_var, *self.carrinho.keys())
            self.item_menu.place(relx=0.5, rely=0.8, anchor=CENTER)
            
            self.remover_button = ttk.Button(self.root, text="Remover", command=self.removerItem)
            self.remover_button.place(relx=0.5, rely=0.85, anchor=CENTER)
            
            ttk.Button(self.root, text="Fechar", command=self.root.destroy).place(relx=0.5, rely=0.9, anchor=CENTER)
            
            self.preco_label = Label(self.root, text=f"Preço Total: R$ {self.preco:.2f}", font=("Arial", 14, "bold"))
            self.preco_label.place(relx=0.5, rely=0.95, anchor=CENTER)

    def adicionarCarrinho(self, nome, preco):
        if nome in self.carrinho:
            self.preco -= self.carrinho[nome]
        self.carrinho[nome] = preco
        self.preco += preco
        self.salvarCarrinho()
        self.atualizarTelaCarrinho()

    def removerCarrinho(self, nome):
        if nome in self.carrinho:
            preco_item = self.carrinho.pop(nome)
            self.preco -= preco_item
            self.salvarCarrinho()
            self.atualizarTelaCarrinho()

    def salvarCarrinho(self):
        with open('carrinho.json', 'w') as file:
            json.dump({'carrinho': self.carrinho, 'preco': self.preco}, file)

    def carregarCarrinho(self):
        try:
            with open('carrinho.json', 'r') as file:
                dados = json.load(file)
                self.carrinho = dados.get('carrinho', {})
                self.preco = dados.get('preco', 0)
        except FileNotFoundError:
            pass

    def atualizarTelaCarrinho(self):
        if hasattr(self, 'carrinho_text'):
            self.carrinho_text.delete(1.0, END)
            for item, preco in self.carrinho.items():
                self.carrinho_text.insert(END, f"{item}: R$ {preco:.2f}\n")
            self.atualizarMenuItems()
            self.atualizarPreco()

    def atualizarMenuItems(self):
        if self.item_menu:
            menu = self.item_menu['menu']
            menu.delete(0, 'end')
            for item in self.carrinho.keys():
                menu.add_command(label=item, command=lambda value=item: self.item_var.set(value))

    def atualizarPreco(self):
        if self.preco_label:
            self.preco_label.config(text=f"Preço Total: R$ {self.preco:.2f}")

    def removerItem(self):
        item = self.item_var.get()
        if item:
            self.removerCarrinho(item)
        else:
            messagebox.showwarning("Aviso", "Selecione um item para remover.")

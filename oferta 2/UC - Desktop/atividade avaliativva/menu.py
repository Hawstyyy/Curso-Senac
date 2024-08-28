from tkinter import *
from tkinter import ttk, PhotoImage
from carrinho import Carrinho

class MenuChefe:
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

    def Label(self, text, font, size, style, x, y):
        self.title = Label(self.root, text=text, font=(font, size, style))
        self.title.place(relx=x, rely=y, anchor=CENTER)

    def botao(self, text, command, x, y):
        botao = ttk.Button(self.root, text=text, command=command)
        botao.place(relx=x, rely=y, anchor=CENTER)

    def start_ent(self):
        carrinho = Carrinho()
        self.root.title("Cardápio de Pratos Principais")
        self.root.state('zoomed')

        self.resizeImg("26", 0.2, 0.2, CENTER)
        self.Label("Espaguete à Carbonara", "Arial", 16, "bold", 0.2, 0.3)
        self.Label("R$ 32.00", "Arial", 16, "bold", 0.2, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Espaguete à Carbonara", 32.00), 0.2, 0.37)

        self.resizeImg("27", 0.2, 0.5, CENTER)
        self.Label("Curry de Frango", "Arial", 16, "bold", 0.5, 0.3)
        self.Label("R$ 34.00", "Arial", 16, "bold", 0.5, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Curry de Frango", 34.00), 0.5, 0.37)

        self.resizeImg("28", 0.2, 0.8, CENTER)
        self.Label("Ribeye Steak", "Arial", 16, "bold", 0.8, 0.3)
        self.Label("R$ 50.00", "Arial", 16, "", 0.8, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Ribeye Steak", 50.00), 0.8, 0.37)

        self.resizeImg("29", 0.7, 0.4, CENTER)
        self.Label("Pasta ao Pesto", "Arial", 16, "bold", 0.4, 0.8)
        self.Label("R$ 28.00", "Arial", 16, "", 0.4, 0.83)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Pasta ao Pesto", 28.00), 0.4, 0.87)

        self.resizeImg("30", 0.7, 0.6, CENTER)
        self.Label("Chili com Carne", "Arial", 16, "bold", 0.6, 0.8)
        self.Label("R$ 36.00", "Arial", 16, "", 0.6, 0.83)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Chili com Carne", 36.00), 0.6, 0.87)

        self.botao("Sair", self.root.destroy, 0.9, 0.9)

        self.root.mainloop()

if __name__ == "__main__":
    MenuChefe().start_ent()

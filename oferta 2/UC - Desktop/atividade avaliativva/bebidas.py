from tkinter import *
from tkinter import ttk, PhotoImage
from carrinho import Carrinho

class BebidasNaoAlcoolicas:
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
        self.root.title("Restaurante do Ederson")
        self.root.state('zoomed')

        self.resizeImg("11", 0.2, 0.2, CENTER)
        self.Label("Suco de Laranja", "Arial", 16, "bold", 0.2, 0.3)
        self.Label("R$ 12.00", "Arial", 16, "bold", 0.2, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Suco de Laranja", 12.00), 0.2, 0.37)

        self.resizeImg("12", 0.2, 0.5, CENTER)
        self.Label("Água Mineral", "Arial", 16, "bold", 0.5, 0.3)
        self.Label("R$ 5.00", "Arial", 16, "bold", 0.5, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Água Mineral", 5.00), 0.5, 0.37)

        self.resizeImg("13", 0.2, 0.8, CENTER)
        self.Label("Refrigerante", "Arial", 16, "bold", 0.8, 0.3)
        self.Label("R$ 8.00", "Arial", 16, "", 0.8, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Refrigerante", 8.00), 0.8, 0.37)

        self.resizeImg("14", 0.7, 0.4, CENTER)
        self.Label("Suco de Maçã", "Arial", 16, "bold", 0.4, 0.8)
        self.Label("R$ 12.00", "Arial", 16, "", 0.4, 0.83)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Suco de Maçã", 12.00), 0.4, 0.87)

        self.resizeImg("15", 0.7, 0.6, CENTER)
        self.Label("Chá Gelado", "Arial", 16, "bold", 0.6, 0.8)
        self.Label("R$ 10.00", "Arial", 16, "", 0.6, 0.83)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Chá Gelado", 10.00), 0.6, 0.87)

        self.botao("Sair", self.root.destroy, 0.9, 0.9)

        self.root.mainloop()

if __name__ == "__main__":
    BebidasNaoAlcoolicas().start_ent()

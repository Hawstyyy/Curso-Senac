from tkinter import *
from tkinter import ttk, PhotoImage
from carrinho import Carrinho

class BebidasAlcoolicas:
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
        self.root.title("Cardápio de Bebidas Alcoólicas")
        self.root.state('zoomed')

        self.resizeImg("16", 0.2, 0.2, CENTER)
        self.Label("Caipirinha", "Arial", 16, "bold", 0.2, 0.3)
        self.Label("R$ 15.00", "Arial", 16, "bold", 0.2, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Caipirinha", 15.00), 0.2, 0.37)

        self.resizeImg("17", 0.2, 0.5, CENTER)
        self.Label("Cerveja Artesanal", "Arial", 16, "bold", 0.5, 0.3)
        self.Label("R$ 20.00", "Arial", 16, "bold", 0.5, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Cerveja Artesanal", 20.00), 0.5, 0.37)

        self.resizeImg("18", 0.2, 0.8, CENTER)
        self.Label("Vinho Tinto", "Arial", 16, "bold", 0.8, 0.3)
        self.Label("R$ 18.00", "Arial", 16, "", 0.8, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Vinho Tinto", 18.00), 0.8, 0.37)

        self.resizeImg("19", 0.7, 0.4, CENTER)
        self.Label("Mojito", "Arial", 16, "bold", 0.4, 0.8)
        self.Label("R$ 16.00", "Arial", 16, "", 0.4, 0.83)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Mojito", 16.00), 0.4, 0.87)

        self.resizeImg("20", 0.7, 0.6, CENTER)
        self.Label("Whisky", "Arial", 16, "bold", 0.6, 0.8)
        self.Label("R$ 19.00", "Arial", 16, "", 0.6, 0.83)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Whisky", 19.00), 0.6, 0.87)

        self.botao("Sair", self.root.destroy, 0.9, 0.9)

        self.root.mainloop()

if __name__ == "__main__":
    BebidasAlcoolicas().start_ent()
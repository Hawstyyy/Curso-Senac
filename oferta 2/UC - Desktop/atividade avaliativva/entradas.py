from tkinter import *
from tkinter import ttk, PhotoImage
from carrinho import Carrinho

# Cria uma instância global do carrinho
carrinho = Carrinho()

class Entradas:
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
        self.root.title("Restaurante do Ederson")
        self.root.state('zoomed')

        self.resizeImg("1", 0.2, 0.2, CENTER)
        self.Label("Bruschetta de Tomate e Manjericão", "Arial", 16, "bold", 0.2, 0.3)
        self.Label("R$ 24.00", "Arial", 16, "bold", 0.2, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Bruschetta de Tomate e Manjericão", 24.00), 0.2, 0.37)

        self.resizeImg("2", 0.2, 0.5, CENTER)
        self.Label("Tartare de Salmão com Abacate", "Arial", 16, "bold", 0.5, 0.3)
        self.Label("R$ 32.00", "Arial", 16, "bold", 0.5, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("Tartare de Salmão com Abacate", 32.00), 0.5, 0.37)

        self.resizeImg("3", 0.2, 0.8, CENTER)
        self.Label("Rolinho Primavera com Molho Agridoce", "Arial", 16, "bold", 0.8, 0.3)
        self.Label("R$ 28.00", "Arial", 16, "", 0.8, 0.33)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("rolinho_primavera", 28.00), 0.8, 0.37)

        self.resizeImg("4", 0.7, 0.4, CENTER)
        self.Label("Sopa de Cogumelos", "Arial", 16, "bold", 0.4, 0.8)
        self.Label("R$ 22.00", "Arial", 16, "", 0.4, 0.83)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("sopa_cogumelos", 22.00), 0.4, 0.87)

        self.resizeImg("5", 0.7, 0.6, CENTER)
        self.Label("Salada Caesar", "Arial", 16, "bold", 0.6, 0.8)
        self.Label("R$ 25.00", "Arial", 16, "", 0.6, 0.83)
        self.botao("Adicionar", lambda: carrinho.adicionarCarrinho("salada_caesar", 25.00), 0.6, 0.87)

        self.botao("Sair", self.root.destroy, 0.9, 0.9)

        self.root.mainloop()

if __name__ == "__main__":
    Entradas().start_ent()

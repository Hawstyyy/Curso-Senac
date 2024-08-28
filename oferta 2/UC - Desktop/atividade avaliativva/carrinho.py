class Carrinho:
  def __init__(self) -> None:
    self.carrinho = []
    self.preco = 0
  def adicionarCarrinho(self,nome, preco):
    self.carrinho.append(nome)
    self.preco += preco
    print(self.carrinho)
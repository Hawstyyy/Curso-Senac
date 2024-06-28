import random as r

class Tabela:
  sorteado = []
  b = []
  i = []
  n = []
  g = []
  o = []

  def gerar_num(self):
    while len(self.b) < 5:
      numero = r.randint(1,15)

      if len(self.sorteado) > 1:
        if numero not in self.sorteado:
          self.sorteado.append(numero)
          self.b.append(numero)
        else:
          continue
      else:
        self.sorteado.append(numero)
        self.b.append(numero)


    while len(self.i) < 5:
      numero = r.randint(16,30)

      if len(self.sorteado) > 1:
        if numero not in self.sorteado:
          self.sorteado.append(numero)
          self.i.append(numero)
        else:
          continue
      else:
        self.sorteado.append(numero)
        self.i.append(numero)


    while len(self.n) < 5:
      numero = r.randint(31,45)

      if len(self.sorteado) > 1:
        if numero not in self.sorteado:
          self.sorteado.append(numero)
          self.n.append(numero)
        else:
          continue
      else:
        self.sorteado.append(numero)
        self.n.append(numero)


    while len(self.g) < 5:
      numero = r.randint(46,60)

      if len(self.sorteado) > 1:
        if numero not in self.sorteado:
          self.sorteado.append(numero)
          self.g.append(numero)
        else:
          continue
      else:
        self.sorteado.append(numero)
        self.g.append(numero)


    while len(self.o) < 5:
      numero = r.randint(61,75)

      if len(self.sorteado) > 1:
        if numero not in self.sorteado:
          self.sorteado.append(numero)
          self.o.append(numero)
        else:
          continue
      else:
        self.sorteado.append(numero)
        self.o.append(numero)
  def printa(self):
    print("B   I   N   G   O")
    for linha in range(5):
        for coluna in range(5):
            if coluna == 0:
                print(f"{self.b[linha]:2}", end="  ")
            elif coluna == 1:
                print(f"{self.i[linha]:2}", end="  ")
            elif coluna == 2:
                if linha == 2:
                    print(" * ", end=" ")
                else:
                    print(f"{self.n[linha]:2}", end="  ")
            elif coluna == 3:
                print(f"{self.g[linha]:2}", end="  ")
            elif coluna == 4:
                print(f"{self.o[linha]:2}", end="  ")
        print()
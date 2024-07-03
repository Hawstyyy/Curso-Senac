import random as r

class Tabela:
    sorteado = []
    b = []
    i = []
    n = []
    g = []
    o = []

    def __init__(self):
        self.gerar_num()

    def gerar_num(self):
        while len(self.b) < 5:
            numero = r.randint(1,15)
            if numero not in self.sorteado:
                self.sorteado.append(numero)
                self.b.append(numero)

        while len(self.i) < 5:
            numero = r.randint(16,30)
            if numero not in self.sorteado:
                self.sorteado.append(numero)
                self.i.append(numero)

        while len(self.n) < 5:
            numero = r.randint(31,45)
            if numero not in self.sorteado:
                self.sorteado.append(numero)
                self.n.append(numero)

        while len(self.g) < 5:
            numero = r.randint(46,60)
            if numero not in self.sorteado:
                self.sorteado.append(numero)
                self.g.append(numero)

        while len(self.o) < 5:
            numero = r.randint(61,75)
            if numero not in self.sorteado:
                self.sorteado.append(numero)
                self.o.append(numero)

    def marcar_numero(self, numero):
        if numero in self.b:
            lugar = self.b.index(numero)
            self.b[lugar] = ' X '
        elif numero in self.i:
            lugar = self.i.index(numero)
            self.i[lugar] = ' X '
        elif numero in self.n:
            lugar = self.n.index(numero)
            self.n[lugar] = ' X '
        elif numero in self.g:
            lugar = self.g.index(numero)
            self.g[lugar] = ' X '
        elif numero in self.o:
            lugar = self.o.index(numero)
            self.o[lugar] = ' X '

    def verificar_bingo(self):
        for linha in [self.b, self.i, self.n, self.g, self.o]:
            if all(num == ' X ' for num in linha):
                return True
        
        for coluna in range(5):
            if self.b[coluna] == ' X ' and self.i[coluna] == ' X ' and self.n[coluna] == ' X ' and self.g[coluna] == ' X ' and self.o[coluna] == ' X ':
                return True
        
        if self.b[0] == ' X ' and self.i[1] == ' X ' and self.n[2] == ' X ' and self.g[3] == ' X ' and self.o[4] == ' X ':
            return True
        elif self.b[4] == ' X ' and self.i[3] == ' X ' and self.n[2] == ' X ' and self.g[1] == ' X ' and self.o[0] == ' X ':
            return True
        
        return False



    def printa(self):
        print()
        print("B   I   N   G   O")
        for linha in range(5):
            for coluna in range(5):
                if coluna == 0:
                    print(f"{self.b[linha]}", end="  ")
                elif coluna == 1:
                    print(f"{self.i[linha]}", end="  ")
                elif coluna == 2:
                    if linha == 2:
                        print("X", end="  ")
                    else:
                        print(f"{self.n[linha]}", end="  ")
                elif coluna == 3:
                    print(f"{self.g[linha]}", end="  ")
                elif coluna == 4:
                    print(f"{self.o[linha]}", end="  ")
            print()
import math
controle = "S"
porta = "N"

while porta != controle:
    n1 = input("Insira o primeiro número: ")

    n1 = float(n1)

    print("Selecione seu operando desejado:")
    print("                    1 - Adição - +")
    print("                    2 - Subtração - -")
    print("                    3 - Multiplicação - *")
    print("                    4 - Divisão - /")
    print("                    5 - Exponeciação - **")
    print("                    6 - Raiz Quadrada - 1/2")
    op = input("                        - ")

    if op == "6":
        resultado = math.sqrt(n1)
        print(f"O resultado da sua conta desejada é de: {resultado}")
    else:
        n2 = input("Insira o segundo número: ")

        n2 = float(n2)

        if op == "1":
            resultado = n1 + n2

        if op == "2":
            resultado = n1 - n2
            
        if op == "3":
            resultado = n1 * n2

        if op == "4":
            resultado = n1 / n2

        if op == "5":
            resultado = n1 ** n2
            
        print(f"O resultado da sua conta desejada é de: {resultado}")

        porta = input("Gostaria de sair?: S/N ")
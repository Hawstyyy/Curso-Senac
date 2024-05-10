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
    op = input("                        - ")
    n2 = input("Insira o segundo número: ")

    n2 = float(n2)

if op == "1":
    resultado = n1 + n2

elif op == "2":
    resultado = n1 - n2
            
elif op == "3":
   resultado = n1 * n2

elif op == "4":
  resultado = n1 / n2
            
print(f"O resultado da sua conta desejada é de: {resultado}")

porta = input("Gostaria de sair?: S/N ")
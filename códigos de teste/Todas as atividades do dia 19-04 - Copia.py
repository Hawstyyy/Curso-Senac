inicio = "\n\n#__________________Início da atividade__________________#\n\n"

fim = "\n\n#__________________Fim da atividade__________________#\n\n"

print("\n\n#----------------Senac Hub Academy----------------#\n\n")

atividaes = ['1','2','3','4','5','6','7','8']

print(f"""Atividades:
    - Atividade {[0]}
    - Atividade {[1]}
    - Atividade {[2]}
    - Atividade {[3]}
    - Atividade {[4]}
    - Atividade {[5]}
    - Atividade {[6]}
    - Atividade {[7]}""")

while True:
    atividade = input("Insira sua atividade desejada: ")

    if(atividade == "1"):
        print(inicio)

        nome, idade = input("Insira seu nome e idade: ").split(",")

        idade = int(idade)

        print(f"\n\nOlá! {nome}, sua idade é de {idade} certo?")
        print(fim)
        
    elif(atividade == "2"):
        print(inicio)

        numero = int(input("Insira seu numero desejado para descobrir seu antecessor e sucessor: "))

        numero_antecessor = numero - 1
        numero_sucessor = numero + 1

        print(f"\n\nSeu número desejado {numero} tem o antecessor {numero_antecessor} e tem o sucessor {numero_sucessor}")
        print(fim)

    elif(atividade == "3"):
        print(inicio)

        numeros = input("Insira suas notas separadas por um espaço: \n\n").split()
        x, y, z = float(numeros[0]), float(numeros[1]), float(numeros[2])

        media = (x + y + z) / 3

        print(f"\n\nSua média será de : {media}")
        print(fim)

    elif(atividade == "4"):
        print(inicio)

        dia = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        try:
            numero = int(input("- Insira um número para convertermos em um dia da semana: "))
            print(f"- Seu dia na semana é: {dia[numero]}")
        except:
            print("Não é um número, por favor insira um número")
            continue
        print(fim)

    elif(atividade == "5"):
        print(inicio)
        
        numero = int(input("Insira seu número que quer descobrir se é positivo ou não: "))

        if (numero < 0):
            print(f"\n\nSeu número {numero} é negativo")
        else:
            print(f"\n\nSeu número {numero} é positivo")

        print(fim)

    elif(atividade == "6"):
        print(inicio)

        numero1, op, numero2 = input("Insira sua conta desejada.(EX: 2 + 2): ").split()

        numero1 = int(numero1)
        numero2 = int(numero2)

        if(op == "+"):
            result = numero1 + numero2
        else:
            result = numero1 - numero2
        print(f"\n\nO resultado da sua subtração é: {result}")
        print(fim)

    elif(atividade == "7"):
        print(inicio)

        cor, quantia = input("Insira a cor do(s) disco(s) que você deseja e a quantidade separados por uma virgula \",\": ").split(",")
        quantia = int(quantia)

        if(cor == "azul" or cor == "Azul"):
                valor = float(20.00)
                break
        elif(cor == "laranja" or cor == "Laranja"):
                valor = float(30.00)
                break
        elif(cor == "roxo" or cor == "Roxo"):
                valor = float(40.00)
                break
        elif(cor == "marrom" or cor == "Marrom"):
                valor = float(50.00)
                break
        else:
                valor = 0
                print("Cor inválida")
        
        total = quantia * valor

        print(f"A quantia total a pagar será de R${total}, todos na cor {cor}")
        print(fim)

    elif(atividade == "8"):
        print(inicio)

        base = 1
        altura = 1
        while base == altura:
            numeros = input("Insira a base e a altura do terreno respectivamente, separados por uma vírgula: ").split(",")
            base, altura = float(numeros[0]), float(numeros[1])

            if(base == altura):
                print("\n!!!!!!!!!!!! Este terreno não é retangular !!!!!!!!!!!!\n")
            
        else:

            area = base * altura
        print(f"\n\nA área de seu terreno retangular é de {area}")
        print(fim)
variavel_de_controle = "sair"
atividade = "0"
inicio = "\n\n#_________________________________Início da atividade_________________________________#\n\n"
fim = "\n\n#_________________________________Fim da atividade_________________________________#\n\n"
print("\n\n#----------------Senac Hub Academy----------------#\n\n")

while atividade != variavel_de_controle:
    atividade = input("Insira sua atividade desejada de 1 - 15, escreva \"sair\" para sair: ")

    if(atividade == "1"):
        print(inicio)

        import time

        numero = int(0)

        while numero < 10:
            numero += 1
            time.sleep(1)
            print(numero)
        time.sleep(1)
        print("cabo")

        print(fim)
    
    elif(atividade == "2"):
        print(inicio)

        peso = int(input("Insira o peso do peixe: "))
        multa = 0

        while peso > 50:
            excesso = peso - 50
            multa = excesso * 4
            break
        print(f"A sua multa é de: R${multa}")

    elif(atividade == "3"):
        print(inicio)

        numero_escolhido = int(input("Insira seu número desejado: "))

        while numero_escolhido >= 1 and numero_escolhido <= 100:
            print("#-----------Está dentro do intervalo-----------#")
            numero_escolhido = int(input("Insira outro número: "))
        
        if numero_escolhido > 100 or numero_escolhido < 1:
            print("#-----------Está fora do intervalo-----------#")
            break
        
        print(fim)

    elif(atividade == "4"):
        print(inicio)

        m = 0
        f = 0
        alunos = 0
        altura_f = 0
        fisico = 0
        fisico_m = 0
        quantia = 0
        total = 50

        while alunos < 50:

            quantia = int (input ("Insira a quantidade de alunos do grupo que gostaria de cadastrar: ") )

            altura = float (input ("Insira a altura dos alunos do grupo: ") )
            
            fisico = int (input ("Insira os portes físicos dos alunos(as), 1 - Bom, 2 - Médio, 3 - Ruim: ") )

            sexo = int (input ("insira o sexo dos alunos(as), 1 - M ; 2 - F: ") )

            if sexo == 2 and altura >= 1.70:
                altura_f += quantia
            if fisico == 1 and sexo == 1:
                fisico_m += quantia
            
            restante = total - quantia
            total -= quantia
            alunos += quantia

            if alunos == 50:
                print("\n\n!!!!!!!!!!!!!!!!!!!!!! Todos os alunos cadastrados !!!!!!!!!!!!!!!!!!!!!!\n\n")
                break

            print(f"\n\n!!!!!!!!!!!!!!!!!!!!!! alunos restantes para cadastrar {restante} !!!!!!!!!!!!!!!!!!!!!!")

        porcentagem = (fisico_m/50) * 100

        print(f"\n\nA quantidade de alunas com mais de 1.70 é de {altura_f}")
        print(f"\n\nA porcentagem de alunos com o físico bom é de {porcentagem}%")
        print(fim)

    elif(atividade == "5"):
        print(inicio)

        print("!------------------Bem vindo a loja de CDs!------------------!\n\n")

        entrada = "S"
        soma = float(0)
        total = float(0)
        saida = "N"
        azul = 20.00
        laranja = 30.00
        roxo = 40.00
        marrom = 50.00

        while saida != entrada:

            print("""(-----------------)Menu(-----------------)
                  

                    1 - CD da cor azul - R$20.00
                    2 - CD da cor laranja - R$30.00
                    3 - CD da cor roxa - R$40.00
                    4 - CD da cor marrom - R$50.00
                  

            (----------------------------------------)\n\n""")

            escolha = input("Insira qual seu cd desejado de acordo com sua cor ou número: ")

            if escolha == "Azul" or escolha == "1":
                escolha = azul

            elif escolha == "Laranja" or escolha == "2":
                escolha = laranja
            
            elif escolha == "Roxo" or escolha == "3":
                escolha = roxo
            
            elif escolha == "Marrom" or escolha == "4":
                escolha = marrom

            quantia = int(input("\n\nInsira a quantia de cds da cor desejada: "))

            total = escolha * quantia
            soma += total

            saida = input("Deseja pagar? (S/N) ")


        print(f"#-------------------O total a pagar será de: R${soma}-------------------#")
        print(fim)

    elif (atividade == "6"):
        print(inicio)

        i = 0
        soma = 0

        while i < 10:
            valor = float(input("Insira seu número: \n\n"))
            soma += float(valor)
            i += 1
            
            faltante = 10 - i
            print(f"\n\n!!!!!!!!!!!!!!!!!!!! Quantia de números faltando para dar 10 números: {faltante} !!!!!!!!!!!!!!!!!!!!\n\n")
        
        print(f"\n\n#-------------------A soma dos 10 números inseridos foi de: {soma}-------------------#")
        print(fim)

    elif (atividade == "7"):
        print(inicio)

        soma = 0
        contagem = 0
        valor = 1

        while valor != 0:
            valor = float(input("Insira seu número: \n\n"))
            soma += float(valor)
            contagem += 1
        
        print(f"\n\n#-------------------A soma dos números inseridos até ser digitado 0 foi de: {soma}, em {contagem} tentativas-------------------#")
        print(fim)

    elif (atividade == "8"):
        print(inicio)

        print("""
              +-----------------------------------------------------------+
              |             Bem-vindo ao login do senac hub               |
              +-----------------------------------------------------------+""")
        nome = input("Insira seu nome para logar: ")
        senha = input("Insira sua senha: ")

        while senha == nome:
            print("\n\n!!!!!!!!!!!!!!!!!!!!!!! A senha não pode ser semelhante ao nome de usuário !!!!!!!!!!!!!!!!!!!!!!!\n\n")
            senha = input("Insira sua senha novamente: ")
        
        print(f"""
              +-----------------------------------------------------------+
              |                      Bem-vindo {nome}!                     |
              +-----------------------------------------------------------+""")

        print(fim)

    elif(atividade == "9"):
        print(inicio)

        contagem = 15
        contador = 0
        par = []
        impar = []

        while contador <= contagem:
            numero = int(input("Insira seu número inteiro: "))
            contador += 1

            if numero % 2 == 0:
                par.append(numero)
            elif numero % 2 == 1:
                impar.append(numero)
        
        print(f"\n\nDe todos os números inseridos os seguintes são pares: {par}\n")
        print(f"De todos os outros números os seguintes são ímpares: {impar}")

        print(fim)

    elif(atividade == "10"):
        print(inicio)

        nome = []
        nome = input("Insira seu nome: ")
        
        while len(nome) <= 3:
            print("\n\n!------------------insira um nome com mais de 3 letras------------------!\n\n")
            nome = input("Insira seu nome novamente: ")

        idade = int(input("Insira sua idade: "))

        while idade > 150:
            print("\n\n!------------------insira uma idade válida------------------!\n\n")
            idade = int(input("Insira sua idade novamente: "))
        
        salario = float(input("Insira seu salário: "))

        while salario <= 0:
            print("\n\n!------------------insira um salário válido------------------!\n\n")
            salario = float(input("Insira seu salário novamente: "))

        sexo = input("Insira seu sexo (M/F) ").capitalize()

        while sexo != "M" and sexo != "F":
            print("\n\n!------------------insira um sexo válido------------------!\n\n")
            sexo = input("Insira seu sexo novamente: ")
        
        print(f"""\n\n
              #------------------------------------#
              | Nome: {nome}
              | Idade: {idade}
              | Salário atual: {salario}
              | Sexo: {sexo}
              #------------------------------------#""")

        print(fim)
    
    elif(atividade == "11"):
        print(inicio)
        numeros = []

        numero = int(input("Insira um número: "))
        numeros.append(numero)

        while numero < 50 and numero > 0:
            numero = int(input("\nNúmero válido! continue digitando!: "))
            if numero >= 50:
                print("------------Número ultrapassou de 50!------------")
            else:
                numeros.append(numero)
    
        numeros_finais = str(numeros).replace("[", "").replace("]", "")
        quantia = len(numeros)
        print(f"todos os números digitados antes de se atingir 50 foram de: {numeros_finais}")
        print(f"A quantia de números digitados até antingir 50 foi de: {quantia}")

        print(fim)

    elif(atividade == "12"):
        print(inicio)

        contador = 0
        soma = 0
        negativos_quantia = 0
        i = 1

        while contador < 20:
            num = int(input(f"\nInsira o {i}° número desejado: "))
            i += 1

            if num < 0:
                negativos_quantia += 1
            elif num > 0:
                soma += num
            
            contador += 1
        
        print(f"\n\nA soma dos números positivios inseridos é de: {soma}")
        print(f"\nE a quantidade de números negativos digitados foi de: {negativos_quantia}")

        print(fim)

    elif (atividade == "13"):
        print(inicio)

        numero = int(input("Insira o número que deseja ver a tabuada: "))
        contador = int(input("\nInsira até que número você quer ver a tabuada escolhida acima: ", "\n\n"))
        i = 1

        while i <= contador:
            tabuada = numero * i

            print(f"{i}°: {tabuada}")
            i += 1
        
        print(fim)

    elif (atividade == "14"):
        print(inicio)

        minuto = 60
        valor = 9.00
        carro = input("O carro permaneceu mais que 15 minutos? (S/N)").capitalize()

        if carro == "S":
            tempo = int(input("Quanto tempo? "))

            if tempo <= 60:
                print(f"O carro permaneceu por {tempo} minutos e deve pagar R$9.00")
            elif tempo >= 120:
                while minuto <= tempo:
                    valor += 0.025
                    minuto += 1
        else:
            print("O tempo não precisa ser cobrado")
        
        print("O carro permaneceu por {0} minutos, devendo portanto pagar R${1:0.2f}".format(tempo,valor))

        print(fim)

    elif (atividade == "15"):
        print(inicio)


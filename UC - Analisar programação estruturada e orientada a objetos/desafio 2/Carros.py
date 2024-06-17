from Habilitação import Habilitacao

def print_master(veiculo):
    print(f"""
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
| Nome do veículo - {veiculo.nome}
| Quantia de pessoas suportada no veículo - {veiculo.quant_pessoa} pessoas
| Veículo de {veiculo.tracao} trações
| Habilitação necessária - {veiculo.tipo()}
| Tipo de motor - {veiculo.tipo_motor}
| Carroceria - {veiculo.carroceria}
| Preço do veículo - R${veiculo.preco}
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -""")

banco_de_dados = {

"Chevrolet Bolt EV": Habilitacao(
nome="Chevrolet Bolt EV",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Hatchback",
tipo_motor="Elétrico",
tipo_veiculo="Carro",
peso=1700,
preco=40000.00
),

"Ford Mustang Mach-E": Habilitacao(
nome="Ford Mustang Mach-E",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="SUV",
tipo_motor="Elétrico",
tipo_veiculo="Carro",
peso=2000,
preco=60000.00
),

"Audi e-tron": Habilitacao(
nome="Audi e-tron",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="SUV",
tipo_motor="Elétrico",
tipo_veiculo="Carro",
peso=2500,
preco=80000.00
),

"Tesla Model 3": Habilitacao(
nome="Tesla Model 3",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Elétrico",
tipo_veiculo="Carro",
peso=1800,
preco=55000.00
),

"BMW Serie 3": Habilitacao(
nome="BMW Serie 3",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1500,
preco=120000.00
),

"Mercedes-Benz Classe C": Habilitacao(
nome="Mercedes-Benz Classe C",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1550,
preco=125000.00
),

"Audi A4": Habilitacao(
nome="Audi A4",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1520,
preco=115000.00
),

"Chevrolet Onix": Habilitacao(
nome="Chevrolet Onix",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Hatchback",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1250,
preco=60000.00
),

"Hyundai HB20": Habilitacao(
nome="Hyundai HB20",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Hatchback",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1200,
preco=58000.00
),

"Kia Cerato": Habilitacao(
nome="Kia Cerato",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1380,
preco=90000.00
),

"Ford Ranger": Habilitacao(
nome="Ford Ranger",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Picape",
tipo_motor="Combustão",
tipo_veiculo="Caminhonete",
peso=1800,
preco=140000.00
),

"Nissan e-NV200": Habilitacao(
nome="Nissan e-NV200",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Van",
tipo_motor="Elétrico",
tipo_veiculo="Van",
peso=1565, 
preco=260000.00
),

"Tesla Cybertruck": Habilitacao(
nome="Tesla Cybertruck",
tracao=4,
quantidade_rodas=4,
quant_pessoa=6,
carroceria="Picape",
tipo_motor="Elétrico",
tipo_veiculo="Caminhonete",
peso=~2500,
preco=4000000.00
),

"Ford Transit": Habilitacao(
nome="Ford Transit",
tracao=2,
quantidade_rodas=4,
quant_pessoa=3,
carroceria="Van",
tipo_motor="Combustão",
tipo_veiculo="Van",
peso=2000,
preco=100000.00
),

"Energica Eva Ribelle": Habilitacao(
nome="Energica Eva Ribelle",
tracao=2,
quantidade_rodas=2,
quant_pessoa=1,
carroceria="Naked",
tipo_motor="Elétrico",
tipo_veiculo="Moto",
peso=260,
preco=23400.00
),

"Yamaha MT-07": Habilitacao(
nome="Yamaha MT-07",
tracao=1,
quantidade_rodas=2,
quant_pessoa=2,
carroceria="Naked",
tipo_motor="Combustão",
tipo_veiculo="Moto",
peso=182,
preco=28000.00
),

"Kawasaki Ninja 650": Habilitacao(
nome="Kawasaki Ninja 650",
tracao=1,
quantidade_rodas=2,
quant_pessoa=2,
carroceria="Sport",
tipo_motor="Combustão",
tipo_veiculo="Moto",
peso=196,
preco=32000.00
),

"Suzuki GSX-S750": Habilitacao(
nome="Suzuki GSX-S750",
tracao=1,
quantidade_rodas=2,
quant_pessoa=2,
carroceria="Naked",
tipo_motor="Combustão",
tipo_veiculo="Moto",
peso=213,
preco=35000.00
),

"BMW S 1000 RR": Habilitacao(
nome="BMW S 1000 RR",
tracao=1,
quantidade_rodas=2,
quant_pessoa=1,
carroceria="Sport",
tipo_motor="Combustão",
tipo_veiculo="Moto",
peso=197,
preco=50000.00
),
"Zero S": Habilitacao(
nome="Zero S",
tracao=2,
quantidade_rodas=2,
quant_pessoa=2,
carroceria="Naked",
tipo_motor="Elétrico",
tipo_veiculo="Moto",
peso=188,
preco=15995.00
),
"Audi e-tron GT": Habilitacao(
nome="Audi e-tron GT",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Elétrico",
tipo_veiculo="Sedan",
peso=2250,
preco=180000.00
),
"Nissan Leaf":Habilitacao(
nome="Nissan Leaf",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Hatchback",
tipo_motor="Elétrico",
tipo_veiculo="Hatchback",
peso=1491,
preco=200000.00
),
"Toyota SW4":Habilitacao(
nome="Toyota SW4",
tracao=4,
quantidade_rodas=4,
quant_pessoa=7,
carroceria="SUV",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=2200,
preco=250000.00
),
"Jeep Renegade":Habilitacao(
    nome="Jeep Renegade",
    tracao=2,
    quantidade_rodas=4,
    quant_pessoa=5,
    carroceria="SUV",
    tipo_motor="Combustão",
    tipo_veiculo="Carro",
    peso=1450,
    preco=120000.00
),
"Ford F-150":Habilitacao(
nome="Ford F-150",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Picape",
tipo_motor="Combustão",
tipo_veiculo="Caminhonete",
peso=2200,
preco=300000.00
),
"Ford F-150 Electric":Habilitacao(
nome="Ford F-150 Electric",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Picape",
tipo_motor="Elétrico",
tipo_veiculo="Caminhonete",
peso=2500,
preco=350000.00
),
"Zero SR/F":Habilitacao(
nome="Zero SR/F",
tracao=2,
quantidade_rodas=2,
quant_pessoa=1,
carroceria="Sport",
tipo_motor="Elétrico",
tipo_veiculo="Moto",
peso=220,
preco=22995.00
),
"Energica Ego":Habilitacao(
nome="Energica Ego",
tracao=2,
quantidade_rodas=2,
quant_pessoa=1,
carroceria="Sport",
tipo_motor="Elétrico",
tipo_veiculo="Moto",
peso=258,
preco=25900.00
),

    }

while True:
    escolha = int(input("""
+------------------- Bem-vindo ao banco de dados --------------------
| 1 - Questionário de escolha de carro
| 2 - Sair
+--------------------------------------------------------------------
    - """))
    
    if escolha == 1:
        hab_user = int(input("""
Qual veículo você busca (será suposto que você tem habilitação do mesmo)
    | 1 - Carro
    | 2 - Moto
        - """))
        if hab_user not in [1,2]:
            print("Número inválido, escolha novamente")
            continue
        elif hab_user == 1:
            hab_user = "Carro"
        else:
            hab_user = "Moto"
        
        filtro = []
        
        for veiculo, hab in banco_de_dados.items():
            if hab_user == "Carro" and (hab.tipo_veiculo == "Van" or hab.tipo_veiculo == "Caminhonete"):
                continue
            elif hab_user not in hab.tipo_veiculo:
                filtro.append(veiculo)
        
        for veiculo in filtro:
            del banco_de_dados[veiculo]
        break
    else:
        exit()

if hab_user == "Carro":
    while True:
        carroceria_user = int(input(f"""
Que tipo de carroceria você gostaria?
    | 1 - Sedan
    | 2 - Hatchback
    | 3 - SUV
    | 4 - Van
    | 5 - Picape
        - """))
        if carroceria_user not in [1,2,3,4,5]:
                print("Número inválido, escolha novamente")
                continue
        elif carroceria_user == 1:
            carroceria_user = "Sedan"
        elif carroceria_user == 2:
            carroceria_user = "Hatchback"
        elif carroceria_user == 3:
            carroceria_user = "SUV"
        elif carroceria_user == 4:
            carroceria_user = "Van"
        else:
            carroceria_user = "Picape"

        filtro = []
            
        for veiculo, carroc in banco_de_dados.items():

            if carroceria_user not in carroc.carroceria:
                filtro.append(veiculo)
            
        for veiculo in filtro:
            del banco_de_dados[veiculo]

        print("Veículos restantes de acordo com a sua resposta: \n")
        for key,value in banco_de_dados.items():
            print(f"| {key} - {value.carroceria}")
        break

else:
    while True:
        carroceria_user = int(input(f"""
Que tipo de carroceria você gostaria?
    | 1 - Sport
    | 2 - Naked
        - """))
        if carroceria_user not in [1,2]:
                print("Número inválido, escolha novamente")
                continue
        elif carroceria_user == 1:
            carroceria_user = "Sport"
        elif carroceria_user == 2:
            carroceria_user = "Naked"

        filtro = []
            
        for veiculo, carroc in banco_de_dados.items():

            if carroceria_user not in carroc.carroceria:
                filtro.append(veiculo)
            
        for veiculo in filtro:
            del banco_de_dados[veiculo]

        print("Veículos restantes de acordo com a sua resposta: \n")
        for key,value in banco_de_dados.items():
            print(f"| {key} - {value.carroceria}")
        break

while True:
    motor_user = int(input("""
Qual tipo de motor você gostaria:
    | 1 - Combustão
    | 2 - Elétrico
        - """))

    if motor_user not in [1,2]:
        print("Número inválido, por favor selecione novamente")
        continue
    elif motor_user == 1:
        motor_user = "Combustão"
    else:
        motor_user = "Elétrico"

    filtro = []

    for veiculo, motor in banco_de_dados.items():
        if motor_user not in motor.tipo_motor:
            filtro.append(veiculo)
        
    for veiculo in filtro:
        del banco_de_dados[veiculo]
    
    print("Esses foram os veículos de acordo com as suas respostas: \n")
    for veiculo,value in banco_de_dados.items():
        print_master(banco_de_dados[veiculo])
    break



# menor_valor = None
# for nome, veiculo in banco_de_dados.items():
#     if menor_valor == None:
#         menor_valor = veiculo
    
#     if veiculo.preco < menor_valor.preco:
#         menor_valor = veiculo

# print(menor_valor.nome, menor_valor.preco) guardando pra mais tarde pra filtrar e tal
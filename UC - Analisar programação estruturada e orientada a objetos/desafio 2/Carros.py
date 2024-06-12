from Habilitação import Habilitacao

def print_master(veiculo):
    print(f"""
- Nome do veículo: {veiculo.nome}
- Tração: {veiculo.tracao}
- Habilitação necessária: {veiculo.tipo()}
- Tipo de motor: {veiculo.tipo_motor}""")
    if veiculo.tipo_veiculo == "Carro" or veiculo.tipo_veiculo == "Caminhonete":
        print(f"- Carroceria: {veiculo.carroceria}")

banco_de_dados = {

"Ford Focus": Habilitacao(
nome="Ford Focus",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1400,
preco=75000.00
),

"Toyota Corolla": Habilitacao(
nome="Toyota Corolla",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1350,
preco=80000.00
),

"Honda Civic": Habilitacao(
nome="Honda Civic",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1370,
preco=78000.00
),

"Volkswagen Golf": Habilitacao(
nome="Volkswagen Golf",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Hatchback",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1300,
preco=70000.00
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

"Chevrolet S10": Habilitacao(
nome="Chevrolet S10",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Picape",
tipo_motor="Combustão",
tipo_veiculo="Caminhonete",
peso=1750,
preco=135000.00
),

"Toyota Hilux": Habilitacao(
nome="Toyota Hilux",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Picape",
tipo_motor="Combustão",
tipo_veiculo="Caminhonete",
peso=1850,
preco=150000.00
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

"Honda CB 500F": Habilitacao(
nome="Honda CB 500F",
tracao=1,
quantidade_rodas=2,
quant_pessoa=2,
carroceria="Naked",
tipo_motor="Combustão",
tipo_veiculo="Moto",
peso=190,
preco=30000.00
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
"Ducati Monster 821": Habilitacao(
nome="Ducati Monster 821",
tracao=1,
quantidade_rodas=2,
quant_pessoa=2,
carroceria="Naked",
tipo_motor="Combustão",
tipo_veiculo="Moto",
peso=206,
preco=45000.00
)
    }
print(len(banco_de_dados))
print_master(banco_de_dados["Ducati Monster 821"])
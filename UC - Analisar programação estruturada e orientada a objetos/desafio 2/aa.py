from Habilitação import Habilitacao

def print_master(veiculo):
    print(f"""
- Nome do veículo: {veiculo.nome}
- Tração: {veiculo.tracao}
- Habilitação necessária: {veiculo.tipo()}
- Tipo de motor: {veiculo.tipo_motor}""")
    if veiculo.tipo_veiculo == "Carro":
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
peso=1400
),

"Toyota Corolla": Habilitacao(
nome="Toyota Corolla",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1350
),

"Honda Civic": Habilitacao(
nome="Honda Civic",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1370
),

"Volkswagen Golf": Habilitacao(
nome="Volkswagen Golf",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Hatchback",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1300
),
"BMW Serie 3": Habilitacao(
nome="BMW Serie 3",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1500
),
"Mercedes-Benz Classe C": Habilitacao(
nome="Mercedes-Benz Classe C",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1550
),
"Audi A4": Habilitacao(
nome="Audi A4",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1520
),
"Chevrolet Onix": Habilitacao(
nome="Chevrolet Onix",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Hatchback",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1250
),
"Hyundai HB20": Habilitacao(
nome="Hyundai HB20",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Hatchback",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1200
),
"Kia Cerato": Habilitacao(
nome="Kia Cerato",
tracao=2,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Sedan",
tipo_motor="Combustão",
tipo_veiculo="Carro",
peso=1380
),
"Ford Ranger": Habilitacao(
nome="Ford Ranger",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Picape",
tipo_motor="Combustão",
tipo_veiculo="Caminhonete",
peso=1800
),
"Chevrolet S10": Habilitacao(
nome="Chevrolet S10",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Picape",
tipo_motor="Combustão",
tipo_veiculo="Caminhonete",
peso=1750
),
"Toyota Hilux": Habilitacao(
nome="Toyota Hilux",
tracao=4,
quantidade_rodas=4,
quant_pessoa=5,
carroceria="Picape",
tipo_motor="Combustão",
tipo_veiculo="Caminhonete",
peso=1850
),
"Ford Transit": Habilitacao(
nome="Ford Transit",
tracao=2,
quantidade_rodas=4,
quant_pessoa=3,
carroceria="Van",
tipo_motor="Combustão",
tipo_veiculo="Van",
peso=2000
),
"Honda CB 500F": Habilitacao(
    nome="Honda CB 500F",
    tracao=1,
    quantidade_rodas=2,
    quant_pessoa=2,
    carroceria="Naked",
    tipo_motor="Combustão",
    tipo_veiculo="Moto",
    peso=190
),
"Yamaha MT-07": Habilitacao(
    nome="Yamaha MT-07",
    tracao=1,
    quantidade_rodas=2,
    quant_pessoa=2,
    carroceria="Naked",
    tipo_motor="Combustão",
    tipo_veiculo="Moto",
    peso=182
),
"Kawasaki Ninja 650": Habilitacao(
    nome="Kawasaki Ninja 650",
    tracao=1,
    quantidade_rodas=2,
    quant_pessoa=2,
    carroceria="Sport",
    tipo_motor="Combustão",
    tipo_veiculo="Moto",
    peso=196
),
"Suzuki GSX-S750": Habilitacao(
    nome="Suzuki GSX-S750",
    tracao=1,
    quantidade_rodas=2,
    quant_pessoa=2,
    carroceria="Naked",
    tipo_motor="Combustão",
    tipo_veiculo="Moto",
    peso=213
),
"BMW S 1000 RR": Habilitacao(
    nome="BMW S 1000 RR",
    tracao=1,
    quantidade_rodas=2,
    quant_pessoa=1,
    carroceria="Sport",
    tipo_motor="Combustão",
    tipo_veiculo="Moto",
    peso=197
),
"Ducati Monster 821": Habilitacao(
    nome="Ducati Monster 821",
    tracao=1,
    quantidade_rodas=2,
    quant_pessoa=2,
    carroceria="Naked",
    tipo_motor="Combustão",
    tipo_veiculo="Moto",
    peso=206
)
}
print(len(banco_de_dados))
print_master(banco_de_dados["teste"])
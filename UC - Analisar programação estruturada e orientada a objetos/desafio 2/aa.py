from Habilitação import Habilitacao

def print_master(veiculo):
    print(f"""
- Nome do veículo: {veiculo.nome}
- Tração: {veiculo.tracao}
- Habilitação necessária: {veiculo.tipo()}""")
    if veiculo.tipo == "Carro":
        print(f"- Carroceria: {veiculo.carroceria}")
    else:
        print(f"- Tipo de motor: {veiculo.tipo_motor}")

banco_de_dados = {
    "teste":Habilitacao(
nome="MeuCarro",
tracao=2, 
quantidade_rodas=4,
quant_pessoa=6,
carroceria="Sedan",
tipo_motor="Combustão",
peso=1500)
}

print_master(banco_de_dados["teste"])
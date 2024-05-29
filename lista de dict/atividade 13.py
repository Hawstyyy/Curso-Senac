# Crie um dicionário com nomes de cidades e suas populações. Peça ao usuário
# para digitar o nome de uma cidade e exiba sua população.

cidades = {
    "Nova york": '8.398.748',
    "Los angeles": '3.990.456',
    "Chicago": '2.705.994',
    "Houston": '2.325.502',
    "Phoenix": '1.660.272',
    "Filadélfia": '1.584.138',
    "San antonio": '1.532.233',
    "San diego": '1.425.976',
    "Dallas": '1.345.047',
    "San jose": '1.030.119'
}
while True:
  escolha = input("\n- Insira o nome da cidade que gostaria de ver a população: ").capitalize()

  if escolha not in cidades:
    print("\n-! Essa cidade não está no nosso dicionário !-")
  
  else:
    for key,value in cidades.items():
      if escolha in key:
        print(f"\n- A cidade {key} tem a população de: {value}\n")
        break
  break
# Crie um dicionário com nomes de cores e seus códigos hexadecimais. Peça ao
# usuário para digitar o nome de uma cor e exiba seu código.

cores = {
    "Preto": "#000000",
    "Branco": "#FFFFFF",
    "Vermelho": "#FF0000",
    "Azul": "#0000FF",
    "Amarelo": "#FFFF00"
}

while True:
  select = input("\n- Fale a cor que você gostaria de descobrir o código hexadecimal: ").capitalize()

  if select not in cores:
    print(f"\n- A cor {select}, não existe no nosso dicionário. ")
  
  else:
    for key,value in cores.items():
      if select in key:
        print(f"\n- O código hexadecimal da cor {key} é: {value}")
        break
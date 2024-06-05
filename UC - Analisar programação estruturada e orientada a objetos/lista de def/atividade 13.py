# Faça um programa que verifica se uma palavra ou frase é um palíndromo. Um palíndromo é
# uma palavra ou frase que se lê da mesma forma de trás para frente. Por exemplo, “arara” é
# um palíndromo

def pali(palavra):
  pal_inv = ""
  for i in palavra[::-1]:
    pal_inv += i
  
  if pal_inv == palavra:
    print(f"- A palavra \"{palavra}\" é um palíndromo")
  else:
    print(f"- A palavra \"{palavra}\" não é um palíndromo")

pali(input("\n- Insira a sua palavra que deseja verificar se é um palíndromo: "))
# Crie um programa que pede ao usuário para digitar uma sequência de números e, em
# seguida, calcula a média aritmética desses números.

def media(n):

  quantia = len(n)
  soma = 0

  for i in n:
    soma += float(i)
  
  media = soma/quantia
  print(f"- A média das notas {", ".join(str(i) for i in n)} é: {round(media,2)}")

media(input("- Insira suas notas, cada um dividos por uma vírgula (EX: 10.0,10.0,10.0): ").split(","))
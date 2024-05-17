# Crie um fluxograma e o pseudocodigo que receba o nome da pessoa, receba o valor do ingresso e o tipo do ingresso (meia ou inteira), caso seja meia receba a carteirinha.
# Calcule no final o valor total da compra com todos os ingressos comprados e imprima quais os tipos de ingresso.
soma = 0
meias = 0
inteiras = 0

while True:
  nome = input("\n- Insira o nome do comprador: ")
  valor = float(input("\n- Insira o valor do ingresso: "))
  soma += valor

  tipo = input("\n- Insira o tipo do ingresso (Meia/Inteira): ")

  if tipo == "Meia" or tipo == "meia":
    meia = input("\n-! Insira as informações da carteirinha: ")
    meias += 1
  else:
    inteiras += 1
  
  sair = input("\n-! Deseja encerrar a compra? (s/n) ")
  if sair == "s":
    break

print(f"""
-! O valor total da compra com todos os ingressos foi de: R$ {soma}
-! Foram comprados: {meias} ingressos de meia entrada.
-! Foram comprados: {inteiras} ingressos de entrada inteira.
""")
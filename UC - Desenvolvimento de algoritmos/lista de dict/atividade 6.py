# Crie um jogo onde o usuário digita uma palavra e o programa verifica se ela está
# no dicionário. Se estiver, exiba seu significado.

lista_de_palavras = {'vocal','bolsas', 'literatura','desatar', 'partida', 'pavio', 'cordão','catalunha','faces','queijo'}

while True:
  palavra = input("\n- Acerte a palavra secreta! ")
  
  if palavra not in lista_de_palavras:
    print("- Palvra errada :), tente de novo\n")
  
  else:
    print(f"- Você acertou a palavra secreta! a palvra era {palavra}\n")
    break
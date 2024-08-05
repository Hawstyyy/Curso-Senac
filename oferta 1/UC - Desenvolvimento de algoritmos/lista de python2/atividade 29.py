cd = {1: {},
      2: {}}
soma = 0

while True:
  preco = float(input("\n- Insira o preço de um grupo de cds: "))
  cds = int(input(f"\n- Agora insira a quantidade de cds com o preço de R${preco}: "))

  grupo = preco * cds

  cd[1][f'cds de R${preco}'] = cds
  cd[2][f'preço total do grupo R${preco}'] = grupo

  saida = input("deseja sair? (S/N) ").capitalize()
  if saida == "S":
    break

for x in cd[2].values():
  soma += x

print(f"""
- O valor total da coleção é de: R${soma}.
- A coleção foi divida em {len(cd[1])} grupos de diferentes valores.
""")
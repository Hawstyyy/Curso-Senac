# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e 
# pretende implantar a metodologia da tabelinha, que já é um sucesso na sua 
# loja de 1,99. Você foi contratado para desenvolver o programa que monta a 
# tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão 
# informado pelo usuário

quantia = int(input("\n- Insira a quantidade de pães do cliente: "))
preco = float(input("\n- Insira o preço base do pão: "))
PRECO = preco

print("\n+ - - - - - - - - - - - - - - - -")
for x in range(1,quantia+1):
  print(f"| {x}° Produto - {preco}")
  preco += PRECO
  preco = round(preco, 2)
print("+ - - - - - - - - - - - - - - - -\n")
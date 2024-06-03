# O Sr. Manoel Joaquim expandiu seus negócios para além dos 
# negócios de 1,99 e agora possui uma loja de conveniências. Faça um 
# programa que implemente uma caixa registradora rudimentar. O programa 
# deverá receber um número desconhecido de valores referentes aos preços 
# das mercadorias. Um valor zero deve ser informado pelo operador para 
# indicar o final da compra. O programa deve então mostrar o total da compra 
# e perguntar o valor em dinheiro que o cliente forneceu, para então calcular 
# e mostrar o valor do troco. Após esta operação, o programa deverá voltar 
# ao ponto inicial, para registrar a próxima compra.

print("\n- Lojas Tabajara -")
i = 0
total = 0

while True:
  i += 1
  produto = float(input(f"\n- Insira o valor do {i}° Produto: "))
  total += produto

  saida = input("\n- Deseja finalizar? (S/N) ").capitalize()
  if saida == "S":
    break

dinheiro = float(input(f"\n- O total da compra foi de: R$ {total}, qual foi a nota fornecida? "))

print("\n- O troco será de: R$",  dinheiro - total)
print()
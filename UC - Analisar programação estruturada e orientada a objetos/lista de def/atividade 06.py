# Crie um software que recebe um número do usuário, passa esse valor para uma função e ela
# retorna o número escrito ao inverso. Por exemplo, se o usuário der o valor 1234, a função
# deve retornar 4321.

def inverse(n):
  num_inv = ' '
  tamanho = len(n)
  for i in range(tamanho, 0, -1):
    num_inv += str(n[i-1])
  print(f"\n- O seu número invertido é: {num_inv}")

inverse(input("\n- Insira o seu número para invertermos! "))
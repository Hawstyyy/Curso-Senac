# Um número primo é aquele que 
# é divisível apenas por um e por ele mesmo. Faça um programa que peça 
# um número inteiro e determine se ele é ou não um número primo. 

num = int(input("\n- Insira o número que quer verificar se é primo ou não: "))
div = []

for x in range(1,num+1):
  if num % x == 0:
    div.append(str(x))

if len(div) > 2:
  print(f"""
- O número {num} não é primo.
- Ele é divisivel por: {", ".join(div)}
""")

else:
    print(f"""
- O número {num} é primo.
- Ele é divisivel apenas por: 1 e ele mesmo.
""")

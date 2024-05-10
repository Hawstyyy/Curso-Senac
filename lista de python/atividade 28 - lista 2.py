print("""
Escolha uma opção:
1 -	Soma de 2 números.
2 -	Diferença entre 2 números (maior pelo menor).
3 -	Produto entre 2 números.
4 -	Divisão entre 2 números (o denominador não pode ser zero).
""")
op = int(input("- "))

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))


if op == 1:
  r = num1 + num2
elif op == 2:
  r = num1 - num2
elif op == 3:
  r = num1 * num2
elif op == 4:
  r = num1 / num2
elif op > 4:
  print("Operação inválida")
  exit()

print(f"O resultado é: {r}")
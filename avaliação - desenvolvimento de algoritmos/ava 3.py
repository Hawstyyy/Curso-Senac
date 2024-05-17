# onde N é o número de notas a serem usadas na média, ni é a i-ésima nota, e X é o fator de
# amortização. Implemente um algoritmo em Python que calcule a média de 3 notas de um aluno
# digitadas no teclado, com fator de amortização igual a 4. Em seguida, informe se o aluno passou
# (média >= 5) ou não (média < 5).

notas = []

n1 = float(input("\n- Insira a primeira nota do aluno: "))
n2 = float(input("- Insira a segunda nota do aluno: "))
n3 = float(input("- Insira a terceira nota do aluno: "))
x = 4

h = 3 / ((1 / (n1 + x)) + (1 / (n2 + x)) + (1 / (n3 + x))) - x

if h < 5:
  print(f"\n-! Você não passou, sua média é de: {h:.2f}")

else:
  print(f"\n-! Você passou, sua média é {h:.2f}")
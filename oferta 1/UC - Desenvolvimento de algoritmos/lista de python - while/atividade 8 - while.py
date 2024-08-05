salario = float(input("Qual o salário do funcionário: "))
salarioinicial = salario
aumento = 1.5
ano = 1

while True:
    aumentosalarial = (salario * aumento) / 100
    salario += aumentosalarial
    salario = round(salario, 2)

    print(f"""\n
      + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      | Salário inicial do funcionário era de: R$ {salarioinicial}
      | Salário atual do funcionário é de: R${salario}
      | Taxa de aumento atual: {aumento}%
      | Anos de trabalho: {ano} anos
      + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
\n""")
    aumento *= 2
    ano += 1

    funcionario = input("O funcionário ainda trabalha na empresa? ").capitalize()
    if funcionario == "N":
      print("\n\n- - - - - - - - Programa encerrado - - - - - - - -\n\n")
      break
# Um funcionário de uma empresa recebe aumento salarial
# anualmente: Sabe-se que:
# a. Esse funcionário foi contratado em 1995, com salário inicial de
# R$ 1.000,00;
# b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# c. A partir de 1997 (inclusive), os aumentos salariais sempre
# correspondem ao dobro do percentual do ano anterior. Faça um
# programa que determine o salário atual desse funcionário. Após
# concluir isto, altere o programa permitindo que o usuário digite o
# salário inicial do funcionário. 

salario = float(input("Qual o salário do funcionário: "))
salario_inicial = salario
aumento = 1.5
ano = 1

while True:
    aumento_salarial = salario * 0.015
    salario += aumento_salarial
    salario = round(salario, 2)

    print(f"""\n
      + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
      | Salário inicial do funcionário era de: R$ {salario_inicial}
      | Salário atual do funcionário é de: R${salario}
      | Taxa de aumento atual: {aumento}%
      | Anos de trabalho: {ano} anos
      + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
\n""")
    aumento *= 2
    ano += 1

    funcionario = input("O funcionário continua trabalhando na empresa? ").capitalize()
    if funcionario == "N":
      print("\n\n- - - - - - - - Programa encerrado - - - - - - - -\n\n")
      break
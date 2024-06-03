salario = float(input("Insira a quantidade que você recebe por hora: "))
tempo = float(input("Insira a quantia de horas que você trabalha por mês: "))

bruto = salario * tempo

inss = (bruto * 8) / 100
sindicato = (bruto * 5) / 100
ir = (bruto * 11) / 100

desconto = inss + sindicato + ir
liquido = bruto - desconto

print(f"""O resultado será o seguinte:
      Você tem o salário bruto de R${bruto}
      Você pagou R${inss} ao INSS
      Você pagou R${sindicato} ao Sindicato
      e o seu salário final com os descontos é de R${liquido}""")
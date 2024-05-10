horas = int(input("Insira a quantia de horas que o funcionário trabalhou: "))

hora_extra = 40.50
salario_base = 2500 - ((2500 * 11) / 100)

if horas > 1:
  salario_base += (hora_extra * horas)
  print(f"O salário do funcionário será de: R${salario_base}")
else:
  salario_base += 40.50
  print(f"O salário do funcionário será de: R$ {salario_base}")
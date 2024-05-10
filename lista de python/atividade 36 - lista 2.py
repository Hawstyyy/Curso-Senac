salario_atual = float(input("Insira o salário atual do funcionário: "))
tempo = int(input("Insira o tempo de serviço do funcionário em anos: "))

if salario_atual <= 500 and tempo < 1:
  porcentagem = ( salario_atual * 25) / 100
  salario_novo = salario_atual + porcentagem
  print(f"O novo salário do funcionário será de: R${salario_novo} e sem acréscimo de bônus")

elif salario_atual <= 1000 and tempo >= 1 and tempo <= 3:
  porcentagem = ( salario_atual * 20) / 100
  salario_novo = salario_atual + porcentagem + 100
  print(f"O novo salário do funcionário será de: R${salario_novo} e com acréscimo de R$100,00 de bônus")

elif salario_atual <= 1500 and tempo >= 4 and tempo <= 6:
  porcentagem = ( salario_atual * 15) / 100
  salario_novo = salario_atual + porcentagem + 200
  print(f"O novo salário do funcionário será de: R${salario_novo} e com acréscimo de R$200,00 de bônus")

elif salario_atual <= 2000 and tempo >= 7 and tempo <= 10:
  porcentagem = ( salario_atual * 10) / 100
  salario_novo = salario_atual + porcentagem + 300
  print(f"O novo salário do funcionário será de: R${salario_novo} e com acréscimo de R$300,00 de bônus")

else:
  salario_novo = salario_atual + 500
  print(f"O novo salário do funcionário será de: R${salario_novo}, sem reajuste de percentual e com acréscimo de R$500,00 de bônus")
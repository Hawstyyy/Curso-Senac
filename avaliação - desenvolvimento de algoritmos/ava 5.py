# 5 - Num país imaginário chamado Lisarb, todas as pessoas ficam muito felizes em pagar os seus
# impostos porque sabem que não existem políticos corruptos e que os impostos são usados para
# beneficiar a população, sem qualquer apropriação indevida. A moeda deste país é o Rombus (R$).
# Leia um valor com 2 dígitos após a vírgula, equivalente ao salário de um habitante do Lisarb. 

salario = float(input("- Insira o salário do habitante: "))
taxa = 0

if salario <= 2000.00:
  print("Isento")

elif salario > 2000.00 and salario < 3000.00:
  taxa = 0.08

elif salario > 3000.00 and salario < 4500.00:
  taxa = 0.18

else:
  taxa = 0.28

if taxa > 0 and salario > 3000:
  imposto = (salario * taxa)
  print(f"R$ {imposto}")
else:
  imposto = (1000 * 0.08)
  resto = salario // 1000
  imposto2 = resto * 0.18

  imposto_final = imposto + imposto2
  print(f"R$ {imposto_final}")
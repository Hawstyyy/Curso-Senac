venda_valor = float(input("Insira o valor da venda realizada: "))

if ( venda_valor >= 100000.00 ):
  porcentagem = (venda_valor * 16) / 100
  venda_final = venda_valor + 700.00 + porcentagem

elif ( venda_valor < 100000.00  and  venda_valor >= 80000.00 ):
  porcentagem = (venda_valor * 14) / 100
  venda_final = venda_valor + 650.00 + porcentagem

elif ( venda_valor < 80000.00  and  venda_valor >= 60000.00 ):
  porcentagem = (venda_valor * 14) / 100
  venda_final = venda_valor + 600.00 + porcentagem

elif ( venda_valor < 60000.00  and  venda_valor >= 40000.00 ):
  porcentagem = (venda_valor * 14) / 100
  venda_final = venda_valor + 550.00 + porcentagem

elif ( venda_valor < 40000.00  and  venda_valor >= 20000.00):
  porcentagem = (venda_valor * 14) / 100
  venda_final = venda_valor + 500.00 + porcentagem

else:
  porcentagem = (venda_valor * 14) / 100
  venda_final = venda_valor + 400.00 + porcentagem

print(f"A comissão do vendedor será de: {venda_final}")
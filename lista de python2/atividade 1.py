# Faça um programa que peça uma nota, entre zero e dez. Mostre
# uma mensagem caso o valor seja inválido e continue pedindo até que o
# usuário informe um valor válido. 

while True:
  nota = float(input("\n- Insira uma nota entre 0 e 10: "))
  
  if nota > 10.0 or nota < 0:
    print("\n- A nota inserida é incorreta")
  else:
    print("\n- Nota válida!")
    break
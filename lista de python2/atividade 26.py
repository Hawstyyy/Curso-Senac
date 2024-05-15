# Faça um programa que peça para n pessoas a sua idade, ao final o 
# programa devera verificar se a média de idade da turma varia entre 0 e 
# 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou 
# idosa, conforme a média calculada.

notas = []
nota = 0 

while True:
  try:
    idade = int(input("\nInsira sua idade, digite 1234 para sair: "))
  except:
    print("\n!!!!!!!! Número inválido !!!!!!!!")
  
  if idade == 1234:
    break
  
  print("\n- Idade cadastrada com sucesso!")
  notas.append(nota)

media = sum(notas) / len(notas)

if idade > 0 and idade < 25:
  print("\n- A idade média da turma é considerada juvenil!")

elif idade > 26 and idade < 60:
  print("\n- A idade média da turma é considerada adulta")

else:
  print("\n- A idade média da turma é considerada idosa!")
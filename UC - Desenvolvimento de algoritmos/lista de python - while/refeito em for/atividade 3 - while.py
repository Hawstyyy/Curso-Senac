nome = []
nome = input("Insira o seu nome: ")

while len(nome) <= 3:
  nome = input("Nome muito curto, tente novamente: ")

idade = int(input("Insira a sua idade: "))

while idade > 150 or idade < 0:
  idade = int(input("Idade inválida, tente de novo: "))

salario = float(input("Insira o seu salário: "))

while salario < 0:
  salario = float(input("Salário inválido, tente de novo: "))

sexo = input("Insira seu sexo, F - Feminino, M - Masculino ou O - Outro: ").capitalize()

while sexo != "F" and sexo != "M" and sexo != "O":
  sexo = input("Sexo inválido, tente novamente: ").capitalize()

estado = input("Insira seu estado civil, S - solteiro, C - Casado, V - Viuvo, D - Divorciado: ").capitalize()

while estado != "S" and estado != "C" and estado != "V" and estado != "D":
  estado = input("Estado civil inválido, tente novamente: ").capitalize()

print("Registro encerrado")
# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c. Salário: maior que zero;
# d. Sexo: 'f' ou 'm';
# e. Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de
# caracteres). 

nome = input("Insira seu nome: ")

if len(nome) < 3:
  print("Nome muito curto")
  nome = input("Insira seu nome: ")

idade = int(input("Insira sua idade: "))

if idade > 150 or idade < 0:
  print("Idade inválida")
  idade = int(input("Insira sua idade: "))

salario = float(input("Insira seu salario acima de 0: "))

if salario < 0:
  print("Salário inválido")
  salario = float(input("Insira seu salario acima de 0: "))

sexo = input("Insira seu sexo (M/F/O(outro)): ").capitalize()

if sexo != "M" and sexo != "F" and sexo != "O":
  print("Sexo inválido")
  sexo = input("Insira seu sexo (M/F/O(outro)): ").capitalize()

tasolteiro = input("Insira seu Estado Cívil (Solteiro/Casado/Viuvo/Divorciado): ").capitalize()

if tasolteiro != "S" and tasolteiro != "C" and tasolteiro != "V" and tasolteiro != "D":
  print("Estado civil inválido")
  tasolteiro = input("Insira seu Estado Cívil (Solteiro/Casado/Viuvo/Divorciado): ").capitalize()










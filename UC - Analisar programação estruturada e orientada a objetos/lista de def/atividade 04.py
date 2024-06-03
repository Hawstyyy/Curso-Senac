# Programe um software que recebe três números e cria duas funções: uma que retorna o
# maior número e outra que retorna o menor número.

numero_lista = []

def maior(numero_lista):
  num_maior = 0
  for i in numero_lista:
    if num_maior == 0 or num_maior < i:
      num_maior = i
  print(f"- O número maior é: {num_maior}")

def menor(numero_lista):
  num_menor = 0
  for i in numero_lista:
    if num_menor == 0 or num_menor > i:
      num_menor = i
  print(f"- O número menor é: {num_menor}")

print("\n#--------------- Bem vindo ao verificador de número ---------------#")

while True:
  numero_lista.append(int(input("- Insira a lista de números que deseja verificar: ")))
  end = input("- Encerra? ").capitalize()
  if end == "S":
    break

select = input("- Deseja verificar o maior, o menor ou ambos? ").capitalize()
if select == "Maior":
  maior(numero_lista)
elif select == "Menor":
  menor(numero_lista)
else:
  maior(numero_lista)
  menor(numero_lista)
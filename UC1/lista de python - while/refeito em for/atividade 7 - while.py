maior = 0
menor = 0
maisgordo = 0
menosgordo = 0

while True:

  codigo = input("Insira o código do cliente, digite 0 para sair: ")

  if codigo == "0":
    break

  altura = int(input("Insira a altura do cliente, em cm: "))

  if altura > maior:
    codigomaior = codigo
    maior = altura

  if altura < menor or menor == 0:
    codigomenor = codigo
    menor = altura

  peso = float(input("Insira o peso do cliente: "))
  
  if peso > maisgordo:
    codigogordo = codigo
    maisgordo = peso

  if peso < menosgordo or menosgordo == 0:
    codigomagro = codigo
    menosgordo = peso

print(f"O cliente mais alto é {codigomaior}, tendo {maior} cm de altura")
print(f"O cliente mais baixo é {codigomenor}, tendo {menor} cm de altura")
print(f"O cliente mais gordo é {codigogordo}, tendo {maisgordo} kg")
print(f"O cliente mais magro é {codigomagro}, tendo {menosgordo} kg")
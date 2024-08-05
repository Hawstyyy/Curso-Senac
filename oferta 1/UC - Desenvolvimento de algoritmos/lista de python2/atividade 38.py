# Uma academia deseja fazer um senso entre seus clientes para
# descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto
# você deve fazer um programa que pergunte a cada um dos clientes da
# academia seu código, sua altura_min e seu peso. O final da digitação de dados
# deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao
# encerrar o programa também deve ser informados os códigos e valores do
# clente mais alto, do mais baixo, do mais gordo e do mais magro, além da
# média das alturas e dos pesos dos clientes
altura_min = 0
cod_baixo = 0

gordo = 0
cod_gordo = 0

magro = 0
cod_magro = 0

altura_max = 0
cod_alto = 0

lista = []

print("""
+ - - - - - - - - - - - - - - - - - - - - +
|      Bem vindo a academia Senac!        |
+ - - - - - - - - - - - - - - - - - - - - +""")

while True:
  codigo = int(input("- Insira o código do cliente, digite 0 para sair: "))
  if codigo == 0:
    break
  else:
    altura = int(input("- Insira a altura do cliente em cm: "))
    peso = float(input("- Insira o peso do cliente: "))
    lista.append([codigo,altura,peso])

for x in lista:
  if altura_min == 0 or altura_min > x[1]:
    altura_min = x[1]
    cod_baixo = x[0]
  else:
    continue

for x in lista:
  if altura_max == 0 or altura_max < x[1]:
    altura_max = x[1]
    cod_alto = x[0]
  else:
    continue

for x in lista:
  if gordo == 0 or gordo < x[2]:
    gordo = x[2]
    cod_gordo = x[0]
  else:
    continue

for x in lista:
  if magro == 0 or magro > x[2]:
    magro = x[2]
    cod_magro = x[0]
  else:
    continue

print(f"""
- O cliente mais magro tem: {magro} kg, e seu código é: {cod_magro}
- O cliente mais gordo tem: {gordo} kg, e seu código é: {cod_gordo}
- O cliente mais alto tem: {altura_max} cm, e seu código é: {cod_alto}
- O cliente mais alto tem: {altura_min} cm, e seu código é: {cod_baixo}""")
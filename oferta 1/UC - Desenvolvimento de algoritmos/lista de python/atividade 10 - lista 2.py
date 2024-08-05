while True: 
  numero = int(input("Insira o número que deseja ver a raiz quadrada e elevado ao quadrado: "))

  if numero > 0:
    raiz = numero ** (1/2)
    elev = numero ** 2
    print(f"""O número {numero} tem de resultados o seguinte:
          raiz quadrada = {raiz}
          elevado ao quadrado = {elev}""")
    break
  else:
    print("Número inválido")
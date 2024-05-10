while True:
  try:
    inteiro = int(input("Insira um numero inteiro: "))
    inteiro2 = int(input("Insira um numero inteiro: "))
    real = float(input("Insira um real: "))
    break
  except:
    print("Poucos valores ou valor inválido")

conta = inteiro * (inteiro2/2)
conta1 = (inteiro * 3) + real
cubo = real ** 3

print(f"""- O produto do primeiro com a metade do segundo: {conta}
    
- A soma do triplo do primeiro com o terceiro: {conta1}

- O terceiro número digitado ao cubo: {cubo}""")
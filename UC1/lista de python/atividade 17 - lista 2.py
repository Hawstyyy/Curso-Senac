while True:
  salario = float(input("Insira seu salário para validarmos o seu empréstimo: "))
  prestacao = float(input("Insira o valor do empréstimo: "))

  porcetagem = (prestacao / salario) * 100

  if porcetagem >= 20:
    print("Empréstimo não concedido")

  else:
    print("Empréstimo concedido")
    break
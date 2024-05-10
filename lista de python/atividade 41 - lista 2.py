raiz = input("Insira o \"a\", o \"b\" e o \"c\" da sua raiz quadrada: ").split(",")

a,b,c = [int(raiz[0]), int(raiz[1]), int(raiz[2])]

if a == "0":
  print("Não é uma equação de segundo grau")

else:
  delta = (b**2) - (4 * a * c)

  if delta < 0:
    print("Não existe raiz para essa equação")
  
  elif delta > 0:
    x1 = ( -(b) + ( delta ** 0.5 ) ) / (2 * a)
    x2 = ( -(b) - ( delta ** 0.5) ) / ( 2 * a)

    print(f"As raízes da sua equação será: {x1} e {x2}")

  else:
    x1 = ( -(b) + ( delta ** 0.5 ) ) / (2 * a)
    x2 = ( -(b) - ( delta ** 0.5) ) / ( 2 * a)

    if x1 == 0:
      print(f"{x2}, raiz única")
  
    else:
      print(f"{x1}, raiz única")
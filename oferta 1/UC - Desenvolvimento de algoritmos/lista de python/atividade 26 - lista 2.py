ano = int(input("Inisira o ano desejado para verificar se é bissexto: "))

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
  print(f"O ano {ano} é bissexto")
else:
  print(f"O ano {ano} não é bissexto")
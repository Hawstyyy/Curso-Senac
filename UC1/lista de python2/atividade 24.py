
primo = []
div_ = 0

while True:
  try:
    n = int(input("\nInsira um número onde deseja ver até onde vai a divisão de primos: "))
    break
  except:
    print("\n!!!!!!!!!!!!!!!!!!!! Número Inválido !!!!!!!!!!!!!!!!!!!!")

for i in range(1,n+1):
  if n % i == 0:
    primo.append(str(i))
    div_ += 1
  
  else:
    div_ += 1

print(f"""
- Entre 1 e o número inserido {n} os seguintes são primos:
- {", ".join(primo)}
- E a quantidade de divisões feitas foram: {div_}
""")
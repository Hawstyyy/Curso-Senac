num1 = 50
num2 = 100
pares = []
impares = []

for i in range(num1,num2):
  if i % 2 == 0:
    pares.append(i)
  else:
    impares.append(i)

parestr = []
for i in pares:
  parestr.append(str(i))

imparstr = []
for i in impares:
  imparstr.append(str(i))

print(f"""Os números pares foram pares: 
      {', '.join(parestr)}""")
print(f"""Os números ímpares foram: 
      {', '.join(imparstr)}""")
while True:
  try:
    num1 = int(input('Insire um numero ai: '))
    num2 = int(input('Insire outro numero ai: '))
    break
  except:
    print("Número inválido")
if num2 < num1:
  num2,num1 = num1,num2
soma = 0

num2 += 1

for i in range(num1,num2):
  i = int(i)
  print(i, end=" ")
  soma += i
print(soma)


def div(a: int,b: int):
  return a / b

try:
  a = 14
  b = '134'

  res = div(a,b)
  print(res)

except TypeError:
  print("- Tipo incorreto de dados")
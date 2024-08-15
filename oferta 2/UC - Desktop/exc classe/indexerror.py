lista = [0,1,2]

for i in range(4):
  print(f"posição atual {[i]}")
  try:
    lista[i]
  except IndexError:
    print(f"- A posição {[i]} está fora da lista atuals")
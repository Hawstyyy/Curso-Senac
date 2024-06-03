posi = []

for i in range(100, 49, -2):
  posi.append(str(i))

print(f"""
Os números pares de 100 a 50 foram:
{", ".join(posi)}""")
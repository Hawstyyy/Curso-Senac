numeros = []

for i in range(10):
  numeros.append(input(f"- Insira seu {i+1}° número: "))

maior = max(numeros)

print(f"""
- O maior número na lista:
{", ".join(numeros)}
\nFoi o número: {maior}""")
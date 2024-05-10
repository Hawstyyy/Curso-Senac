num = []
multi = []
multi_str = []
num_str = []

for i in range(1,6):
  num.append(int(input(f"Insira seu {i}° número: ")))

for i in num:
  multi.append(int(i * 5))

# multi_str = ''.join(multi)
# num_str = ''.join(num)

print(f"""
Os números inseridos foram: {', '.join(str(i) for i in num)}
Agora esses multiplicados por 5 terão o resultado de: {', '.join(str(i) for i in multi)}""")
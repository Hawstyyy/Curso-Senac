tamanho = float(input("Insira os metros quadrados a ser pintada: "))

quantia = tamanho / 108
quantia2 = tamanho / 21.6
metade = tamanho / 2
quantia3 = metade / 108
quantia31 = metade / 21.6

preco = quantia * 80.00
preco2 = quantia2 * 25.00
preco3 = quantia3 * 80.00
preco4 = quantia31 * 3.6
precofinal = preco3 + preco4

print(f"Comprando apenas latas de 18 litros será: {quantia} e custará R$ {preco}")
print(f"Comprando apenas galões de 3.6 litros será: {quantia2} e custará R$ {preco2}")
print(f"Comprando metade latas e metade galões será: {quantia3} latas e {quantia31} galões e custará R$ {precofinal}")
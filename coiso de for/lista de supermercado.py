lista = []
print("""
+- - - - - - - - - - - - - PRODUTOS - - - - - - - - - - - - - +
| - Macarrão
| - Refrigerante
| - Frutas
| - Verduras
| - Arroz
| - Feijão
+- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
""")
for i in range(1,11):
  lista.append(input(f"Insira sua {i}° mercadoria desejada: "))

print("Você escolheu os seguintes produtos: ")
print(", ".join(lista))
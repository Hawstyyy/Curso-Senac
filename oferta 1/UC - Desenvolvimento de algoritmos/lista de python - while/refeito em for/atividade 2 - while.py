nome = input("Insira o nome desejado: ")
senha = input("Inira a senha desejada: ")

while senha == nome:
  print("A senha não pode ser a mesma que o nome")
  senha = input("Inira a senha desejada: ")

print("Registrado com sucesso")
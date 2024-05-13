# Faça um programa que leia um nome de usuário e a sua senha e
# não aceite a senha igual ao nome do usuário, mostrando uma mensagem
# de erro e voltando a pedir as informações. 


while True:
  nome = input("\nInsira o seu nome de usuário: ").split()
  senha = input("\nInsira sua senha: ").split()



  for x in nome:

    for y in senha:

      if x == y:
        print("mema senha doido")
      else:
        print("Cadastrado com sucesso")
        quit()


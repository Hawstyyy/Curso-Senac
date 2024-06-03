# Faça um programa que imprima na tela apenas os números ímpares
# entre 1 e 50. 


impar = []
for x in range(1,51,2):
  impar.append(str(x))

print("Os números ímpares de 0 a 50 são de:",", ".join(impar))
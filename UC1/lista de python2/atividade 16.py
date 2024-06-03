# A série de Fibonacci é formada pela sequência
# 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
# valor seja maior que 500. 

n = int(input("Insira até que termo gostaria de ver: "))
fibonacci1 = 0
fibonacci2 = 1
fibonacci3 = 1

while fibonacci3 <= n:
    print(f"{fibonacci3}", end=", ")

    fibonacci3 = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci3

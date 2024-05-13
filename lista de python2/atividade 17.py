# A série de Fibonacci é formada pela sequência
# 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o
# valor seja maior que 500. 

n = 500
fibonacci1 = 0
fibonacci2 = 1
fibonacci3 = 0

while fibonacci3 < 500:
    print(f"{fibonacci3}")

    fibonacci3 = fibonacci1 + fibonacci2
    fibonacci1 = fibonacci2
    fibonacci2 = fibonacci3

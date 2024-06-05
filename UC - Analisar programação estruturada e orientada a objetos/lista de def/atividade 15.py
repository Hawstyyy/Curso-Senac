# Crie um programa que converte uma temperatura em graus Celsius para Fahrenheit. A
# fórmula de conversão é: F=(C * 9/5)+32

def C_to_F(n):
  Fahrenheit = (n * 9/5) + 32

  print(f"\n- A temperatura {n}°C é {Fahrenheit}°F em Fahrenheit")

C_to_F(n = float(input("\n- Insira o temperatura em celsius que deseja converter: ")))
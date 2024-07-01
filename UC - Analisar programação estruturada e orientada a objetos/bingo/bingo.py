import random
sorteado_final = []
sorteado = []

class Bingo():
  def sorte(self):
    while True:
      numero = random.randint(1,75)
      letra = ["B","I","N","G","O"]
      letra_sort = random.choice(letra)

      if len(sorteado) > 1:
        if numero not in sorteado:
          sorteado.append(numero)
        else:
          continue
      else:
        sorteado.append(numero)
      
      if numero < 15 and letra_sort == "B":
        sorteado_final.append(str(numero) + letra_sort)
      elif numero > 15 and numero < 30 and letra_sort == "I":
        sorteado_final.append(str(numero) + letra_sort)
      elif numero > 30 and numero < 45 and letra_sort == "N":
        sorteado_final.append(str(numero) + letra_sort)
      elif numero > 45 and numero < 60 and letra_sort == "G":
        sorteado_final.append(str(numero) + letra_sort)
      elif numero > 60 and numero < 75 and letra_sort == "O":
        sorteado_final.append(str(numero) + letra_sort)
      else:
        continue
      

      print(", ".join(map(str, sorteado_final)))
      break
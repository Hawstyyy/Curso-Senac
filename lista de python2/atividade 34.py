# O Departamento Estadual de Meteorologia lhe contratou para 
# desenvolver um programa que leia as um conjunto indeterminado de 
# temperaturas, e informe ao final a menor e a maior temperaturas 
# informadas, bem como a média das temperaturas.

temps = []

while True:
  temp = input("\n- Insira a temperatura, digite Sair para sair: ").capitalize()
  if temp == "Sair":
    break
  else:
    temps.append(float(temp))

media = sum(temps) / len(temps)

print(f"""
- A menor temperatura registrada foi de: {min(temps)}°
- A maior temperatura registrada foi de: {max(temps)}°
- A temperatura média foi de: {media}°
""")

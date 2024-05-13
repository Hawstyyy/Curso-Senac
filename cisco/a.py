hora = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins += dura

if mins >= 60:
    doacao = mins // 60
    mins = mins % 60
    hora += doacao

if hora >= 24:
    hora = hora % 24

print(f"{hora}:{mins}")
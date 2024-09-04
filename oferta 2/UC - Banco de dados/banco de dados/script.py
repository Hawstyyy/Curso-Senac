import mysql.connector as sql

conn = sql.connect(
  host="10.28.2.16",
  user="suporte",
  password="suporte",
  database="cadastros"
)
if conn.is_connected():
  print("Conectado")
else:
  print("Foi nao pae")

cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT telefone_cliente, id_cliente FROM cliente")
fetch = cursor.fetchall()

for registro in fetch:
  new = ''
  conta = 0
  # print(x['id_cliente'], x['telefone_cliente'])
  for x in registro['telefone_cliente']:
    if conta == 2:
      
      new += "9"
      conta += 1
    
    conta += 1
    new += x
  query = "update cliente set telefone_cliente=%s where id_cliente=%s"
  registros = cursor.execute(query, (new, registro['id_cliente']))
  conn.commit()
  print(new)



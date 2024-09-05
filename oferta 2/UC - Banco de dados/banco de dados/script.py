import mysql.connector as sql
new_count = []
new_count_email = []

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


def opcao_num():
  cursor.execute("SELECT telefone_cliente, id_cliente FROM cliente")
  fetch_telefone = cursor.fetchall()
  for registro in fetch_telefone:
    new = ''
    conta = 0
    for x in registro['telefone_cliente']:
      if conta == 2:
        new += "9"
        conta += 1
      conta += 1
      new += x
    new_count.append(new)
    query = "update cliente set telefone_cliente=%s where id_cliente=%s"
    registros = cursor.execute(query, (new, registro['id_cliente']))
    conn.commit()
  print(f"{len(new_count)} números alterados com sucesso")
    

def opcao_email():
  cursor.execute("SELECT email_cliente, id_cliente FROM cliente")
  fetch_email = cursor.fetchall()

  for email in fetch_email:
    new = ''
    count = 0
    if email['id_cliente'] >= 20 and email['id_cliente'] < 45:
      email['email_cliente'].split('@')
      print(new)
      new_count_email.append(new)
    
    # query = "update cliente set email_cliente=%s where id_cliente=%s"
    # registros = cursor.execute(query, (new, email['id_cliente']))
    # conn.commit()
  print(f"{len(new_count_email)} números alterados com sucesso")

while True:
  print("\n--- Menu Principal ---")
  print("1. Adicionar um 9 nos números")
  print("2. Trocar email")
  print("3. Sair")
  escolha = input("Escolha uma opção (1-3): ")
  if escolha == '1':
    opcao_num()
  elif escolha == '2':
    opcao_email()
  elif escolha == '3':
    print("Saindo do programa...")
    break
  else:
    print("Opção inválida. Tente novamente.")
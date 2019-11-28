import MySQLdb

# Abrindo conexão com banco de dados
conn = MySQLdb.connect(host='localhost',
                       user='root',
                       passwd='')

# iniciado o cursos
cursor = conn.cursor()

# selecione o database
conn.select_db('Seudatabase')

# executa o comando sql
cursor.execute("SELECT * FROM customers")

# resultado com fetchall, que busca todas as linhas da ultima instrucao executada.
result = cursor.fetchall()

for x in result:
  print(x)

# fechando a conexao
conn.close()
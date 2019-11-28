import MySQLdb

# Abrindo conexão com banco de dados
conn = MySQLdb.connect(host='localhost',
                        user='root',
                        passwd=''
                        )

# iniciado o cursor
cursor = conn.cursor()



# criar table
cursor.execute("CREATE TABLE Bucket_info (name VARCHAR(255))")

# Verificar tabelas
cursor.execute("SHOW TABLES")

for x in cursor:
  print(x)

# fechando a conexao
conn.close()
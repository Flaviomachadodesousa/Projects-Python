import MySQLdb

# Abrindo conexão com banco de dados
conn = MySQLdb.connect(host='localhost',
                       user='root',
                       passwd='')

# iniciado o cursos
cursor = conn.cursor()

conn.select_db('bucket.sql')

# executando script SQL
cursor.execute('CREATE DATABASE IF NOT EXISTS bucket.sql')

# comite do scrit SQL
conn.commit()

# fechando a conexao
conn.close()
import MySQLdb


conn = MySQLdb.connect('localhost',
                       'root',
                       '',
                       'db3aws',
                       )
print("Succesfully Connected to database using MySQLdb!")

# fechando a conexao
conn.close()
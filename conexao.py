import mysql.connector

class Conexao():
    def conectar():
        #conectando 
        mydb = mysql.connector.connect(
        host="10.110.140.136",
        user="equipe",
        password="123456789",
        database="COLAZAP"
        )

        return mydb

# Criar uma conexão com o banco de dados
mydb = Conexao.conectar()

# Criar um objeto cursor para executar instruções SQL
mycursor = mydb.cursor()

# Executar a consulta SQL para obter os nomes das colunas da tabela tb_mensagem
mycursor.execute("DESCRIBE tb_mensagem")

# Recuperar os nomes das colunas da tabela tb_mensagem
colunas = mycursor.fetchall()

# Imprimir os nomes das colunas
print("Nomes das colunas da tabela tb_mensagem:")
for coluna in colunas:
    print(coluna[0])

# Fechar o cursor e a conexão para liberar recursos
mycursor.close()
mydb.close()
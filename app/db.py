import mysql.connector
from flask import app
from ..config import Config
import mysql.connector

#conectando ao banco de dados
def create_db_connection():
    db_config = {
        'user': Config.DB_USER,
        'password': Config.DB_PASSWORD,
        'host': Config.DB_HOST,
        'database': Config.DB_NAME,
        'port': Config.DB_PORT
    }    
    return mysql.connector.connect(**db_config)
def close_db_connection(connection):
    connection.close()

#validar login
def validar_login(username, password):
    # Configurar a conexão com o banco de dados
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()
    # Executar a consulta para verificar se o usuário e a senha estão corretos
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    # Verificar se o usuário foi encontrado e se a senha corresponde
    if user:
        # Dados de login válidos
        return True
    else:
        # Dados de login inválidos
        return False

    # Fechar a conexão e o cursor
    cursor.close()
    cnx.close()

    
#criar usuario
def create_usuario(username, password):
    
    data = request.json
    username = data.get('username')
    password = data.get('password')

    connection = create_db_connection()
    cursor = connection.cursor()

    # Inserir o usuário no banco de dados
    query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
    values = (username, password)
    cursor.execute(query, values)
    connection.commit()

    close_db_connection(connection)
    # Fechando a conexão
    cursor.close()
    conn.close()

#atualizar usuario
def update_user(user_id, new_data):
    connection = create_db_connection(**db_config)
    cursor = connection.cursor()

    update_query = """
        UPDATE users
        SET name = %s, email = %s
        WHERE id = %s
    """

    try:
        cursor.execute(update_query, (new_data['name'], new_data['email'], user_id))
        connection.commit()
        return True
    except mysql.connector.Error as error:
        print(f"Error updating user: {error}")
        return False
    finally:
        close_db_connection(connection)


#deletar usuario
def delete_user(user_id):
    connection = create_db_connection(**db_config)
    cursor = connection.cursor()

    delete_query = """
        DELETE FROM users
        WHERE id = %s
    """

    try:
        cursor.execute(delete_query, (user_id,))
        connection.commit()
        return True
    except mysql.connector.Error as error:
        print(f"Error deleting user: {error}")
        return False
    finally:
        close_db_connection(connection)

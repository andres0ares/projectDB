#from sqlalchemy import create_engine, text
import pymysql
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()

        # Usa as variáveis de ambiente
        self.DATABASE_HOST = os.getenv("DATABASE_HOST")
        self.DATABASE_PORT = int(os.getenv("DATABASE_PORT"))
        self.DATABASE_USER = os.getenv("DATABASE_USER")
        self.DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")

    def get_connection(self):
        # Conexão com o banco de dados
        timeout = 10
        return pymysql.connect(
            charset="utf8mb4",
            connect_timeout=timeout,
            cursorclass=pymysql.cursors.DictCursor,
            db=self.DATABASE_NAME,
            host=self.DATABASE_HOST,
            password=self.DATABASE_PASSWORD,
            read_timeout=timeout,
            port=self.DATABASE_PORT,
            user=self.DATABASE_USER,
            write_timeout=timeout,
        )

    def execute_query(self, sql_query,  values=None):
        # Obtém uma conexão com o banco de dados
        connection = self.get_connection()
        
        try:
            cursor = connection.cursor()
            if values:
                cursor.execute(sql_query, values)
            else:
                cursor.execute(sql_query)

            # Commit da transação para efetivar as alterações no banco de dados
            connection.commit()

            return cursor.fetchall()
        finally:
            # Fecha a conexão após a consulta
            connection.close()

    def queryMany(self, sql_query):
        # Obtém uma conexão com o banco de dados
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            return cursor.fetchall()
        finally:
            # Fecha a conexão após a consulta
            connection.close()

    def queryOne(self, sql_query):
        # Obtém uma conexão com o banco de dados
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            return cursor.fetchone()
        finally:
            # Fecha a conexão após a consulta
            connection.close()

    def queryModify(self, sql_query):
        # Obtém uma conexão com o banco de dados
        connection = self.get_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)
            connection.commit()

            return cursor
        finally:
            # Fecha a conexão após a consulta
            connection.close()
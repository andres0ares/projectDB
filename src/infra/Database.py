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

    def query(self, sql_query):
        # Obtém uma conexão com o banco de dados
        connection = self.get_connection()
        
        try:
            cursor = connection.cursor()
            cursor.execute(sql_query)

            # Se a consulta é de modificação, faz o commit da transação para efetivar as alterações no banco de dados
            if sql_query.strip().split()[0].lower() in ['insert', 'update', 'delete']:
                connection.commit()

                # Retorna o ID da última linha inserida
                return cursor.lastrowid
            else:
                # Se não for uma consulta de modificação, retorna os resultados da consulta
                return cursor.fetchall()
        finally:
            # Fecha a conexão após a consulta
            connection.close()
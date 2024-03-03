from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):

        # Carrega as variáveis de ambiente do arquivo .env
        load_dotenv()

        # Usa as variáveis de ambiente
        DATABASE_HOST = os.getenv("DATABASE_HOST")
        DATABASE_PORT = os.getenv("DATABASE_PORT")
        DATABASE_USER = os.getenv("DATABASE_USER")
        DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
        DATABASE_NAME = os.getenv("DATABASE_NAME")

        # Constroe a URL de conexão com o banco de dados
        DATABASE_URL = f"mysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

        self.engine = create_engine(DATABASE_URL)

    def execute_query(self, sql_query):
        with self.engine.connect() as conn:
            result = conn.execute(text(sql_query))
            rows = result.fetchall()
            return rows
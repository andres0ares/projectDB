# Instalar Dependencias
pip install -r requirements.txt

# Arquivo .env

Importante criar um arquivo .env na raiz do projeto e adicionar os campos substituindo os valores:

DATABASE_HOST=host  
DATABASE_PORT=3306  
DATABASE_USER=user  
DATABASE_PASSWORD=password  
DATABASE_NAME=name  

# Rodar Localmente
uvicorn src.main:app --reload
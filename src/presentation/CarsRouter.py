from fastapi import APIRouter
from src.infra.Database import Database
router = APIRouter()

@router.get("/api/")
async def execute_query():
    print('here')

    db = Database()

    query = "SELECT * FROM newrma.pergunta_avaliacao;"
    result = db.execute_query(query)

    return result
    # try:
    #     with engine.connect() as conn:
    #         result = conn.execute(text(sql_query))
    #         rows = result.fetchall()
    #         return rows
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
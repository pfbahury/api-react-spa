from fastapi import APIRouter, HTTPException
from db.db import get_db_connection
from psycopg import Error, sql

router = APIRouter()

@router.get("/boletos/")
def get_boletos():
    conn = get_db_connection() 
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")

    try:
        cursor = conn.cursor()
        query  = sql.SQL("SELECT * FROM boletos;")
        cursor.execute(query)
        boletos = cursor.fetchall()

        if boletos:
            return boletos

    except Error as e:
       raise HTTPException(status_code=500, detail=f"Database Error : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()
from fastapi import APIRouter, HTTPException
from db.db import get_db_connection
from psycopg import Error, sql
from pydantic import BaseModel

class Boleto(BaseModel):
    numero_boleto: str
    data_emissao: str
    data_vencimento: str
    valor: float
    status: str
    cliente: str
    empresa: str


router = APIRouter()

@router.get("/boletos")
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

@router.post("/boletos")
async def post_boletos(boleto: Boleto):
    if not boleto:
        raise HTTPException(status_code=400, detail="Body missing or incomplete")
    
    conn = get_db_connection()
    if conn is None:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO boletos (numero_boleto, data_emissao, data_vencimento, valor, status, cliente, empresa) values (%s,%s,%s,%s,%s,%s,%s)",
            (boleto.numero_boleto, boleto.data_emissao, boleto.data_vencimento, boleto.valor, boleto.status, boleto.cliente, boleto.empresa)
        )
        conn.commit()

        return{"message": "New Item created successfully!"}

    except Error as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database Error : {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()

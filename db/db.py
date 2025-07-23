import psycopg
from psycopg import sql
import os
from dotenv import load_dotenv
from psycopg.rows import dict_row

load_dotenv()  # Load the .env file

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_db_connection():
    try:
        conn = psycopg.connect(
            row_factory=dict_row,
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn 
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
import os
import mysql.connector
from mysql.connector import Error, IntegrityError

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "gerenciamento_projetos"),
    )

def executar(sql, params=(), consulta=False):
    # Executa um comando SQL. SELECT retorna lista de dicionarios;
    # INSERT/UPDATE/DELETE retornam o numero de linhas afetadas.
    conn = cursor = None
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, params)
        if consulta:
            return cursor.fetchall()
        conn.commit()
        return cursor.rowcount
    except IntegrityError as erro:
        if conn:
            conn.rollback()
        if erro.errno == 1062:
            raise ValueError("Registro duplicado (CPF ou e-mail ja cadastrado).")
        if erro.errno in (1451, 1452):
            raise ValueError("Operacao viola o relacionamento: funcionario com "
                             "projetos ou funcionario inexistente.")
        raise
    except Error:
        if conn:
            conn.rollback()
        raise
    finally:
        if cursor:
            cursor.close()
        if conn and conn.is_connected():
            conn.close()

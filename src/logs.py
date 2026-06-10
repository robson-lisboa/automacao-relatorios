import sqlite3
from datetime import datetime

def registrar_log(processo, status):

    conexao = sqlite3.connect("empresa.db")

    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO logs (
        data_execucao,
        processo,
        status
    )
    VALUES (?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        processo,
        status
    ))

    conexao.commit()
    conexao.close()
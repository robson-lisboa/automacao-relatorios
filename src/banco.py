# src/banco.py

import sqlite3

conexao = sqlite3.connect("empresa.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    produto TEXT,
    cliente TEXT,
    cidade TEXT,
    quantidade INTEGER,
    valor_unitario REAL
)
""")

conexao.commit()

print("Banco criado com sucesso!")

conexao.close()
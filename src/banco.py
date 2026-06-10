# src/banco.py
import sqlite3

conexao = sqlite3.connect("empresa.db")

cursor = conexao.cursor()

# Tabela de vendas
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

# Tabela de logs
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_execucao TEXT,
    processo TEXT,
    status TEXT
)
""")

conexao.commit()

print("Banco criado com sucesso!")

conexao.close()
import sqlite3
import pandas as pd

conexao = sqlite3.connect("empresa.db")

df = pd.read_sql_query(
    "SELECT * FROM logs ORDER BY id DESC",
    conexao
)

print(df)

conexao.close()
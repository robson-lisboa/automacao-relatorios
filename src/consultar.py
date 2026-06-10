# src/consultar.py

import sqlite3
import pandas as pd

conexao = sqlite3.connect("empresa.db")

consulta = """
SELECT
    produto,
    SUM(quantidade) AS total_vendido
FROM vendas
GROUP BY produto
ORDER BY total_vendido DESC
"""

df = pd.read_sql_query(consulta, conexao)

print(df)

conexao.close()
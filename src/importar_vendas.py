# src/importar_vendas.py

import sqlite3
import pandas as pd

conexao = sqlite3.connect("empresa.db")

df = pd.read_csv("dados/vendas.csv")

df.to_sql(
    "vendas",
    conexao,
    if_exists="append",
    index=False
)

print("Dados importados!")

conexao.close()
import sqlite3
import pandas as pd

conexao = sqlite3.connect("empresa.db")

df = pd.read_csv("dados/vendas.csv")

df.to_sql(
    "vendas",
    conexao,
    if_exists="replace",
    index=False
)

print("Dados importados!")

conexao.close()
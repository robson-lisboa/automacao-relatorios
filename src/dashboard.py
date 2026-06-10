import sqlite3
import pandas as pd

conexao = sqlite3.connect("empresa.db")

consulta = """
SELECT
    SUM(quantidade * valor_unitario) AS faturamento_total,
    COUNT(*) AS total_vendas
FROM vendas
"""

df = pd.read_sql_query(consulta, conexao)

faturamento = df["faturamento_total"][0]
vendas = df["total_vendas"][0]

print("\n===== DASHBOARD =====")
print(f"Faturamento Total: R$ {faturamento:,.2f}")
print(f"Quantidade de Vendas: {vendas}")

conexao.close()
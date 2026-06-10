import sqlite3
import pandas as pd

conexao = sqlite3.connect("empresa.db")

# Faturamento total e quantidade de vendas
consulta = """
SELECT
    SUM(quantidade * valor_unitario) AS faturamento_total,
    COUNT(*) AS total_vendas
FROM vendas
"""

df = pd.read_sql_query(consulta, conexao)

# Produto campeão
produto = pd.read_sql_query("""
SELECT
    produto,
    SUM(quantidade * valor_unitario) AS faturamento
FROM vendas
GROUP BY produto
ORDER BY faturamento DESC
LIMIT 1
""", conexao)

# Cidade campeã
cidade = pd.read_sql_query("""
SELECT
    cidade,
    SUM(quantidade * valor_unitario) AS faturamento
FROM vendas
GROUP BY cidade
ORDER BY faturamento DESC
LIMIT 1
""", conexao)

print("\n===== DASHBOARD =====")

print(f"Faturamento Total: R$ {df['faturamento_total'][0]:,.2f}")
print(f"Quantidade de Vendas: {df['total_vendas'][0]}")

print(f"Produto Campeão: {produto['produto'][0]}")
print(f"Cidade Campeã: {cidade['cidade'][0]}")

conexao.close()
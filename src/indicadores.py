import sqlite3
import pandas as pd

conexao = sqlite3.connect("empresa.db")

# Faturamento por produto
consulta_produto = """
SELECT
    produto,
    SUM(quantidade * valor_unitario) AS faturamento
FROM vendas
GROUP BY produto
ORDER BY faturamento DESC
"""

df_produto = pd.read_sql_query(consulta_produto, conexao)

print("\n=== FATURAMENTO POR PRODUTO ===")
print(df_produto)

# Faturamento por cidade
consulta_cidade = """
SELECT
    cidade,
    SUM(quantidade * valor_unitario) AS faturamento
FROM vendas
GROUP BY cidade
ORDER BY faturamento DESC
"""

df_cidade = pd.read_sql_query(consulta_cidade, conexao)

print("\n=== FATURAMENTO POR CIDADE ===")
print(df_cidade)

# PASSO 8 - PRODUTO CAMPEÃO
produto_top = df_produto.iloc[0]

print("\n=== PRODUTO CAMPEÃO ===")
print(
    f"{produto_top['produto']} - "
    f"R$ {produto_top['faturamento']:,.2f}"
)

conexao.close()
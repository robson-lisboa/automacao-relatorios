import sqlite3
import pandas as pd

conexao = sqlite3.connect("empresa.db")

# Vendas
df_vendas = pd.read_sql_query(
    "SELECT * FROM vendas",
    conexao
)

# Produto
df_produto = pd.read_sql_query("""
SELECT
    produto,
    SUM(quantidade * valor_unitario) AS faturamento
FROM vendas
GROUP BY produto
ORDER BY faturamento DESC
""", conexao)

# Cidade
df_cidade = pd.read_sql_query("""
SELECT
    cidade,
    SUM(quantidade * valor_unitario) AS faturamento
FROM vendas
GROUP BY cidade
ORDER BY faturamento DESC
""", conexao)

with pd.ExcelWriter(
    "relatorio.xlsx",
    engine="openpyxl"
) as writer:

    df_vendas.to_excel(
        writer,
        sheet_name="Vendas",
        index=False
    )

    df_produto.to_excel(
        writer,
        sheet_name="Produtos",
        index=False
    )

    df_cidade.to_excel(
        writer,
        sheet_name="Cidades",
        index=False
    )

print("Relatório gerado com sucesso!")

conexao.close()
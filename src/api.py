from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()


# =========================
# HOME
# =========================
@app.get("/")
def home():
    return {"mensagem": "API de Indicadores"}


# =========================
# PRODUTOS
# =========================
@app.get("/produtos")
def produtos():

    conexao = sqlite3.connect("empresa.db")

    consulta = """
    SELECT
        produto,
        SUM(quantidade * valor_unitario) AS faturamento
    FROM vendas
    GROUP BY produto
    ORDER BY faturamento DESC
    """

    df = pd.read_sql_query(consulta, conexao)

    conexao.close()

    return df.to_dict(orient="records")


# =========================
# VENDAS
# =========================
@app.get("/vendas")
def vendas():

    conexao = sqlite3.connect("empresa.db")

    df = pd.read_sql_query(
        "SELECT * FROM vendas",
        conexao
    )

    conexao.close()

    return df.to_dict(orient="records")


# =========================
# CIDADES
# =========================
@app.get("/cidades")
def cidades():

    conexao = sqlite3.connect("empresa.db")

    consulta = """
    SELECT
        cidade,
        SUM(quantidade * valor_unitario) AS faturamento
    FROM vendas
    GROUP BY cidade
    ORDER BY faturamento DESC
    """

    df = pd.read_sql_query(consulta, conexao)

    conexao.close()

    return df.to_dict(orient="records")


# =========================
# DASHBOARD AVANÇADO
# =========================
@app.get("/dashboard")
def dashboard():

    conexao = sqlite3.connect("empresa.db")

    resumo = pd.read_sql_query("""
    SELECT
        COALESCE(SUM(quantidade * valor_unitario), 0) AS faturamento_total,
        COUNT(*) AS total_vendas
    FROM vendas
    """, conexao)

    produto = pd.read_sql_query("""
    SELECT
        produto,
        SUM(quantidade * valor_unitario) AS faturamento
    FROM vendas
    GROUP BY produto
    ORDER BY faturamento DESC
    LIMIT 1
    """, conexao)

    cidade = pd.read_sql_query("""
    SELECT
        cidade,
        SUM(quantidade * valor_unitario) AS faturamento
    FROM vendas
    GROUP BY cidade
    ORDER BY faturamento DESC
    LIMIT 1
    """, conexao)

    conexao.close()

    return {
        "faturamento_total": float(resumo["faturamento_total"][0]),
        "total_vendas": int(resumo["total_vendas"][0]),
        "produto_campeao": produto["produto"][0] if not produto.empty else None,
        "cidade_campea": cidade["cidade"][0] if not cidade.empty else None
    }


# =========================
# LOGS
# =========================
@app.get("/logs")
def logs():

    conexao = sqlite3.connect("empresa.db")

    df = pd.read_sql_query(
        "SELECT * FROM logs ORDER BY id DESC",
        conexao
    )

    conexao.close()

    return df.to_dict(orient="records")
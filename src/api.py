from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()


@app.get("/")
def home():
    return {"mensagem": "API de Indicadores"}


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


@app.get("/vendas")
def vendas():

    conexao = sqlite3.connect("empresa.db")

    df = pd.read_sql_query(
        "SELECT * FROM vendas",
        conexao
    )

    conexao.close()

    return df.to_dict(orient="records")


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


@app.get("/dashboard")
def dashboard():

    conexao = sqlite3.connect("empresa.db")

    consulta = """
    SELECT
        SUM(quantidade * valor_unitario) AS faturamento_total,
        COUNT(*) AS total_vendas
    FROM vendas
    """

    df = pd.read_sql_query(consulta, conexao)

    conexao.close()

    return {
        "faturamento_total": float(df["faturamento_total"][0]),
        "total_vendas": int(df["total_vendas"][0])
    }


@app.get("/logs")
def logs():

    conexao = sqlite3.connect("empresa.db")

    df = pd.read_sql_query(
        "SELECT * FROM logs ORDER BY id DESC",
        conexao
    )

    conexao.close()

    return df.to_dict(orient="records")
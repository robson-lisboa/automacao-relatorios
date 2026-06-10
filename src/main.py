from logs import registrar_log

print("=== INICIANDO PROCESSO ===")

try:
    from importar_vendas import *
    print("Importação concluída!")
    registrar_log("IMPORTACAO", "SUCESSO")
except Exception as erro:
    print(f"Erro na importação: {erro}")
    registrar_log("IMPORTACAO", "ERRO")

try:
    from indicadores import *
    print("Indicadores gerados!")
    registrar_log("INDICADORES", "SUCESSO")
except Exception as erro:
    print(f"Erro nos indicadores: {erro}")
    registrar_log("INDICADORES", "ERRO")

try:
    from relatorio import *
    print("Relatório gerado!")
    registrar_log("RELATORIO", "SUCESSO")
except Exception as erro:
    print(f"Erro no relatório: {erro}")
    registrar_log("RELATORIO", "ERRO")

print("=== PROCESSO FINALIZADO COM SUCESSO ===")
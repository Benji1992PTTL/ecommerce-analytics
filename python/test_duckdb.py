import duckdb

# Criar uma ligação temporária ao DuckDB
con = duckdb.connect(database=":memory:")

# Executar uma query SQL
result = con.execute("""
    SELECT
        1 + 1 AS resultado,
        'DuckDB está a funcionar!' AS mensagem
""").fetchdf()

print(result)

# Fechar a ligação
con.close()
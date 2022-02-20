import sqlite3
import pandas as pd

# Conexão com banco de dados
conn = sqlite3.connect("contratos.db")
c = conn.cursor()

def main():

    # Consulta SQL
    sql = """
        SELECT nome_coop, ROUND(AVG(spread_c), 4) as spread
        FROM contratos 
            JOIN cooperativas ON cooperativas.id = contratos.id_coop
        GROUP BY contratos.id_coop
        ORDER BY contratos.id_coop
    """
    # Executar consulta
    query = c.execute(sql).fetchall()
    if query:
        # Campos da tabela
        h = list(map(lambda x: x[0], c.description))
    # Encerrar conexão
    conn.close()

    # Ler consulta em data frames
    df1 = pd.DataFrame(query, columns = h)
    # Dados estatísticos
    df2 = get_stats(df1)

    # Saída de dados
    df1.to_csv("spreads.csv", index = False, encoding="utf-8-sig")
    df2.to_csv("stats.csv", header = False, encoding="utf-8-sig")


# Calcular dados estatísticos
def get_stats(data, rv = {}):

    ma = round(data["spread"].mean(), 4)
    dp = round(data["spread"].std(ddof = 0), 4)
    q1 = round(data["spread"].quantile(q = 0.25), 4)
    q3 = round(data["spread"].quantile(q = 0.75), 4)
    iqr = round(q3 - q1, 4)
    ls = round(ma + 1.5*iqr, 4)
    li = round(ma - 1.5*iqr, 4)

    rv["Média"] = [ma]
    rv["Desvio-P"] = [dp]
    rv["Q1"] = [q1]
    rv["Q3"] = [q3]
    rv["IQR"] = [iqr]
    rv["LS"] = [ls]
    rv["LI"] = [li]

    return pd.DataFrame(rv).transpose()


if __name__ == "__main__":
    main()
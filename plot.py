import matplotlib.pyplot as plt
import pandas as pd
import csv

# Lear em data frames arquivo csv dos spreads
df = pd.read_csv("spreads.csv")

# Eixo x do gráfico
x = list(range(1, df.shape[0] + 1))
# Spread de cada cooperativa
ma = list(df["spread"])

# Ler arquivo csv de dados calculados
with open("stats.csv", "r", newline="", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    rows = list(reader)
    for row in rows:
        match row[0]:
            case "Média":
                # Média dos spreads
                ms = [float(row[1])] * df.shape[0]
            case "LS":
                # Limite superior
                ls = [float(row[1])] * df.shape[0]
            case "LI":
                # Limite inferior
                li = [float(row[1])] * df.shape[0]


# Plotar linhas
plt.plot(x, li, color = "r")
plt.plot(x, ms, color = "#a8a8a8")
plt.plot(x, ls, color = "r")
plt.plot(x, ma, color = "g")

# Título e rótulo dos eixos
plt.title("Limite Superior e Inferior")
plt.xlabel("Observações")
plt.ylabel("Spreads")

# Mostrar gráfico
plt.show()
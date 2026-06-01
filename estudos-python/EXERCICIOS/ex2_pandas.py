import pandas as pd
import numpy as np

dados = {
    "nome": ["Ana", "Bruno", "Carla", "Diego", "Eva", "Felipe", "Gabi", "Hugo", "Iara", "João"],
    "idade": [25, 30, 22, 28, 35, 27, 31, 24, 29, 33],
    "departamento": ["TI", "RH", "TI", "Financeiro", "TI", "Marketing", "RH", "TI", "Financeiro", "Marketing"],
    "salario": [5500, 4800, 6200, 7500, 8000, 5200, 4900, 5800, 7200, 5500],
    "tempo_empresa": [2, 5, 1, 8, 6, 3, 4, 2, 7, 5],
    "nota_avaliacao": [8.5, 7.0, 9.0, 6.5, 9.5, 7.5, 8.0, 8.5, 7.0, 6.0]
}

df = pd.DataFrame(dados)

# exercício1
df["salario_anual"] = df["salario"] * 13
print(df)

# exercício2
df["senioridade"] = df["tempo_empresa"].apply(
    lambda s: "Júnior" if s < 3 else "Pleno" if 3 <= s <= 5 else "Sênior")
print(df)

# exercício3
salario_por_departamento = df.groupby("departamento")["salario"].mean()
print((salario_por_departamento))

# exercício4
qtd_depart = df.groupby("departamento").size()
print(qtd_depart)


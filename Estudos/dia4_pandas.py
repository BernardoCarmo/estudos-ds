import pandas as pd

# Series — uma coluna
notas = pd.Series([8.5, 7.0, 9.0, 6.5, 7.5])
print(notas)
print(notas.mean())

# DataFrame — tabela completa
dados = {
    "nome": ["Ana", "Bruno", "Carla", "Diego", "Eva"],
    "idade": [25, 30, 22, 28, 35],
    "nota": [8.5, 5.0, 9.0, 6.5, 7.5],
    "departamento": ["TI", "RH", "TI", "Financeiro", "TI"]
}

df = pd.DataFrame(dados)
print(df)

# explorando
print(df.head())          # primeiras linhas
print(df.info())          # tipos e nulos
print(df.describe())      # estatísticas das colunas numéricas
print(df.shape)           # (linhas, colunas)
print(df.columns)         # nomes das colunas

# selecionando colunas
print(df["nome"])
print(df[["nome", "nota"]])

# filtrando linhas (aqui o pulo do gato)
aprovados = df[df["nota"] >= 7]
print(aprovados)

ti = df[df["departamento"] == "TI"]
print(ti)

# múltiplas condições
ti_aprovados = df[(df["departamento"] == "TI") & (df["nota"] >= 7)]
print(ti_aprovados)

# groupby — agrupar e agregar
media_por_dept = df.groupby("departamento")["nota"].mean()
print(media_por_dept)

# ordenando
ordenado = df.sort_values("nota", ascending=False)
print(ordenado)

# adicionando coluna
df["status"] = df["nota"].apply(lambda x: "Aprovado" if x >= 7 else "Reprovado")
print(df)
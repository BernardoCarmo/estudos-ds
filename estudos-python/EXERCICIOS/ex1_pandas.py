import pandas as pd

dados = {
    "nome": ["Bernardo", "Sophia", "Luiza", "Isabel", "Simone", "Décio"],
    "idade": [19, 18, 25, 20, 55, 55],
    "nota_tecnica": [52, 75, 70, 71, 69, 72],
    "nota_comportamental": [70, 82, 90, 72, 80, 79],
    "area_desejada": ["Tech", "Marketing", "RH", "RH", "Compras", "Tech"]
}

df = pd.DataFrame(dados)
print(df)

df["media"] = (df["nota_tecnica"] + df["nota_comportamental"]) / 2

media_7 = df[df["media"] > 75]
print(media_7)

media_por_area = df.groupby("area_desejada")["media"].mean()
print(media_por_area)

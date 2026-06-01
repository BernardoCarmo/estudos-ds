import pandas as pd

# carrega o arquivo
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# o "olhar inicial" — sempre comece assim
print("Shape:", df.shape)              # (1470, 35) — 1470 linhas, 35 colunas
print("\nPrimeiras linhas:")
print(df.head())

print("\nColunas disponíveis:")
print(df.columns.tolist())

print("\nTipos de dados:")
print(df.dtypes)

print("\nEstatísticas descritivas:")
print(df.describe())

print("\nValores nulos por coluna:")
print(df.isnull().sum())
